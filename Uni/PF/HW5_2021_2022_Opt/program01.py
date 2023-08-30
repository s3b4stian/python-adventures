# -*- coding: utf-8 -*-
'''
Una serie di poster rettangolari sono stati affissi ad un muro.  I
   loro lati sono orizzontali e verticali. Ogni poster può essere
   parzialmente o totalmente coperto dagli altri. Chiameremo
   perimetro la lunghezza del contorno dell'unione di tutti i posters
   sul muro. Si guardi l'immagine in "posters.png" in cui i poster sulla
   parete compaiono in bianco coi bordi blu e la si confronti con l'immagine
   "posters1.png" in cui in rosso vengono evidenziati i soli
   bordi che contribuiscono al perimetro.

Vogliamo un programma che calcola il perimetro dei poster e produce
   una immagine simile a "posters1.png".

Progettare dunque una funzione
     ex1(ftesto, filepng)
   che prenda come parametri
   - ftesto, l'indirizzo di un file di testo contenente le informazioni sulla
     posizione dei poster sul muro,

   - filepng, nome del file immagine in formato PNG da produrre

   e restituisca il perimetro dei poster come numero di pixel rossi.

Il file di testo contiene tante righe quanti sono i poster,
   nell'ordine in cui sono stati affissi alla parete. In ciascuna
   riga ci sono le coordinate intere del vertice in basso a sinistra e
   del vertice in alto a destra del poster. I valori di queste
   coordinate sono dati come coppie ordinate della coordinata x
   seguita dalla coordinata y. Si veda ad esempio il file
   rettangoli_1.txt contenente le specifiche per i 7 posters in
   "posters.png".
   
L'immagine da salvare in filepng deve avere lo sfondo nero, altezza h
   +10 e larghezza w+10 dove h è la coordinata y massima del muro su
   cui compaiono poster e w la coordinata x massima del muro su cui
   compaiono posters. I bordi visibili dei poster sono colorati di
   rosso o di verde a seconda che appartengano al perimetro o meno.
   Notare che un pixel si trova sul perimetro (e quindi è rosso) se nel
   suo intorno (gli 8 pixel adiacenti) si trova almeno un pixel esterno
   a tutti i poster.

   Per caricare e salvare i file PNG si possono usare le funzioni load
   e save presenti nel modulo "images".

Per esempio: ex1('rettangoli_1.txt', 'test_1.png') deve costruire un file PNG
   identico a "posters1.png" e restituire il valore 1080.
   
NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun
   test

ATTENZIONE: quando caricate il file assicuratevi che sia nella
    codifica UTF8 (ad esempio editatelo dentro Spyder)

'''

import images

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, point_sw: Point, point_ne: Point, z_index: int):
        # lower left point
        self.sw = point_sw
        # high right point
        self.ne = point_ne

        # z index, indicates the z values in 3D representation
        self.z_index = z_index

        # height and width values
        # mul for -1 because there are negative heights
        # rectangle where sw point in above ne point
        self.h = (point_ne.y - point_sw.y) * -1
        self.w = (point_sw.x - point_ne.x) * -1

        # high left point
        self.nw = Point(point_ne.x - self.w, point_ne.y)
        # lower right point
        self.se = Point(point_sw.x + self.w, point_sw.y)

    def __str__(self):
        return f"Rectangle(h={self.h}, w={self.w}, " \
               f"sw=({self.sw.x}, {self.sw.y}), "    \
               f"nw=({self.nw.x}, {self.nw.y}), "    \
               f"ne=({self.ne.x}, {self.ne.y}), "    \
               f"se=({self.se.x}, {self.se.y}))"


def point_inside(img_w: int, img_h: int, x: int, y: int) ->bool:
    """
    Checks if a vertex of the rectangel in inside of the image area

    Parameters
    ----------
    img_w : int
        image width.
    img_h : int
        image height.
    x : int
        x coordinate of the vertex.
    y : int
        y coordinate of the vertex.

    Returns
    -------
    bool
        True if the vertex of the triangle is inside else False.

    """

    return 0 <= x < img_w and 0 <= y < img_h


def inside(r: Rectangle, img_w: int, img_h: int) ->bool:
    """
    Checks if all vertex of the rectangle are inside the image

    Parameters
    ----------
    r : Rectangle
        rectangle to check.
    img_w : int
        image width.
    img_h : int
        image height.

    Returns
    -------
    bool
        True if the whole rectangle is inside the area of the image else False.

    """

    return point_inside(img_w, img_h, r.sw.x, r.sw.y) and \
           point_inside(img_w, img_h, r.ne.x, r.ne.y) and \
           point_inside(img_w, img_h, r.nw.x, r.nw.y) and \
           point_inside(img_w, img_h, r.se.x, r.se.y)


def draw_inner(rect: Rectangle, l_f: list, l_w: list) ->None:
    """
    draws the rectangle inner using a solid color.
    fills the withe layer with a number representing the quote of the
    rectangle. Aka z_index like in css

    Parameters
    ----------
    rect : Rectangle
        rectangle to draw.
    l_f : list
        final layer, the image.
    l_w : list
        white layer, growing z_index

    Returns
    -------
    None

    """

    # heigth and width of the rectangle
    h = rect.h + 1
    w = rect.w + 1

    # z index of the rectangle
    z = rect.z_index

    # starting point
    x = rect.sw.x
    y = rect.sw.y

    for i in range(h):
        f_y = y - i
        # new method
        l_f[f_y][x:x + w] = [(255, 255, 255)] * w
        l_w[f_y][x:x + w] = [z] * w

        # old method
        # for c in range(w):
        #     f_x = x + c
        #     # fill the white layer with the z_index of the rectangle
        #     l_w[f_y][f_x] = z
        #     # fill the final layer with the white color
        #     l_f[f_y][f_x] = (255, 255, 255)


def is_internal(l_w: list, y: int, x: int) ->bool:
    """
    checks if a point has a black point around.

    Parameters
    ----------
    l_w : list
        final layer, the image.
    y : int
        y coordinate of the point.
    x : int
        x coordinate of the point.

    Returns
    -------
    bool
        True if the point doesn't have any black point around else False.

    """

    # get pixels around
    p_N     = l_w[y - 1][x]
    p_NE    = l_w[y - 1][x + 1]
    p_NW    = l_w[y - 1][x - 1]
    p_E     = l_w[y][x + 1]
    p_W     = l_w[y][x - 1]
    p_S     = l_w[y + 1][x]
    p_SW    = l_w[y + 1][x - 1]
    p_SE    = l_w[y + 1][x + 1]
    
    return bool(p_N      * \
                p_NE     * \
                p_NW     * \
                p_E      * \
                p_W      * \
                p_S      * \
                p_SW     * \
                p_SE)


def draw_line_vertical(x: int,
                       y: int,
                       h: int,
                       z_index: int,
                       l_f: list,
                       l_w: list,
                       l_r: list) ->None:
    """
    draws a vertical line, used for draw the red or green border

    Parameters
    ----------
    x : int
        x coordinate of the starting point.
    y : int
        y coordinate of the starting point.
    h : int
        lenght of the line.
    z_index : int
        the level that identify the rectagle.
    l_f : list
        final layer, the image.
    l_w : list
        white layer, the rectangle as z_index
    l_r : list
        red layer, the red dots layer.

    Returns
    -------
    None

    """

    r = (255, 0, 0)
    g = (0, 255, 0)

    for i in range(h):
        f_y = y - i
        # if the point belongs the current rectangle
        if l_w[f_y][x] == z_index:
            # fill the point with the green color
            l_f[f_y][x] = r
            # if the point is boundary, it has a black pixel near
            if is_internal(l_w, f_y, x):
                # turn the point to red color
                l_f[f_y][x] = g
                continue
            # set to 1 the same point into the red layer
            l_r.add((f_y, x))


def draw_line_horizontal(x: int,
                       y: int,
                       w: int,
                       z_index: int,
                       l_f: list,
                       l_w: list,
                       l_r: list) ->None:
    """
    draws a horizontal line, used for draw the red or green border

    Parameters
    ----------
    x : int
        x coordinate of the starting point.
    y : int
        y coordinate of the starting point.
    w : int
        lenght of the line.
    z_index : int
        the level that identify the rectagle.
    l_f : list
        final layer, the image.
    l_w : list
        white layer, the rectangle as z_index
    l_r : list
        red layer, the red dots layer.

    Returns
    -------
    None

    """
    r = (255, 0, 0)
    g = (0, 255, 0)

    for i in range(w):
        f_x = x + i
        # if the point belongs the current rectangle
        if l_w[y][f_x] == z_index:
            # fill the point with the green color
            l_f[y][f_x] = r
            # if the point is boundary, it has a black pixel near
            if is_internal(l_w, y, f_x):
                # turn the point to red color
                l_f[y][f_x] = g
                continue
            # set to 1 the same point into the red layer
            l_r.add((y, f_x))


def draw_border(rect: Rectangle, l_f: list, l_w: list, l_r: list) ->None:
    """
    draws a rectangle border.

    Parameters
    ----------
    rect : Rectangle
        rectangle to be drawn.
    l_f : list
        final layer, the image.
    l_w : list
        white layer, the rectangle as z_index
    l_r : list
        red layer, the red dots layer.

    Returns
    -------
    None

    """

    # draw sw to nw line
    # vertical line left
    draw_line_vertical(rect.sw.x,       \
                       rect.sw.y,       \
                       rect.h,          \
                       rect.z_index,    \
                       l_f, l_w, l_r)

    # draw sw to se line
    # horizontal line bottom
    draw_line_horizontal(rect.sw.x,     \
                         rect.sw.y,     \
                         rect.w,        \
                         rect.z_index,  \
                         l_f, l_w, l_r)

    # draw nw to ne line
    # horizontal line top
    draw_line_horizontal(rect.nw.x,     \
                         rect.nw.y,     \
                         rect.w,        \
                         rect.z_index,  \
                         l_f, l_w, l_r)

    # draw se to ne line
    # vertical line right
    draw_line_vertical(rect.se.x,       \
                       rect.se.y,       \
                       rect.h + 1,      \
                       rect.z_index,    \
                       l_f, l_w, l_r)


def create_rectangles(r: list, r_c: list, y_point: list, x_point: list) ->None: 
    """
    create a collection of Rectagle object starting from a list of values
    read from a file.

    Parameters
    ----------
    r : list
        a list of coordinates from a file.
    r_c : list
        void collection to fill.
    y_point : list
        list to collect y coordinate.
    x_point : list
        list to collect x coordinate.

    Returns
    -------
    None

    """

    # for every couple of coordinates in the list
    for z_index, rect in enumerate(r):
        # convert to integer type
        coordinates = list(map(int, rect.strip().split()))

        # get coordinates of the two points
        p_sw = tuple(coordinates[0:2])
        p_ne = tuple(coordinates[2:4])

        # create Point objects
        p_sw_tmp = Point(p_sw[0], p_sw[1])
        p_ne_tmp = Point(p_ne[0], p_ne[1])

        # add x value to the list of x
        x_point.add(p_sw_tmp.x)
        x_point.add(p_ne_tmp.x)

        # add y value to the list of y
        y_point.add(p_sw_tmp.y)
        y_point.add(p_ne_tmp.y)

        # add the new Rectangle object to the rectangle collention
        r_c.append(Rectangle(p_sw_tmp, p_ne_tmp, z_index + 1))


def create_layer(c, x: int, y: int) ->list:
    """
    create avoid layer filled with c

    Parameters
    ----------
    c : any
        value to fill the layer/matrix.
    x : int
        columns of the matrix.
    y : int
        rows of the matrix.

    Returns
    -------
    list
        the matrix filled with c.

    """

    return [ [c] * x for _ in range(y)]


# def red_dots(l_r: list) ->int:
#     """
#     count the number of red dots into the layer.

#     Parameters
#     ----------
#     l_r : list
#         red layer, the red dots layer.

#     Returns
#     -------
#     int
#         the number of red dots into the layer.

#     """

#     reds = 0
#     for c in l_r:
#         reds += sum(c)
#     return reds


def ex1(ftesto, filepng):
    with open(ftesto, encoding='utf-8') as f:
         rectangles = f.readlines()

    # declare a void rectangles collection
    rect_collection = []

    y_point = set()
    x_point = set()

    # create rectangle collection from values into the file
    create_rectangles(rectangles, rect_collection, y_point, x_point)

    # define final image dimensions
    img_h = max(y_point) + 10
    img_w = max(x_point) + 10

    # create layers
    layer_final = create_layer((0,0,0), img_w, img_h)
    layer_white = create_layer(0, img_w, img_h)
    layer_red = set()

    # draw rettangles inner
    for r in rect_collection:
        if inside(r, img_w, img_h):
            draw_inner(r, layer_final, layer_white)

    # draw rettangles border
    for r in rect_collection:
        if inside(r, img_w, img_h):
            draw_border(r, layer_final, layer_white, layer_red)

    # save image
    images.save(layer_final, filepng)

    # return ne number of red dors into the image
    return len(layer_red)


if __name__ == '__main__':
    print(ex1('rectangles_185.txt', 'test_185.png'))
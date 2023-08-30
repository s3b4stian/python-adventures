# -*- coding: utf-8 -*-
''' 
Il sindaco si una città deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi può
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrà disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrà i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere più vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profondità.  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o più spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo è rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrà essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi più
    alti delle due fasce consecutive. 
    Il palazzo più grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore. 
    Il palazzo più grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore 
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''
import images

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Building:

    def __init__(self, point_sw: Point, w: int, h: int, color: tuple):
        # lower left point
        self.sw = point_sw

        # rectangel color
        self.color = color

        # height and width values
        self.h = h
        self.w = w

    def __str__(self):
        return f"Building(h={self.h}, w={self.w}, " \
               f"sw=({self.sw.x}, {self.sw.y}), "    \
               f"nw=({self.color}, {self.color}), "


def draw_inner(rect: Building, l_f: list) ->None:
    """
    Draws the rectangle inner using a solid color.
    fills the withe layer with a number representing the quote of the
    rectangle. Aka z_index like in css

    Parameters
    ----------
    rect : Rectangle
        rectangle to draw.
    l_f : list
        final layer, the image.

    Returns
    -------
    None

    """

    # heigth and width of the rectangle
    h = rect.h
    w = rect.w

    # rectangle color
    c = rect.color

    # starting point
    x = rect.sw.x
    y = rect.sw.y

    for i in range(h):
        f_y = y - i
        l_f[f_y][x:x + w] = [c] * w


def create_layer(c, x: int, y: int) ->list:
    """
    Create avoid layer filled with c

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

    return [[c] * x for _ in range(y)]


def get_buildings_file(file_data: str) ->list:
    """
    Read buildings data from a file of data.

    Parameters
    ----------
    file_data : str
        path to file with buildings data.

    Returns
    -------
    list
        a list of list where every list contain on or more building data.

    """

    # internal function
    # clean a row from tab and spaces
    def clean_rows(f):
        return [[e.strip() for e in c.split(',')][:-1] for c in f.readlines()]

    # internal function
    # convert all values to int
    def set_type(l):
        return [tuple(map(int, r)) for r in l]

    with open(file_data, encoding='utf-8') as f:
        lines = clean_rows(f)
        lines = set_type(lines)

    # make chunks every 5 values
    return [tuple([l[x:x + 5] for x in range(0, len(l), 5)]) for l in lines]


def get_buildings_properties(b_l: list) ->tuple:
    """
    return the properties of the buildings into the row

    Parameters
    ----------
    b_l : list
        a list of buildings where every building is a list of five
        integers like [20,50,255,0,0] -> [w,h,r,g,b].

    Returns
    -------
    tuple
        contains three lists, first the width of all buildings, second
        the height of all buildings.

    """

    # all w (r[0]) of the buildings in row
    # all h (r[1]) of the buildings in row
    return [r[0] for r in b_l], [r[1] for r in b_l], 


def get_buildings_measures(b: list,
                           s: int,
                           r_m: list,
                           l_img_w: list,
                           l_img_h: list) ->None:
    """
    fill lists passed as argument with building properties

    Parameters
    ----------
    b : list
        all buildings, a list of lists where every list is a row of buildins.
    s : int
        spacing.
    r_m : list
        list of tuples (one for row) where every tuple composed by:
            - sum of all w of the buildings in row
            - number of buildings in row
            - most length building of the row
    l_img_w : list
        contains all width of every row of buildings plus the spacing
        between buildings.
    l_img_h : list
        contains all max height of every row of buildings.

    Returns
    -------
    None

    """

    #for every row of buildings
    for b_l in b:

        # create a list of w, h and color
        l_w, l_h = get_buildings_properties(b_l)

        # sum of all w of the buildings in row
        s_l_w = sum(l_w)
        # number of buildings in row
        l_l_w = len(l_w)
        # most length building of the row
        m_l_h = max(l_h)

        r_m.append((s_l_w, l_l_w, m_l_h))

        # append the sum of all w of buildings plus spacing
        l_img_w.append((l_l_w + 1) * s + s_l_w)
        # append the the max h of the row
        l_img_h.append(m_l_h)


def draw_buildings_row(b_l: list,
                       m_h: int,
                       x: int,
                       y: int,
                       s: int,
                       l_f: list) ->None:
    """
    draws a row of buildings.

    Parameters
    ----------
    b_l : list
        a list of buildings where every building is a list of five
        integers like [20,50,255,0,0] -> [w,h,r,g,b].
    m_h : int
        most length building of the row.
    x : int
        x cordinate of the south west point of the building.
    y : int
        y cordinate of the south west point of the building.
    s : int
        building spacing.
    l_f : list
        final layer, the image.

    Returns
    -------
    None

    """

    rel_y = y

    # for every building in row
    for w, h, r, g, b in b_l:

        # make centering operation
        rel_y -= (m_h - h) // 2

        # draw the building
        draw_inner(Building(Point(x, rel_y), w, h, (r, g, b)), l_f)

        # update coordinates
        # for the next rectangle
        x += w + s
        rel_y = y


def ex(file_dati, file_png, spaziatura):

    buildings = get_buildings_file(file_dati)

    # lists for w and h of every building
    l_img_w = []
    l_img_h = []

    # list of measures needed to calculate buildings position
    row_measures = []

    # fill lists with buildings measures
    get_buildings_measures(buildings, spaziatura, row_measures, l_img_w, l_img_h)

    # image w, the max value
    img_w = max(l_img_w)

    # id of the row of the max value
    # img_w_idx = l_img_w.index(img_w)

    # image h, the sum of all max h plus spacing
    img_h = (len(l_img_h) + 1) * spaziatura + sum(l_img_h)

    layer_final = create_layer((0,0,0), img_w, img_h)

    # y initial position
    start_y = -1

    #for every row of buildings
    for idx_y, b_l in enumerate(buildings):

        # get the:
        #  - s_l_w : sum of all w of the buildings in row
        #  - l_l_w : number of buildings in row
        #  - m_l_h : most length building of the row
        s_l_w, l_l_w, m_l_h = row_measures[idx_y]

        # initial coordinates
        # copy of spaziatura to spacing
        start_x = spacing = spaziatura
        start_y += spaziatura + m_l_h

        # if the building is alone into the row
        #  - l_l_w : number of buildings in row
        if l_l_w == 1:
            # unpack building attributes
            w, h, r, g, b = b_l[0]

            # center the building
            start_x = (img_w - w) // 2

            # draw the building
            draw_inner(Building(Point(start_x, start_y), w, h, (r, g, b)), layer_final)
            continue

        # commented, reduce complexity to 3
        # if the row isn't the row that enstablishes the w of the image
        # if idx_y != img_w_idx:
        # calculate new spacing
        spacing = (img_w - (spaziatura * 2) - s_l_w) // (l_l_w - 1)

        draw_buildings_row(b_l, m_l_h, start_x, start_y, spacing, layer_final)

    # save the image
    images.save(layer_final, file_png)

    return (img_w, img_h)

# test-id    spacing   exp_dimensions   timeout
# ( 'example',   42,      ( 288, 348),     0.5),
# ( 'minimal',   30,      (  82, 140),     0.5),
# ( 'mat-3-1',    1,      ( 466, 120),     0.5),
# ( 'mat-4-5',    5,      ( 120,  61),     0.5),
# ( 'mat-5-5',    5,      ( 150,  78),     0.5),
# ( 'mat-2-97',  97,      ( 690, 341),     0.5),
# ( 'mat-23-2',   2,      ( 882, 802),     0.5),
# ( 'mat-53-1',   1,      ( 600,1748),     0.5),
# ( 'mat-12-25', 25,      (2362, 813),     1.0),
# ( 'mat-16-25', 25,      (2822,1071),     1.0)
if __name__ == '__main__':
    file_dati   = "secrets/mat-wide.txt"
    file_png    = "test_mat-wide.png"
    spaziatura  = 25
    print(ex(file_dati, file_png, spaziatura))


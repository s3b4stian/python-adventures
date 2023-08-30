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


class Rectangle:

    def __init__(self, point_sw: Point, w: int, h: int, color: tuple):
        # lower left point
        self.sw = point_sw

        # rectangel color
        self.color = color

        # height and width values
        self.h = h
        self.w = w

    def __str__(self):
        return f"Rectangle(h={self.h}, w={self.w}, " \
               f"sw=({self.sw.x}, {self.sw.y}), "    \
               f"nw=({self.color}, {self.color}), "


def draw_inner(rect: Rectangle, l_f: list) ->None:
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


def get_buildings_file(file_dati: str) ->tuple:
    with open(file_dati, encoding='utf-8') as f:
         tmp_lines = [''.join([b for b in c if b.isdigit() or b == ',' ]).split(',') for c in f.readlines()]

         buildings = []
         for l in tmp_lines:
             l = list(map(int,[r for r in l if r.isdigit()]))
             chunks = [l[x:x + 5] for x in range(0, len(l), 5)]
             buildings.append(chunks)
    
    return buildings


def get_buildings_properties(b: list) ->tuple:
    # l_w = []
    # l_h = []
    # l_c = []
    
    # for r in b:
    #     l_w.append(r[0])
    #     l_h.append(r[1])
    #     l_c.append(tuple([r[2],r[3],r[4]]))
   
    l_w = [r[0] for r in b]
    l_h = [r[1] for r in b]
    l_c = [tuple([r[2],r[3],r[4]]) for r in b]

    return l_w, l_h, l_c


def ex(file_dati, file_png, spaziatura):

    # with open(file_dati, encoding='utf-8') as f:
    #      tmp_lines = [''.join([b for b in c if b.isdigit() or b == ',' ]).split(',') for c in f.readlines()]

    #      buildings = []
    #      for l in tmp_lines:
    #          l = list(map(int,[r for r in l if r.isdigit()]))
    #          chunks = [l[x:x + 5] for x in range(0, len(l), 5)]
    #          buildings.append(chunks)

    buildings = get_buildings_file(file_dati)

    # lists for w and h of every building
    l_img_w = []
    l_img_h = []

    # list of all buildings
    rect_collection = [0] * len(buildings)

    # lists for know the number of buildings on avery row
    r_numbers = []
    # list to know the sum of all w of buildings
    r_sum_w = []

    # y initial position
    start_y = -1

    row_mesaures = [0] * len(buildings)

    #for every row of buildings
    for i, b_l in enumerate(buildings):
        # create a list of w, h and color
        l_w, l_h, l_c = get_buildings_properties(b_l)

        row_mesaures.append()

        s_l_w = sum(l_w)
        l_l_w = len(l_w)
        m_l_h = max(l_h)

    #for every row of buildings
    for idx_y, b_l in enumerate(buildings):
        # create a list of w, h and color
        l_w, l_h, l_c = get_buildings_properties(b_l)

        s_l_w = sum(l_w)
        l_l_w = len(l_w)
        m_l_h = max(l_h)

        # append the number of buildings
        r_numbers.append(l_l_w)
        # append the sum of all w of buildings
        r_sum_w.append(s_l_w)

        # initial coordinates
        start_x = spaziatura
        start_y += spaziatura + m_l_h

        # make a copy of start y
        # use the copy to calculate the vertical centering of a building
        rel_y = start_y

        # initialize the row of the list of buildings
        rect_collection[idx_y] = []

        # for every building in row
        for idx_x, (w, h, c) in enumerate(zip(l_w, l_h, l_c)):

            # if the building hasn't the max h
            if h < m_l_h:
                # make centering operation
                rel_y -= (m_l_h - h) // 2

            # append to the rect collection the new building
            rect_collection[idx_y].append(Rectangle(Point(start_x, rel_y), w, h, c))

            # update coordinates
            start_x += spaziatura + w
            rel_y = start_y
        
        # append the sum of all w of buildings plus spacing
        l_img_w.append((l_l_w + 1) * spaziatura + s_l_w)
        # append the the max h of the row
        l_img_h.append(m_l_h)

    # image w, the max value
    img_w = max(l_img_w)
    # id of the row of the max value
    img_w_idx = l_img_w.index(img_w)
    # image h, the sum of all max h plus spacing
    img_h = (len(l_img_h) + 1) * spaziatura + sum(l_img_h)



    # centrate on x axis
    # for every row of buildings in rect collecion
    for idx, row in enumerate(rect_collection):

        # if the number of buildings in row is one
        if r_numbers[idx] == 1:
            # centrate the building
            row[0].sw.x = (img_w - row[0].w) // 2

        # else if the row isn't the row that enstablishes the w of the image
        elif idx != img_w_idx:
            # calculate the new spacing betwheen buildings
            new_x = (img_w - (spaziatura * 2) - r_sum_w[idx]) // (r_numbers[idx] - 1) - spaziatura
            # apply new spacing
            for i, r in enumerate(row[1:]):
                # new spacing need to be multiplied for the number of the
                # building (incremental)
                r.sw.x += new_x * (i + 1)

    # create a the final image
    layer_final = create_layer((0,0,0), img_w, img_h)

    # draw rettangles
    for row in rect_collection:
        for r in row:
            draw_inner(r, layer_final)

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
    file_dati   = "matrices/mat-16-25.txt"
    file_png    = "test_mat-16-25.png"
    spaziatura  = 25
    print(ex(file_dati, file_png, spaziatura))


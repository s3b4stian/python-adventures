## ESERCIZI

# Scrivere le funzioni seguenti.
# 1. rotL90(img) ritorna una nuova immagine che è l'immagine img ruotata a sinistra di 90 gradi. 
#    Esempio: nel file es1.png vedete come l'immagine img_in_01.png viene ruotata

# 2. red(img, s) ritorna una nuova immagine che è l'immagine img ridotta di un fattore s . Si assume che
#    s sia un intero positvo che divide esattamente sia la larghezza che l'altezza di img . 
#    Per calcolare il colore di un pixel dell'immagine ridotta si usi la tecnica di mosaic_average() . 
#    Ad esempio, red(img, 2) e red(img, 4) , dove img è l'immagine img_in_01.png , 
#    producono le immagini es2_1.png e es2_2.png

# 3. mult(img, s) ritorna una nuova immagine, con le stesse dimensioni di img , che contiene s x s copie
#    ridotte di img . Si assume che s è un intero positvo che divide esattamente sia la larghezza che l'altezza
#    di img . 
#    Esempi, se img è l'immagine img_in_01.png , mult(img, 2) e mult(img, 4) producono, rispettivamente,
#    le immagini dei file es3_1.png ed es3_2.png

# 4. gray(img) ritorna una nuova immagine ottenuta trasformando i colori di img in livelli di grigio. 
#    Ad esempio, se applicata alla solita immagine produce l'immagine es4_1.png

# 5. patchwork(img, s) ritorna un nuova immagine ottenuta dividendo l'immagine img in quadratini di
#    lato s e su ognuno di questi applicando in modo casuale una delle seguenti trasformazioni: 
#    - identità (cioè il quadratino è lasciato invariato), 
#    - invert() , 
#    - contrast() con c = 0.5 , 
#    - contrast() con c = 2.0
#    - e gray() . 
#    Ad esempio, se img è l'immagine img_in_01.png , patchwork(img, 64) e patchwork(img, 16) producono, 
#    rispettivamente immagini simili alle es5_1.png e es5_2.png

# 6. edge(img, t, bg) ritorna una nuova immagine ottenuta dall'immagine img colorando con il colore
#    nero i pixel di confine tra zone di colore significativamente differente. Il parametro t è la soglia minima
#    (un float tra 0.0 e 1.0) della differenza di colore affinché un pixel sia considerato di confine. 
#    Se bg = None , i pixel non di confine sono lasciati con i colori originali, altrimenti sono colorati con il colore bg .

#    Per determinare se un pixel p è di confine si controlla se nell'intorno di p (cioè gli 8 pixel adiacenti per
#    lato o spigolo a p) c'è almeno un pixel la cui distanza normalizzata da p è maggiore o uguale a t ed è più
#    chiaro di p . Come distanza normalizzata si può usare la somma delle differenze assolute delle tre
#    componenti colore diviso per 765 (=3*255). 

#    Esempi, sia img e img2 le immagini img_in_01.png e img_in_02.png , 
#    edge(img, 0.1, None), edge(img, 0,05, None), edge(img2, 0.2, (240,240,240)) ed edge(img2, 0.15, (240,240,240)) 
#    producono rispettivamente le immagini es6_1.png, es6_2.png, es6_3.png, es6_4.png

from lec_12_files_img import image as im

# ex. 1
def rotL90(img: list) ->list:
    w, h = len(img[0]), len(img)
    # new image with inverted height and width
    ret = im.create(h, w, (0,0,0))
    for y in range(h):
        for x in range(w):
            # invert x with y to rotate 90 degrees left
            ret[x][y] = img[y][w - 1 - x]
    return ret

# ex. 2
def red(img: list, s: int) ->list:
    w, h = len(img[0]), len(img)
    ret = im.create(w//s, h//s, (0,255,0))
    # mosaic pixel
    mos = im.mosaic_average(img,s)
    for y in range(h//s):
        for x in range(w//s):
            # copy one s pixels
            ret[y][x] = mos[y*s][x*s]
    return ret

# ex. 3
def mult(img: list, s: int) ->list:
    w, h = len(img[0]), len(img)
    ret = im.create(w, h, (0,255,0))
    # mosaic pixel
    mos = im.mosaic_average(img,s)
    # repeat in y axis
    for yy in range(s):
        for y in range(h//s):
            for x in range(w//s):
                # repeat on x axys
                for xx in range(s):
                    # copy one s pixels
                    ret[y+h//s*yy][x+w//s*xx] = mos[y*s][x*s]
    return ret

# https://docs.gimp.org/2.10/en/gimp-filter-desaturate.html
def gray_luminance(r: int, g: int, b: int) -> tuple:
    # anyone teach me how to implement this
    pass

def gray_luma(r: int, g: int, b: int) -> tuple:
    g = round((0.22 * r) + (0.72 * g) + (0.06 * b))
    return (g, g, g)

def gray_lightness(r: int, g: int, b: int) -> tuple:
    g = round((max(r, g, b) + min(r, g, b)) / 2)
    return (g, g, g)

def gray_average(r: int, g: int, b: int) -> tuple:
    g = round((r + g + b) / 3)
    return (g, g, g)

def gray_value(r: int, g: int, b: int) -> tuple:
    g = max(r, g, b)
    return (g, g, g)

# ex. 4
def gray(img):
    w, h = len(img[0]), len(img)
    ret = im.create(w, h, (0,255,0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = gray_lightness(*img[y][x])
    return ret

def gray_fn(fn, img):
    w, h = len(img[0]), len(img)
    ret = im.create(w, h, (0,255,0))
    for y in range(h):
        for x in range(w):
            ret[y][x] = fn(*img[y][x])
    return ret

# ex. 5
from random import randint

# generic
def contrast(r: int, g: int, b: int, c: float) -> tuple:
    r = ((r - 128) * c) + 128
    g = ((g - 128) * c) + 128
    b = ((b - 128) * c) + 128
    r = round(min(255, max(0, r)))
    g = round(min(255, max(0, g)))
    b = round(min(255, max(0, b)))
    return (r, g, b)

# alias generic to 2.0
def contrast20(r: int, g: int, b: int) -> tuple:
    return contrast(r, g, b, 2)

# alias generic to .5
def contrast05(r: int, g: int, b: int) -> tuple:
    return contrast(r, g, b, 0.5)

def invert(r: int, g: int, b: int) -> tuple:
    return ( 255 - r, 255 - g, 255 - b)

def patchwork(img, s):
    w, h = len(img[0]), len(img)
    ret = im.create(w, h, (0,255,0))

    # list of functions
    # every square select one index
    fn_list = [invert, contrast05, contrast20, gray_average]

    # how many squares in vertical line
    for yy in range(h // s):
        n = yy * s
        # how many squares on horizontal line
        for xx in range(w // s):
            m = xx * s
            fn = fn_list[randint(0, 3)]

            # generate square
            for y in range(n,n + s):
                for x in range(m, m + s):
                    # apply random function to pixel
                    ret[y][x] = fn(*img[y][x])

    return ret

# ex. 6
def check_pixel(p0, p1, t):

    # sum the absolute of difference of every channel
    sum_channels = abs(p0[0] - p1[0]) + abs(p0[1] - p1[1]) + abs(p0[2] - p1[2])

    if sum_channels / 765 >= t and sum(p0) > sum(p1):
        return True

    return False

def is_edge(img, y, x, t):

    # get pixels around
    p       = img[y][x]
    p_N     = img[y - 1][x]
    p_NE    = img[y - 1][x + 1]
    p_NW    = img[y - 1][x - 1]
    p_E     = img[y][x + 1]
    p_W     = img[y][x - 1]
    p_S     = img[y + 1][x]
    p_SW    = img[y + 1][x - 1]
    p_SE    = img[y + 1][x + 1]

    # return the first True due to short
    # circuit
    return check_pixel(p, p_N, t)  or \
           check_pixel(p, p_NE, t) or \
           check_pixel(p, p_NW, t) or \
           check_pixel(p, p_E, t)  or \
           check_pixel(p, p_W, t)  or \
           check_pixel(p, p_S, t)  or \
           check_pixel(p, p_SW, t) or \
           check_pixel(p, p_SE, t)

def edge(img, t, bg):
    w, h = len(img[0]), len(img)
    ret = im.create(w, h, (0,0,0))

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if is_edge(img, y, x, t):
                ret[y][x] = (0, 0, 0)
                continue

            if bg != None:
                ret[y][x] = bg
                continue

            ret[y][x] = img[y][x]
    return ret

# doesn't work in python 3.9
# tested succesfuly using Spyder 4.2.5 and Python 3.8 on windows 10
if __name__ == '__main__':

    # ex 1 test
    img = im.load('lec_12_files_img/img_in_01.png')
    im.visd(img)
    # rotare 90deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 180deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 270deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 360deg left
    img = rotL90(img)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_02.png')
    im.visd(img)
    # rotare 90deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 180deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 270deg left
    img = rotL90(img)
    im.visd(img)
    # rotare 360deg left
    img = rotL90(img)
    im.visd(img)

    # ex 2 test
    img = im.load('lec_12_files_img/img_in_01.png')
    img = red(img, 2)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = red(img, 4)
    im.visd(img)

    # ex 3 test
    img = im.load('lec_12_files_img/img_in_01.png')
    img = mult(img, 2)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = mult(img, 4)
    im.visd(img)

    # ex 4 test
    #img = im.load('lec_12_files_img/img_in_01.png')
    #img = gray_fn(gray_luminance, img)
    #im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = gray_fn(gray_luma, img)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = gray_fn(gray_lightness, img)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = gray_fn(gray_average, img)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = gray_fn(gray_value, img)
    im.visd(img)

    # ex 5 test
    img = im.load('lec_12_files_img/img_in_01.png')
    img = patchwork(img, 64)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = patchwork(img, 16)
    im.visd(img)

    # ex 6 test
    img = im.load('lec_12_files_img/img_in_01.png')
    img = edge(img, 0.1, None)
    im.visd(img)

    img = im.load('lec_12_files_img/img_in_01.png')
    img = edge(img, 0.05, None)
    im.visd(img)

    img2 = im.load('lec_12_files_img/img_in_02.png')
    img2 = edge(img2, 0.2, (240,240,240))
    im.visd(img2)

    img2 = im.load('lec_12_files_img/img_in_02.png')
    img2 = edge(img2, 0.15, (240,240,240))
    im.visd(img2)

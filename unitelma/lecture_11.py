## ESERCIZI
#
#Scrivere le funzioni seguenti.
#
################################################################################
#
#1. size(ll) prende in input una lista di liste ll e ritorna il numero di righe, la lunghezza mimima e
#   massima delle righe e il numero totale di elementi. 
#   Esempio
#>>> size([[1,2,3],['a','b'],[1,2,'A',4,5]]) 
#(3, 2, 5, 10)
#
#
################################################################################
#
#2. draw_h_line(img, x, y, w, c) che disegna sulla immagine img una linea orizzontale che parte dalla coordinata x, y, di lunghezza w e colore c
#   senza sbordare.
#
#   Esempio
#>>> import image as im
#>>> img = im.create(500,150,(0,255,0))
#>>> draw_h_line(img, 100, 50,  300, (255, 0, 0) )
#>>> draw_h_line(img,  50, 100, 700, (0, 0, 255) )
#>>> im.visd(img)
#
#mostra l'immagine del file es2-1.png
#
#
#
################################################################################
#
#3. draw_v_line(img, x, y, h, c) che disegna sulla immagine img una linea verticale che parte dalla coordinata x, y, di altezza w e colore c
#   senza sbordare.
#
#   Esempio
#>>> import image as im
#>>> img = im.create(500,150,(0,0,0))
#>>> draw_v_line(img, 100, 50,  300, (255, 0, 0) )
#>>> draw_v_line(img,  50, 100, 700, (0, 0, 255) )
#>>> im.visd(img)
#
#mostra una immagine uguale al file es3-1.png
#
#
#
################################################################################
#
#4. draw_quad_out(img, x1, y1, x2, y2, c) disegna sull'immagine img il contorno di un rettangolo di
#   colore c che ha lo spigolo in alto a sinistra in (x1, y1) e quello in basso a destra in (x2, y2) . 
#   Esempi
#>>> import image as im
#>>> img = im.create(300,150,(0,0,0))
#>>> draw_quad_out(img,  50,  20, 100,140,(255,128,0))
#>>> im.visd(img)
#>>> draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
#>>> im.visd(img)
#>>> draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
#>>> im.visd(img)
#
#mostra immagini uguali a quelle allegate es4-1.png, es4-2.png, es4-3.png
#
#
#
#################################################################################
#
#5. draw_grid(img, s, c) disegna sull'immagine img una griglia di linee orizzontali e verticali di colore c
#   separate da s pixels le une dalle altre. Questo significa che se s è zero, le linee sono adiacenti. 
#   Esempi
#>>> img = im.create(200, 100, (200,200,200))
#>>> draw_grid(img, 2, (0,0,0))
#>>> im.visd(img)
#
#mostra una immagine uguale al file es5-1.png
#
#>>> img = im.create(400, 200, (240,240,240))
#>>> for k in range(6):
#...     s = int(8*(1.5**k))
#...     c = 200 - 40*k
#...     draw_grid(img, s, (c, c, c))
#>>> im.visd(img)
#
#mostra una immagine uguale al file es5-2.png
#
#
################################################################################


# ex. 1
def size(ll: list) -> tuple:
    # tmp list comprehension to obtain a list
    # whith the lengths of the inner lists
    ll_len = [len(x) for x in ll]
    # return a tuple of
    #   - the number of rows
    #   - the min of all lengths of the inner lists
    #   - the max of all lengths of the inner lists
    #   - the sum of all lengths of the inner lists
    return  len(ll), min(ll_len), max(ll_len), sum(ll_len)

# ex. 2
def draw_h_line(img, x, y, w, c):
    pass

# ex. 3
def draw_v_line(img, x, y, h, c):
    pass

# ex. 4
def draw_quad_out(img, x1, y1, x2, y2, c):
    pass

# ex. 5
def draw_grid(img, s, c):
    pass


if __name__ == '__main__':

    # ex 1 test
    print(size([[1,2,3],['a','b'],[1,2,'A',4,5]])) # print (3, 2, 5, 10)

    # ex 2 test
    from files_img import image as im
    img = im.create(500,150,(0,255,0))
    draw_h_line(img, 100, 50,  300, (255, 0, 0) )
    draw_h_line(img,  50, 100, 700, (0, 0, 255) )
    im.visd(img)

    # ex 3 test
    img = im.create(500,150,(0,0,0))
    draw_v_line(img, 100, 50,  300, (255, 0, 0) )
    draw_v_line(img,  50, 100, 700, (0, 0, 255) )
    im.visd(img)

    # ex 4 test
    img = im.create(300,150,(0,0,0))
    draw_quad_out(img,  50,  20, 100,140,(255,128,0))
    im.visd(img)
    draw_quad_out(img, 120, -10, 180, 70, (255,255,255))
    im.visd(img)
    draw_quad_out(img, 140,  40, 320, 120, (80,80,255))
    im.visd(img)

    # ex 5 test
    img = im.create(200, 100, (200,200,200))
    draw_grid(img, 2, (0,0,0))
    im.visd(img) # show an image equal to es5-1.png

    img = im.create(400, 200, (240,240,240))
    for k in range(6):
        s = int(8*(1.5**k))
        c = 200 - 40*k
        draw_grid(img, s, (c, c, c))
    im.visd(img) # show an image equal to es5-2.png
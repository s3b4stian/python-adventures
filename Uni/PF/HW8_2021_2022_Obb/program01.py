# -*- coding: utf-8 -*-
'''
Un pixel artist di fama mondiale di nome Fred Zuppa ha recentemente
prodotto diversi capolavori sottoforma di immagini quadrate raster
codificate su pixels in scala di grigi. Le immagini che ha disegnato
possono prendere valori da 0 a 255 compresi. Sfortunatamente le famose
opere sono andate perdute in quanto il suo disco rigido (ahilui!) ha
smesso di funzionare e ovviamente il buon Fred e' disperato. I
programmi per recuperarle dal filesystem non funzionano purtroppo e
cosi' Fred si affida al suo amico informatico di fiducia, il quale gli
dice:

   "Fratello, in verita' ti dico, se ti ricordi la dimensione delle
   immagini e i valori dei pixel di cui erano formate e delle
   proprieta' particolari delle tue opere, allora possiamo provare a
   scrivere un generatore ricorsivo che le produca tutte in base ai
   tuoi input, cosi' facendo possiamo provare a recuperarle!"

Il mattino seguente Fred riesce a dare le informazioni necessarie
sottoforma di:
   1. `D` parametro intero che descrive la dimensione dell'immagine
       quadrata.
   2. `colors` una lista di interi che descrive i colori delle
      immagini di Fred.  I colori di Fred sono compresi fra 0, 255.
      colors puo' essere quindi [128, 0, 255] mentre NON puo' essere
      [-100, 999]
   3. Un testo `img_properties` che descrive le proprieta' delle sue
      immagini: Il testo puo' descrivere nessuna proprita' (stringa
      vuota) oppure puo' descrivere una proprieta' che riguarda i
      pattern che le immagini devono contenere.

       Ad esempio:

       Se `img_properties` e' vuota allora le immagini non devono soddisfare
       nessuna proprieta'. Viceversa se `img_properties` e' uguale a
       'pattern_{type}_' allora signifca che le immagini devono
       mostrare il pattern di tipo `type` specificato nella stringa.
       Il pattern puo' essere di un solo tipo.

       I tipi di pattern possibili sono i quattro seguenti:
          a) 'pattern_diff_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve avere i
          pixel di colore tutti diversi.

                 valid        not valid
            |  96 | 255 |   |   0 | 255 |
            | 128 |   0 |   | 255 |  96 |


          b) 'pattern_cross_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve
          avere i pixel sulla diagonale uguali fra loro e i pixel
          sulla antidiagonale uguale fra loro ma pixel delle due
          diagonali devono essere diverse.

               valid          not valid     not valid
            |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
            | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

          c) 'pattern_hrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle righe tutti uguali ma righe adiacenti di colore
          diverso.

                 valid       not valid        not valid
            |   0 |   0 |   | 255 | 255 |    | 43 | 43 |
            | 128 | 128 |   | 0   | 255 |    | 43 | 43 |

          d) 'pattern_vrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle colonne tutti uguali ma colonne adiacenti di colore
          diverso.

                valid         not  valid    not valid
             | 0 | 255 |     | 0  | 0  |    | 22 | 22 |
             | 0 | 255 |     | 0  | 255|    | 22 | 22 |

Implementare la funzione ricorsiva o che usa metodi ricorsivi:
  
      images = ex(colors, D, img_properties)

che prende in ingresso la lista di colori `colors`, la dimensione
delle immagini `D` e una stringa `img_properties` che ne descrive le
proprieta' e generi ricorsivamente tutte le immagini seguendo le
proprieta' suddette.  La funzione deve restituire l'elenco di tutte le
immagini come una lista di immagini.  Ciascuna immagine e' una tupla di
tuple dove ogni intensita' di grigio e' un intero.
L'ordine in cui si generano le immagini non conta.

     Esempio: immagine 2x2 di zeri (tutto nero) e':
        img = ( (0, 0), (0, 0), )


Il timeout per ciascun test è di 1 secondo.

***
E' fortemente consigliato di modellare il problema come un albero di
gioco, cercando di propagare le solo le "mosse" necessarie nella
ricorsione e quindi nella costruzione della soluzione in maniera
efficiente; oppure, in maniera alternativa, cercate di "potare" l'albero di
gioco il prima possibile.
***

Potete visualizzare tutte le immagini da generare invocando

     python test_01.py data/images_data_15.json

questo salva su disco tutte le immagini attese del test 15 e crea
un file HTML di nome `images_data_15.html` nella directory radice
del HW con cui e' possibile vedere le immagini aprendo il file html
con browser web.
'''

def create_matrix(x: int, y: int)->list:
    """
    Create a void layer filled with -1, not a valid color

    Parameters
    ----------
    x : int
        Columns of the matrix.
    y : int
        Rows of the matrix.

    Returns
    -------
    list
        The matrix filled with -1.

    """

    return [[-1] * x for _ in range(y)]


def gen_matrix(
        colors: list,
        moves: list,
        matrix: list,
        m_d: int,
        images: list,
        level: int
    )->None:
    """
    Calculete all possible combination of matrix using pixel by pixel strategy.

    Parameters
    ----------
    colors : list
        Colors list used to build the image/matrix.
    moves : list
        All positions into the image/matrix.
    matrix : list
        Matrix skeleton to populate using the pixel/colors.
    m_d : int
        Matrix dimension, also the max recurion depth.
    images : list
        List to append a complete image/matrix.
    level : int
        Current recursion level.

    Returns
    -------
    None.

    """

    # current cell/position into the matrix
    y, x = moves[level]

    for c in colors:
        # assign the color to current cell
        matrix[y][x] = c

        # if the level of recurions in equal to the matrix dimension
        # then the matrix is filled and it is possible to add it to the
        # list of images
        if level == m_d:
            images.append((tuple([tuple(x) for x in matrix])))
            continue

        # recursive call to add the next pixel to the matrix
        gen_matrix(colors,
                   moves,
                   matrix,
                   m_d,
                   images,
                   level + 1)


def filter_diff(colors: set, m: list, x: int, y: int)->set:
    """
    Checks which colors match the pattern for the next moves.

    It indicates that by taking arbitrarily a subimage of equal to 2x2 in 
    Fred's images, this subimage must have pixels on the diagonal all equal
    and the pixels on the anti-diagonal all equal but the two diagonals must 
    be different in colors.

        valid         not valid     not valid
    |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
    | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

    Parameters
    ----------
    colors : set
        All colors to build the image.
    m : list
        Matrix to check.
    x : int
        x position of the evaluated pixel.
    y : int
        y position of the evaluated pixel.

    Returns
    -------
    set
        Compatible colors with current pattern for the next moves.

    """

    if y:
        if not x:
            # return all colors except color at n and ne
            return colors ^ {m[y-1][x], m[y-1][x+1]}

        if x:
            s_c = {
                m[y-1][x-1],    # color at nw
                m[y][x-1],      # color at w
                m[y-1][x]       # color at n
            }

            if x < len(m) - 1:
                # color at ne
                s_c.add(m[y-1][x+1])

            return colors ^ s_c

    if x:
        # return all colors except color at w
        return colors ^ {m[y][x-1]}

    return colors


def filter_cross(colors: set, m: list, x: int, y: int):
    """
    Checks which colors match the pattern for the next moves.

    It indicates that by taking arbitrarily a subimage of equal to 2x2 in 
    Fred's images, this subimage must have pixels on the diagonal all equal
    and the pixels on the anti-diagonal all equal but the two diagonals must 
    be different in colors.

        valid         not valid     not valid
    |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
    | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

    Parameters
    ----------
    colors : set
        All colors to build the image.
    m : list
        Matrix to check.
    x : int
        x position of the evaluated pixel.
    y : int
        y position of the evaluated pixel.

    Returns
    -------
    set
        Compatible colors with current pattern for the next moves.

    """

    if y:
        if not x:
            # return the color at ne
            return {m[y-1][x+1]}
        if x:
            # return the color at nw
            return {m[y-1][x-1]}

    if x > 1:
         # return the color at w -1
         return {m[y][x-2]}

    if x:
        # return all colors except color at w
        return colors ^ {m[y][x-1]}

    return colors


def filter_hrect(colors: set, m: list, x: int, y: int):
    """
    Checks which colors match the pattern for the next moves.

    If present, this indicates that by taking arbitrarily a subimage of 
    dimension equal to 2x2 in Fred's images, this subimage must have the 
    pixels on the rows all equal but adjacent rows of different colors.

        valid         not valid       not valid
    |   0 |   0 |   | 255 | 255 |    | 43 | 43 |
    | 128 | 128 |   | 0   | 255 |    | 43 | 43 |

    Parameters
    ----------
    colors : set
        All colors to build the image.
    m : list
        Matrix to check.
    x : int
        x position of the evaluated pixel.
    y : int
        y position of the evaluated pixel.

    Returns
    -------
    set
        Compatible colors with current pattern for the next moves.

    """

    if y:
        if not x:
            # return all colors except color at n
            return colors ^ {m[y-1][x]}
        if x:
            # return the color at w
            return {m[y][x-1]}

    if x:
        # return the color at w
        return {m[y][x-1]}

    return colors


def filter_vrect(colors: set, m: list, x: int, y: int):
    """
    Checks which colors match the pattern for the next moves.

    If present, this indicates that by taking arbitrarily a subimage of
    dimension equal to 2x2 in Fred's images, this subimage must have the
    pixels on the columns all equal but adjacent columns with different colors.

       valid         not  valid     not valid
    | 0 | 255 |     | 0  | 0  |    | 22 | 22 |
    | 0 | 255 |     | 0  | 255|    | 22 | 22 |

    Parameters
    ----------
    colors : set
        All colors to build the image.
    m : list
        Matrix to check.
    x : int
        x position of the evaluated pixel.
    y : int
        y position of the evaluated pixel.

    Returns
    -------
    set
        Compatible colors with current pattern for the next moves.

    """

    if y:
        # return the color at n
        return {m[y-1][x]}

    if x:
        # return all colors except color at w
        return colors ^ {m[y][x-1]}

    return colors


def gen_matrix_pattern(
        colors: set,
        moves: list,
        matrix: list,
        m_d: int,
        images: list,
        level: int, 
        p_filter
    )->None:
    """
    Calculete all possible combination of matrix using pixel by pixel strategy.

    Parameters
    ----------
    colors : set
        All colors used to build the image/matrix.
    moves : list
        All positions into the image/matrix.
    matrix : list
        Matrix skeleton to populate using the pixel/colors.
    m_d : int
        Matrix dimension, also the max recurion depth.
    images : list
        List to append a complete image/matrix.
    level : int
        Current recursion level.
    p_filter : callable
        Function used to obtain the whished pattern into the image.

    Returns
    -------
    None.

    """

    y, x = moves[level]

    filtered_colors = p_filter(colors, matrix, x, y)

    for c in filtered_colors:

        # print(level,"|--" * level, c, y, x, matrix)

        matrix[y][x] = c

        # print(level,"|-+" * level, c, y, x, matrix)

        if level == m_d:
            # print(level,"|-=" * level, c, y, x, matrix)
            images.append((tuple([tuple(x) for x in matrix])))
            # print()
            continue

        gen_matrix_pattern(colors,
                   moves,
                   matrix,
                   m_d,
                   images,
                   level + 1,
                   p_filter)


def ex(colors, D, img_properties):

    # all positions inside the matrix
    moves = [tuple([y,x]) for y in range(D) for x in range(D)]

    images = []

    call = {
        'pattern_diff_':filter_diff,
        'pattern_cross_':filter_cross,
        'pattern_hrect_':filter_hrect,
        'pattern_vrect_':filter_vrect
    }

    if img_properties:
        gen_matrix_pattern(
                set(colors),
                moves,
                create_matrix(D, D),
                D*D - 1,
                images,
                0,
                call[img_properties])
    else:
        gen_matrix(
            colors,
            moves,
            create_matrix(D, D),
            D*D - 1,
            images,
            0)

    return images

## tests
#  1 {"colors": [0],                         "D": 1,  "img_properties": ""}
#  2 {"colors": [0, 255],                    "D": 1,  "img_properties": ""}
#  3 {"colors": [0, 255],                    "D": 2,  "img_properties": ""}
#  4 {"colors": [127, 196],                  "D": 3,  "img_properties": ""}
#  5 {"colors": [0, 128, 196, 255],          "D": 2,  "img_properties": "pattern_diff_"}
#  6 {"colors": [0, 128, 196, 255],          "D": 3,  "img_properties": "pattern_diff_"}
#  7 {"colors": [0, 96, 128, 255],           "D": 6,  "img_properties": "pattern_diff_"}
#  8 {"colors": [0, 128, 196, 255],          "D": 7,  "img_properties": "pattern_diff_"}
#  9 {"colors": [0, 128, 196, 255],          "D": 7,  "img_properties": "pattern_cross_"}
# 10 {"colors": [0, 255],                    "D": 16, "img_properties": "pattern_cross_"}
# 11 {"colors": [0, 128, 196, 255],          "D": 4,  "img_properties": "pattern_cross_"}
# 12 {"colors": [0, 128, 196, 255],          "D": 4,  "img_properties": "pattern_hrect_"}
# 13 {"colors": [0, 128, 196, 255],          "D": 2,  "img_properties": "pattern_diff_"}
# 14 {"colors": [0, 255],                    "D": 2,  "img_properties": "pattern_cross_"}
# 15 {"colors": [0, 96, 200, 255],           "D": 4,  "img_properties": "pattern_vrect_"}
# 16 {"colors": [0, 96, 128, 200, 228, 255], "D": 4,  "img_properties": "pattern_vrect_"}
# 17 {"colors": [0, 96, 128, 228, 255],      "D": 3,  "img_properties": "pattern_diff_"}

if __name__ == '__main__':
    colors = [0, 128, 196, 255]
    D = 7
    img_properties = "pattern_diff_"

    ex(colors, D, img_properties)

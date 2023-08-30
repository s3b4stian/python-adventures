# -*- coding: utf-8 -*-
'''
Anche nella poesia, così come nella musica, esiste la nozione di ritmo.
In musica, il ritmo è quella proprietà della canzone che stai ascoltando che ti fa
battere il piede o le mani a tempo, o ti guida mentre stai ballando.
Analogamente, anche le poesie o i poemi non scritti in versi liberi hanno un ritmo, determinato
dalle sillabe che compongono le parole dei loro versi.
Alcune poesie o poemi poi hanno un ritmo sempre uguale in ogni riga, mentre altri hanno un ritmo
che cambia leggermente tra una riga e la successiva.
Vorremmo quindi provare a stimare quanto una poeasia o poema è regolare o irregolare in termini di ritmo
contenuto nei versi. Un ritmo regolare significa che le varie righe della poesia o poema
hanno tutte esattamente lo stesso ritmo, diremo quindi che sono in sync.
Al contrario, un ritmo irregolare varie ad ogni riga, diremo quindi in quel caso che le
righe della poesia o poema sono out of sync.

Ogni parola in qualunque lingua è composta di sillabe che vengono pronunciate usando l'intonazione della
voce per dare loro un accento più o meno forte. Ad esempio, in italiano la parola "casa" ha un accento
sulla prima sillaba. Esiste un modo per specificare questo, si chiama trascrizione fonetica
di una parola: nell'esempio, la trascrizione fonetica di casa è kˈaza, dove l'apostrofo
indica che sulla prima sillaba (ka) c'è un accento primario.

Vogliamo scrivere un programma che, dato un file di testo con encoding 'utf-8'
contenente i versi di una poesia o poema divisi in un certo numero di righe 
(possono esserci anche righe vuote, che ignoreremo),
trovi gli accenti di ogni parola e quindi di tutta la poesia, mantenendo però la suddivisione
del testo per righe, com'era nel testo originale.
Per farlo, sfrutteremo due funzioni, "phones_for_word" e "stresses", del modulo "pronouncing"
(https://pronouncing.readthedocs.io/en/latest/).
Data quindi una riga (non vuota) della poesia, chiameremo la funzione phones_for_word su ogni parola,
ottenendo da essa la traduzione fonetica della parola (casa -> k'asa).
La funzione potrebbe restituire più di una traduzione fonetica per la stessa parola nel
caso di parole che possono essere pronunciate in diversi modi, in quel caso considereremo
solo la prima traduzione fonetica restituita.
A quel punto, chiameremo la funzione stresses che, data in input la traduzione phonetica
della parola, ci restituirà una stringa di accenti, in cui: 0=nessun accento, 1=accento primario,
2=accento secondario. Per il nostro scopo, considereremo solo gli accenti primari, quindi
tralasceremo i secondari considerandoli come assenza di accento (come se fossero degli zeri).
Inoltre, nel tradurre frasi intere in accenti, aggiungeremo uno zero tra ogni coppia di parole
(vedi anche Nota 2 sotto).

Nota 1: nel tradurre parole in fonemi, la funzione phones_for_word potrebbe restituire
una lista vuota (perché la parola è sconosciuta); in quel caso considereremo come accenti
corrispondenti alla parola una sequenza di zeri pari alla lunghezza della parola divisa
per due (parte intera del risultato); ad esempio, siccome "pierc" non ha traduzione
fonetica, considereremo come stringa di accenti "00"

Nota 2: per semplificare, ci sarà sempre uno zero extra dopo l'ultima parola di ogni riga

Ad esempio, dalla seguente riga di testo: "IN the midway of this our mortal life,"
otterremo la lista di accenti: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
Perché:
IN -> ['IH0 N', 'IH1 N'] -> 0
spazio -> 0
the -> ['DH AH0', 'DH AH1', 'DH IY0'] -> 0
spazio -> 0
midaway - > ['M IH1 D W EY2'] -> 1,0
spazio -> 0
of -> ['AH1 V'] -> 1
spazio -> 0
this -> ['DH IH1 S', 'DH IH0 S'] -> 1
spazio -> 0
our -> ['AW1 ER0', 'AW1 R', 'AA1 R'] -> 1,0
spazio -> 0
mortal -> ['M AO1 R T AH0 L'] -> 1,0
spazio -> 0
life -> ['L AY1 F'] -> 1
spazio -> 0

Una volta tradotta tutta la poesia in sequenze di zeri e uni, avremo una lista di liste
di varie lunghezze, ad esempio:

IN the midway of this our mortal life,
I found me in a gloomy wood, astray
Gone from the path direct: and e'en to tell
It were no easy task, how savage wild
That forest, how robust and rough its growth,
Which to remember only, my dismay
Renews, in bitterness not far from death.

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
]

Vogliamo trasformare questa lista di liste in una matrice di accenti,
aggiungendo un opportuno numero di zeri alla fine delle righe
eventualmente più corte della riga più lunga:

[
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
]

A questo punto calcoliamo la sincronizzazione tra le tutte le coppie di righe
della matrice. Date due liste A e B, ciascuna di N valori 0 o 1, e un valore tau
compreso tra zero e N, definiamo l'indice di sincronizzazione tra A e B come:

       0.5 * (c(B|A) + c(A|B))
Sync = -----------------------
          sqrt(m(A)*m(B))

Dove:
    - c(B|A) è il numero di volte in cui un accento di B è preceduto da un accento di A 
      a una distanza <= tau
    - c(A|B) è il numero di volte in cui un accento di A è preceduto da un accento di A 
      a una distanza <= tau
    - m(A) è il numero di accenti in A
    - m(B) è il numero di accenti in B

e dove, ricordiamo, un valore di 1 in A o B rappresenta un accento.

NOTA: se m(A) == 0 o m(B) == 0 assumiamo come valore di Sync zero

Ad esempio, date le due sequenze:
    - A = [0, 0, 0, 0, 1, 0, 0, 1]
    - B = [1, 0, 1, 0, 1, 0, 0, 0]
    - tau = 3

avremo:
    - c(B|A) = 1, perché solo il terzo accento in B (posizione 4) è preceduto in A da un
      accento a una distanza inferiore o uguale a 3 (in questo caso l'1 in A coincide come
      posizione con l'1 in B)
    - c(A|B) = 2, perché entrambi gli accenti di A sono preceduti in B da due accenti entro
      3 posizioni
    - m(A) = 2
    - m(B) = 3
    - Sync = 0.5 * (1 + 2) / sqrt(2 * 3) = 0.6123724356957946

Data una poesia o poema in input, definiamo l'indice di sincronizzazione del testo come
la media tra i valori di Sync tra tutte le coppie di righe  di accenti (A1, A2)
dove A1 e A2 non sono la stessa lista
NOTA: due liste diverse possono comunque contenere gli stessi valori

Scrivere la funzione PoemSync che, dati in input:
- il path di un file di testo contenente una poesia
- il path del file di output in cui salvare la matrice di accenti
- il valore (intero) di tau

svolga le seguenti operazioni:
- apra il file della poesia e calcoli la matrice degli accenti
- salvi la matrice degli accenti nel file il cui path è specificato in input, nel formato specificato
- calcoli e ritorni l'indice di sincronizzazione del testo, arrotondato
  alla sesta cifra decimale (es: 0.6123724356957946 -> 0.612372)

nota: tornando alla matrice degli accenti riportata sopra, il file generato
da PoemSync conterrà:

000010010101001001000
101010000010010010000
101000100100010101010
101010100101010010000
101001001000101010000
101001001001001000000
010001000101010100000


ESEMPIO DI ESECUZIONE:

PoemSync("example.txt", "example.out.txt", 2)

contenuto di example.txt:
No one can tell me
Where the wind comes from
Where the wind comes from

no one can tell me
['no', 'one', 'can', 'tell', 'me']
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
where the wind comes from
['where', 'the', 'wind', 'comes', 'from']
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]

matrix:
1010101010
1000101010
1000101010

sync tra a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync tra a=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (5, 5)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (5, 5) (c(a|b), m(a)) = (4, 4)
sync = 1.0062305898749053

sync tra a=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0] e
         b=[1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
(c(b|a), m(b)) = (4, 4) (c(a|b), m(a)) = (4, 4)
sync = 1.0

PoemSync = 1.004154

TIMEOUT: 0.5s

'''

import pronouncing
import math


def combinations(n: int) -> list:
    """
    https://en.wikipedia.org/wiki/Combination
    k is always 2
    code recycled from HW2 :)

    Parameters
    ----------
    n : int
        number of rows.

    Returns
    -------
    list
        a list of tuples with all combinations of players.

    """

    n -= 1
    i = 0
    j = 1
    lst = []
    while i < n:
        lst += [(i, j)]
        j += 1

        if j > n:
            i += 1
            j = i + 1

    return lst


def calculate_sync(rw_p: list, mm: list, t: int) ->float:
    """
    calculate the sync of all pairs of rows

    Parameters
    ----------
    rw_p : list
        list of tuples with rows combination.
    mm : list
        a matrix containing positions of the accents.
    t : int
        tau.

    Returns
    -------
    float
        sync value.

    """

    # initialize sync
    sync = 0.0

    # for every row pair
    for idx_a, idx_b in rw_p:

        # get the number of 1 for rows
        m_a = len(mm[idx_a])
        m_b = len(mm[idx_b])

        # precalculate 
        mul_ab = m_a * m_b
        
        # continue if m_a or m_b is zero
        if not mul_ab:
             continue

        # calculate the sum of c(B|A) and c(A|B)
        count = C(mm[idx_b], mm[idx_a], t) + C(mm[idx_a], mm[idx_b], t)

        # calculate sync removing 0,5 mul to avoid to repeat the formula
        # two times
        sync += (count) / math.sqrt(mul_ab)

    return sync


def C(lst_a: list, lst_b: list, tau: int) ->int:
    """
    calculate the c(B|A) or the c(A|B)

    Parameters
    ----------
    lst_a : list
        list of positions of accents.
    lst_b : list
        list of positions of accents.
    tau : int
        tau.

    Returns
    -------
    int
        the number of accents preceded.

    """

    c = 0
    # compare positions of every accent in list a with every accent in list b
    for a in lst_a:
        for b in lst_b:
            # if the difference between the position a and b is less than or
            # equal to tau and greather than or equal to zero then
            # there is the accent to count
            if 0 <= a - b <= tau:
                c += 1
                break

    # reduce the Cyclomatic Complexity to 3 but is 3x slower
    # c = 0
    # for a in lst_a:
    #     c += 1 if tuple(filter(lambda b: 0 <= a - b <= tau, lst_b)) else 0

    return c


def calculate_stress(cl: str) ->list:
    """
    returns the stress list for a row.
    the stress list for the example.txt:
    no one can tell me 
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    where the wind comes from 
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    where the wind comes from 
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0]

    Parameters
    ----------
    cl : str
        a line of text (phrase) containing only letters and spaces.

    Returns
    -------
    list
        a list of accents for the line.

    """

    # declare needed vars
    stress_list = []

    # for every line of the text
    # line here is already clened from special chars
    for w in cl.split():

        # calculate the pronounce
        phones_list = pronouncing.phones_for_word(w)

        # if there is a pronounce for the word
        if phones_list:
            # calculate the accentes for the word
            stress_list += list(map(int, pronouncing.stresses(phones_list[0])))
        else:
            # add zeroes if there isn't any accent
            stress_list += [0] * math.floor(len(w) / 2)

        stress_list += [0]

    return stress_list


def create_matrix(inputfilename: str) ->tuple:
    """
    create a matrix of accent positions from the input file.

    considering the stress matrix of the file example.txt:
    1010101010
    1000101010
    1000101010
    this function calculate this matrix
    [
      (0, 2, 4, 6, 8),
      (0, 4, 6, 8), 
      (0, 4, 6, 8)
    ]
    every number into the matrix is the position of a 1 

    Parameters
    ----------
    inputfilename : str
        file to analyze.

    Returns
    -------
    tuple
        containing a list with the length of the stresses and a
        list of tuples where every tuple contains the position of accents.

    """

    # nested function used only internally
    # returns a row without special chars
    # only letters and spaces
    def remove_secial_chars(l: str) -> str:
        return ''.join([c if c.isalpha() else ' ' for c in l])

    # nested function used only internally
    # returns a tuple containing the indexs of every 1 into the
    # input list
    def extract_indexes(lst: list) -> tuple:
        return tuple([x for x, y in enumerate(stress_list) if y == 1])

    # open the file and read whole contet as list of lines
    with open(inputfilename, encoding='utf-8') as f:
         lines = f.readlines()

    # declare needed vars
    matrix = []
    line_max = set()

    # for every line
    for l in lines:
        # remove special chars
        l_clen = remove_secial_chars(l)
        # calculate the stress list
        stress_list = calculate_stress(l_clen)

        # if the list isn't void
        if stress_list:
            # append the lenght of the list of future use
            line_max.add(len(stress_list))
            # append the indexes of 1 to the matrix
            matrix.append(extract_indexes(stress_list))

    return line_max, matrix


def write_file(outputfilename: str, mm: list, max_row_len):
    """
    write the output file

    Parameters
    ----------
    outputfilename : str
        filename for the file to write the output.
    mm : list
        a matrix containing positions of the accents.
    max_row_len : TYPE
        a list with the length of the stresses.

    Returns
    -------
    None.

    """

    # get the max length of the rows of the matrix
    max_row_len = max(max_row_len)

    with open(outputfilename, encoding='utf-8', mode='w') as fo:
        # create line by line a void list of zeroes
        # then insert a correct value where needed
        # zero line, len == max_row_len
        # 0000000000 -> (0, 2, 4, 6, 8) = 1010101010
        # 0000000000 -> (0, 4, 6, 8)    = 1000101010
        # 0000000000 -> (0, 4, 6, 8)    = 1000101010

        # for every row in the matrix
        for row in mm:
            # generate a void content
            test = ['0'] * max_row_len
            # append the value one when needed
            for col in row:
                test[col] = '1'
            # write to file
            fo.write(''.join(test))
            fo.write('\n')


def PoemSync(inputfilename, outputfilename, tau):

    # create a matrix with positions of accents
    l_max, mc = create_matrix(inputfilename)

    # write final matrix to file and return it
    # to calculate the sync
    write_file(outputfilename, mc, l_max)

    # caluculate row pairs
    row_pairs = combinations(len(mc))

    # calculate sync
    sync = calculate_sync(row_pairs, mc, tau)

    return round(sync / (len(row_pairs) * 2), 6)

# ID,       tau,  expectedsync, timeout
# ( '02',      2,   0.915513,     0.5 ),
# ( '06',      2,   0.546026,     0.5 ),
# ( '01',      2,   0.886818,     0.5 ),
# ( '08',     15,   0.156752,     0.5 ),
# ( '05',      2,   0.796107,     0.5 ),
# ( '07',      2,   0.864993,     0.5 ),
# ( '03',      2,   0.84305 ,     0.5 ),
# ( '09',     10,   0.011507,     14  ),
# ( '04',      2,   0.846562,     15  ),
# ( '04.200',  7,   0.960865,      1  )

if __name__ == "__main__":
    # local test
    inputfilename = "poems/text04.200.txt"
    outputfilename = "test04.200.out.txt"
    tau = 2
    PoemSync(inputfilename, outputfilename, tau)

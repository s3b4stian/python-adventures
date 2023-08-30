# -*- coding: utf-8 -*-
'''
In un file di testo e' riportata una sequenza binaria S. Siamo interessati
    alla  frequenza delle sottosequenze di S(la frequenza di una sottosequenza
    di S e'  il numero di volte che la sottosequenza occorre in S). Si consideri
    ad esempio il file di testo f1.txt contenente la sequenza

    01010010010001000111101100001010011001111000010010011110010000000

    la sottosequenza '00' ha frequenza 23 mentre la sottosequenza '1000' ha
    frequenza 5. Notare che la sottosequenza e' separata su tre righe nel file.

Dati gli interi a e b, con a<=b, siamo interessati a contare le frequenze delle
    sottosequenze si S che presentano una lunghezza tra a e b. Dato l'intero
    n vogliamo listare le al piu' n frequenze massime ciascuna con le
    corrispondenti sottosequenze. Nel caso ci siano meno di n distinte
    frequenze con lunghezza tra a e b, l'output avra' meno di n elementi.

Progettare la funzione ex1(ftesto, a, b, n) che prende come parametri:
    - ftesto: l'indirizzo del file di testo in cui e' registrata la sequenza
      binaria in una o piu' righe consecutive;
    - a,b: i due interi a e b con a<=b che indicano l'intervallo delle
      lunghezze delle sottosequenze  di cui contare le frequenze;
    - n: l'intero che indica il numero di frequenze massime cui siamo
      interessati;
e restituisce una lista di tuple.

Ciascuna tupla della lista ha come prima coordinata una frequenza e come
    seconda coordinata la lista delle sottosequenze che hanno quella frequenza.
    La lista deve contenere solo le tuple con le prime n frequenze massime e, in
    caso ci siano meno di n frequenze distinte, conterra' tutte le tuple con
    frequenze distinte. La lista e' ordinata in ordine lessicografico rispetto
    alla prima coordinata delle tuple e in ciascuna tupla la lista presente
    nella seconda coordinata e' ordinata lessicograficamente.

Ad esempio, ex1('ft1.txt', 2, 4, 20) restituisce la lista:
    [ (4, ['0001', '0011', '1100' ]),
      (5, ['011', 1000', '110' ]),
      (6, ['0000', '111']),
      (7, ['0010','1001' ]),
      (8, ['0100']),
      (10,['010']),
      (11,['000', '001', '11']),
      (12,['100']),
      (15,['01','10']),
      (23,['00'])
    ]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando caricate il file, assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder).

'''

def build_result(occ: dict, n: int) -> list:

    # reverse keys with values in dict
    d = {}
    for k, v in occ.items():
        if v in d:
            d[v].append(k)
        else:
            d[v] = [k]
    # return the first n elemtes of sorted list
    return sorted([ (x, sorted(y)) for x,y in list(d.items())])[-n:]

    # same thing but using list comprehension
    # faster than normal for
    #return sorted([(v, sorted([x for x, y in occ.items() if y == v])) for v in set(occ.values())])[-n:]

def ex1(ftesto, a, b, n):

    # open file and read whole content
    with open(ftesto, encoding='utf-8') as f:
        stream = f.read().replace("\n","")

    # take the lenght of the stream
    s_len = len(stream)

    # declare a void dictionary
    occurrences = {}

    # reversed for, iterate only one time on the stream
    i = 0
    while i < s_len:
        for c_len in range(a, b + 1):

            # exit strategy
            if i + c_len > s_len:
                break

            # get the current sequence
            tmp = stream[i:i + c_len]

            # count the occurrence
            if tmp in occurrences:
                occurrences[tmp] += 1
            else:
                occurrences[tmp] = 1

        i += 1

    return build_result(occurrences, n)

if __name__ == '__main__':
    expected = [
        [1032, ["1011"]], 
        [1062, ["1110"]], 
        [1063, ["0111"]], 
        [1409, ["101"]],
        [1438, ["011", "110"]],
        [1964, ["01", "10"]], 
        [2043, ["11111"]],
        [2813, ["1111"]],
        [3876, ["111"]], 
        [5315, ["11"]]
    ]

    filename = "ft2.txt"
    da = 2
    a = 5
    n = 10

    #filename = "ft9600.txt"
    #da = 23
    #a = 69
    #n = 22

    ex1(filename, da, a, n)
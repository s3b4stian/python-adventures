# -*- coding: utf-8 -*-
'''
    Abbiamo una sequenza di N interi con N dispari. Sottoponiamo la sequenza alla seguente
    procedura che portera' all'eventuale cancellazione di elementi della sequenza:
    - Finche' nella sequenza sono presenti numeri uguali:
       - si selezionano nella sequenzai due numeri uguali ed li si eliminano ricompattando i numeri rimanenti.

    Data la sequenza di interi noi siamo interessati a trovare tutte le
    sequenze finali che e' possibile ottenere applicando la procedura descritta fintanto che è applicabile.
    Nota che tutte queste sequenze sono composte da uno stesso numero positivo di interi distinti.

    Si consideri ad esempio l'albero delle sequenze  che si ottiene a partire dalla
    1 2 0 1 0 0 1  e che e' riportato nel file game_tree.pdf
    Le foglie dell'albero sono le sequenze finali.

    Nota: questo è un esempio di albero definito implicitamente dalle regole del gioco.
    - la radice è la sequenza iniziale
    - i nodo figli di un qualsiasi nodo si ottengono eliminando una coppia di numeri uguali
    - le foglie sono le sequenze in cui non è più applicare la regola di eliminazione delle coppie

    Definire una funzione ex1(s) ricorsiva (o che fa uso di funzioni o
    metodi ricorsive/i) che prende come parametro  una  stringa  che codifica  una
    sequenza di N interi con N dispari (in questa stringa i numeri della sequenza
    compaiono uno di seguito all'altro e separati da uno spazio) e  restituisce
    l'insieme delle codifiche (stringhe con i numeri separati da uno spazio)
    delle sequenze finali che e' possibile ottenere.
      Ad esempio con s='1 2 0 1 0 0 1' la funzione ex1 deve restituire  l'insieme
      {'2 0 1', '2 1 0', '1 2 0'}


NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe
    (non può essere una funzione definita all'interno di un'altra funzione/metodo)

ATTENZIONE: Non potete usare altre librerie

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

'''

def clean(s):
    f_l = s.split()

    d = {k:f_l.count(k) for k in set(f_l)}

    return [e for e in f_l if d[e] % 2 != 0]

def get_indexes(f_l, f_s):
    return tuple([[i for i, e in enumerate(f_l) if e == k] for k in f_s if f_l.count(k) > 1])


def recurse(final_set, mem_set, f_lst):

    f_set = set(f_lst)

    # if the string hasn't duplicate elements stop the recursion
    if len(f_lst) == len(f_set):
        final_set.add(' '.join(f_lst))
        return

    idx_lst = get_indexes(f_lst, f_set)

    cp_lst = f_lst.copy()

    for t in idx_lst:
        t_len = len(t) - 1
        for i in range(t_len + 1):

            v1 = t[t_len - i - 1]
            v2 = t[t_len - i]

            # swap indexes
            if v1 > v2:
                v1, v2 = v2, v1

            f_lst.pop(v2)
            f_lst.pop(v1)

            # exit strategy
            if tuple(f_lst) in mem_set:

                # revert to original list
                f_lst = cp_lst.copy()
                continue

            # memoize
            mem_set.add(tuple(f_lst))

            recurse(final_set, mem_set, f_lst)

            # revert to original list
            f_lst = cp_lst.copy()


def ex1(s):

    f_set = set()

    recurse(f_set, set(), clean(s))

    return f_set


# @data(
# 1        (False, ' '.join(['1']*1),                             { '1' } ),
# 2        (False, ' '.join(['1']*2)+' 2',                        { '2' } ),
# 3        (False, ' '.join(['1']*7),                             { '1' } ),
# 4        (False, ' '.join(['1']*8)+' 2',                        { '2' } ),
# 5        (True,  '2 2 1 2 3',                                   { '1 2 3', '2 1 3' } ),
# 6        (False, '1 2 1 2 2',                                   { '2' } ),
# 7        (True,  '1 2 1 2 1 2 3',                               { '1 2 3', '2 1 3'} ),
# 8        (True,  '1 2 0 1 0 0 1',                               { '2 0 1', '2 1 0', '1 2 0'} ),   # esempio
# 9        (True,  '3 3 2 3 2 3 2 3 1',                           { '3 2 1', '2 3 1'} ),
# 10       (True,  '1 2 3 1 2 3 1 2 3',                           { '1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 1 2', '3 2 1'} ),
# 11       (True,  '1 2 3 2 2 1 1 3 3',                           { '1 2 3', '1 3 2', '2 1 3', '2 3 1', '3 2 1'} ),
# 12       (True,  '1 1 2 2 3 3 1 2 3',                           { '1 2 3', '1 3 2', '2 3 1', '2 1 3', '3 1 2'} ),
# 13       (True,  '1 2 1 2 1 2 1 2 1 2 3',                       { '1 2 3', '2 1 3'} ),
# 14       (True,  '1 1 2 1 1 3 1 1 4 1 5',                       { '1 2 3 4 5', '2 1 3 4 5', '2 3 1 4 5', '2 3 4 1 5'} ),
# 15       (True,  '1 2 3 4 7 5 7 6 7 8 9 8 8 6 9 5 9 4 3 2 1',   { '7 8 9', '7 9 8' } ),
# 16       (True,  '1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 10 9 10 9 10 1 8 1 7 1 6 1 5 1 4 1 3 1 2 1 11', {'9 10 11', '10 9 11'} ),
# 17       (True,  '1 '*5 + '4 '*2 + '2 '*5 + '3 '*5 + '4 '*3 + '6',   { '1 4 2 3 6', '1 2 3 4 6'} ),
# 18       (False, '1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 10 10 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1', { '11' }),
#     )
if __name__ == '__main__':
    string = '1 2 0 1 0 0 1'
    print(ex1(string))
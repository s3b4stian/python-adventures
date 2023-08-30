# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def starting_zeroes(start, lst_seq, lst_seq_len):
    count = 0
    while count <= lst_seq_len:
        if lst_seq[start+count]:
            return count
        count += 1
    return count

# hash edition 1.0.0
# how much memory for the hash?
# memory over speed?
def ex1(int_seq, subtotal):
    # from string of comma separated ints to list of integers 
    list_seq = list(map(int, int_seq.split(",")))
    # len of the list
    list_seq_len = len(list_seq) - 1

    acc_map = {0: [0]}
    acc = 0
    count = 0

    # for every element in the list
    for i, n in enumerate(list_seq):

        # compute summation
        # used as key for the hash map
        acc += n
        # calculate index as difference between the summation and the
        # subtotal
        index = acc - subtotal

        # if the index is in hash map
        # then the index is equal to the current sum minus the subtotal
        if index in acc_map:
            # increment counter
            count +=1
            # get from the hash map the start index
            # the minimum is used to determine if there are
            # zeroes behind the list
            # avoid min function call
            # list is already ordered, the smallest element is the first
            start = acc_map[index][0]
            # should be equal to:
            #start = min(acc_map[index])

            # if start isn't zero or the index isn't the first
            # then increment
            # using + instead of or decrease ciclomatic complexity
            # barbatrucco
            if start + index:
                start += 1
            # if the element of the list is a zero start to count zeroes
            # before the first non zero number
            if not list_seq[start]:
                count += starting_zeroes(start, list_seq, list_seq_len)

        if acc in acc_map:
            acc_map[acc].append(i)
            continue

        acc_map[acc] = [i]

    return count


if __name__ == '__main__':
    # Inserisci qui i tuoi test 
    print(ex1("3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2", 9))
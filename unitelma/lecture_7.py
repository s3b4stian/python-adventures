## ESERCIZI
#
#Usando la list comprehension definite le seguenti funzioni:
#
#1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi, 
#   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
#   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
#   Esempio:
#>>> triangolo(4)
#[[1],
# [2, 4],
# [3, 6, 9],
# [4, 8, 12, 16]]
#
#2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
#   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
#   in posizione i della lista passata come argomento.
#   Esempio:
#>>> potenze_crescenti([2, 3, 4, 5, 6])
# [1, 3, 16, 125, 1296]
#
#3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
#   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
#   Esempio:
#>>> non_divisibili(10, [2, 3])
#[1, 5, 7]
#
#
#4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
#    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
#    Esempio:
#>>> doppio_dado()
#3 5
#2 2
#1 6
#6 4
#3 1
#5 4
#6 6
#7

# ex. 1
def triangolo(N: int) -> list:
    return [
        [i * c for i in range(1, c + 1 )]   # value of elements
        for c in range(1, N + 1)            # number of rows
    ]

# ex. 2
def potenze_crescenti(lst: list) -> list:
    return [ lst[i] ** i for i in range(len(lst))]

# ex. 3
def non_divisibili(N: int, divisori: list) -> list:
    # get divisible numbers
    # not in list-comprehension style
    #for i in range(1, N + 1):
    #    for d in divisori:
    #        if i % d == 0:
    #            print(i) # divisible 
    #            continue
    
    # list-comprehension for numbers
    #num = [i for i in range(1, N + 1)]
    # list-comprehension for divisible numbers using dividers
    #div = [i for i in range(1, N + 1) for d in divisori if i % d == 0]
    # return the result
    #return [i for i in num if i not in div]
    # or difference between sets
    #return list(set(num) - set(div))
    return list(set([i for i in range(1, N + 1)]) - set([i for i in range(1, N + 1) for d in divisori if i % d == 0]))

# ex. 4
import random
def doppio_dado() -> None:

    def gamble() -> int:
        return random.randint(1, 6)
    
    count = 0

    while True:
        l1 = gamble()
        l2 = gamble()
        count += 1

        print(l1, l2)

        if l1 == 6 and l2 == l1:
            print(count)
            break


if __name__ == '__main__':
    # ex 1 test
    print(triangolo(4)) # print [[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]]

    # ex 2 test
    print(potenze_crescenti([2, 3, 4, 5, 6])) # print [1, 3, 16, 125, 1296]

    # ex 3 test
    print(non_divisibili(10, [2, 3])) # print [1, 5, 7]

    # ex 4 test
    doppio_dado()
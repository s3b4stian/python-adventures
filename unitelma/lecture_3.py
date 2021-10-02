## ESERCIZI
#
#1. Scrivere una funzione media(vals) che prende in input una lista vals (i cui valori si assume siano
#   numeri) e ritorna la media dei suoi valori.
#
#2. Scrivere una funzione space(s, k) che prende in input una stringa s e un intero k e ritorna una nuova
#   stringa che ha i caratteri di s separati da k spazi. Ad esempio
#   space('ciao ciao', 1) ritorna la stringa
#
#    'c i a o   c i a o'
#
#3. Scrivere una funzione crossing_over(m, f) che prese in input due liste m e f (che si assume abbiano
#   la stessa lunghezza), ritorna una nuova lista che contiene l'incrocio delle due liste come illustrato dal
#   seguente esempio (prendendo alternativamente un elemento dalla prima lista, poi dalla seconda, poi dalla prima ...):
#   crossing_over([1, 3, 5], [2, 4, 6]) 
#   ritorna la lista [1, 2, 3, 4, 5, 6]

# ex. 1
def media(vals: list):
    sum = 0
    for n in vals:
        sum += n
    return sum / len(vals)

# ex. 2
def space(s: str, k: int) -> str:
    final = ''
    for n in s:
        final = final + n + (' ' * k)
    return final

# ex. 3
def crossing_over(l1: list, l2: list) -> list:
    # length check
    if len(l1) != len(l2):
        print("lists of different length")
        return []

    # crossing
    final = []
    for n in range(len(l1)):
        final.append(l1[n])
        final.append(l2[n])
    
    return final


if __name__ == '__main__':
    # ex 1 test
    print(media([10,20,30])) # print 20.0

    # ex 2 test
    print(space('ciao ciao', 1)) # print 'c i a o   c i a o'

    # ex 3 test
    print(crossing_over([1, 3, 5], [2, 4, 6]) ) # print [1, 2, 3, 4, 5, 6]
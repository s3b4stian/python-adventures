## ESERCIZI

# Scrivere le funzioni seguenti.
# 1. occ(lst, v) ritorna una lista contenente gli indici delle occorrenze di v nella lista lst . 
#   Esempi, sia	lst = ['red','blue','red','gray','yellow','red']
# 	occ(lst, 'red')		ritorna [0,2,5]
# 	occ(lst, 'green')	ritorna []

# 2. rep(lst, k) ritorna una lista, senza ripetizioni, che contiene i valori che nella lista lst occorrono
#   almeno k volte. 
#   Esempi, sia lst = [1,2,1,5,3,4,2,1,3,5,6]

# 	rep(lst, 2)	ritorna [1,2,5,3]
# 	rep(lst, 3)	ritorna [1]
# 	rep(lst, 4)	ritorna []

# 3. lastfirst(lst) presa in input una lista lst di parole, ritorna la prima parola che inizia con un
#   carattere diverso dall'ultimo carattere della parola precedente, se non c'è ritorna None . 
#   Esempi
# 	lastfirst(['sole','elmo','orco','alba','asta'])		ritorna 'alba'
# 	lastfirst(['sky','you','use','ear','right'])		ritorna None

# 4. groupd(lst) presa in input una lista lst di interi tale che i primi tre rappresentano una data, 
#   i secondi tre un'altra data, i successivi tre un'altra data e così via, 
#   modifica la lista lst raggruppando ogni tripla in una stringa separando i numeri con il carattere '/' . 
#   Si assume che la lista lst abbia una lunghezza multipla di 3. 
#   Esempio
# >>> lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
# >>> groupd(lst)
# >>> lst
# ['1/2/2013', '23/9/2011', '10/11/2000']

# ex. 1
def occ(lst: list, v) -> list:
    final = []
    for i in range(len(lst)):
        if lst[i] == v:
            final.append(i)
    return final

# ex. 2
def rep(lst: list, k) -> list:
    final = []
    el_current = lst[0]
    lst.sort()
    count = 0

    for el in lst:
        # if element is equal then there is one more occurrence
        if el == el_current:
            count += 1
            if count >= k and el_current not in final:
                final.append(el_current)
            continue
        # restart with new element
        el_current = el
        count = 1

    return final

# ex. 3
def lastfirst(lst: list) -> list:

    # last char of the first word
    last_char = lst[0][-1]
    # list with the first element padded 
    lst = lst[1:]

    for i in range(len(lst)):
        if lst[i][0] != last_char:
            return lst[i]
        last_char = lst[i][-1]
    
    return None

# ex. 4
def groupd(lst: list) -> list:
    
    if len(lst) % 3:
        print("List must contains multiple of 3 elements")
        return []
    
    final = []
    iterate = len(lst) / 3
    count = 0

    while True:
        el1 = lst[count * 3 + 0]
        el2 = lst[count * 3 + 1]
        el3 = lst[count * 3 + 2]

        final.append(f"{el1}/{el2}/{el3}")

        count += 1
        if count == iterate:
            break
    
    lst[:] = final


if __name__ == '__main__':
    # ex 1 test
    lst = ['red','blue','red','gray','yellow','red']
    print(occ(lst, 'red')) # print [0,2,5]
    print(occ(lst, 'green')) # print []

    # ex 2 test
    lst = [1,2,1,5,3,4,2,1,3,5,6]
    print(rep(lst, 2)) # print [1,2,5,3]
    print(rep(lst, 3)) # print [1]
    print(rep(lst, 4)) # print []

    # ex 3 test
    print(lastfirst(['sole','elmo','orco','alba','asta'])) # print 'alba'
    print(lastfirst(['sky','you','use','ear','right'])) # print None

    #ex 4 test
    lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
    groupd(lst)
    print(lst) # print ['1/2/2013', '23/9/2011', '10/11/2000']
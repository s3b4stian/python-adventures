## ESERCIZIO
#
#Usando lo schema descritto definite l'algoritmo e il suo pseudo-codice e poi implementate e testate le funzioni e sottofunzioni realizzate.
#
#1)  Modificate la funzione aggiorna_k_massimi in modo da usare una lista ordinata invece che disordinata 
#    e misurate i tempi di esecuzione di k_massimi_casuali in Jupyter col comando %time per K=3000 e K=30 (e S=0, N=1000000).


# ex. 1
# function defined by prof in lecture 8
import random
def k_massimi_casuali_prof(S, N, K):
    '''estrae i K maggiori valori interi tra N generati a caso a partire dal seed S'''
    random.seed(S)
    massimi = []                                        # inizialmente i K valori massimi sono la lista vuota
    for i in range(N):                                  # per N volte
        X = random.randint(-1000000000, 1000000000)     # estraggo un valore intero a caso tra -1000000000 e +100000000000
        #if i < 10:
        #    print(X)                                   # stampo i primi 10 valori generati per testare il funzionamento
        aggiorna_K_massimi_prof(massimi, X, K)          # aggiorno i K maggiori valori inserendoci X se necessario
    return massimi                                      # torno i K valori massimi

def aggiorna_K_massimi_prof(massimi, V, K):
    '''aggiorna i K massimi aggiungendo un nuovo valore V'''
    if len(massimi) < K:                    # se massimi contiene meno di K valori
        massimi.append(V)                   # aggiungiamo V
        return                              # e usciamo
    minimo = min(massimi)
    if V <= minimo:                         # altrimenti se V è minore o uguale del minimo valore contenuto in massimi lo ignoriamo
        return
    else:			
        massimi.remove(minimo)              # altrimenti eliminiamo il minimo 
        massimi.append(V)                   # ed aggiungiamo V alla lista


# my definition
def k_massimi_casuali_my(S, N, K):
    '''estrae i K maggiori valori interi tra N generati a caso a partire dal seed S'''
    random.seed(S)
    massimi = []                                        # inizialmente i K valori massimi sono la lista vuota
    for i in range(N):                                  # per N volte
        X = random.randint(-1000000000, 1000000000)     # estraggo un valore intero a caso tra -1000000000 e +100000000000
        #if i < 10:
        #    print(X)                                   # stampo i primi 10 valori generati per testare il funzionamento
        aggiorna_K_massimi_my(massimi, X, K)            # aggiorno i K maggiori valori inserendoci X se necessario
    return massimi                                      # torno i K valori massimi

def aggiorna_K_massimi_my(massimi: list, V: int, K: int):
    '''aggiorna i K massimi aggiungendo un nuovo valore V'''
    if len(massimi) < K:                    # se massimi contiene meno di K valori
        massimi.append(V)                   # aggiungiamo V
        
        # sort in reverse order the maximum list
        if len(massimi) == K -1 : 
            massimi.sort(reverse=True)
        
        return                              # e usciamo
    
    # updated 2021-10-16
    # sort every time not needed,
    # sort only when the list "massimi" is filled
    # and when a number is greather than the the min of the "massimi"
    #
    # sort in reverse order the maximum list
    #massimi.sort(reverse=True)

    if massimi[K - 1] < V:
        massimi[K - 1] = V
        massimi.sort(reverse=True)

## binary definition
## use binary search to determine the insert position
## https://en.wikipedia.org/wiki/Binary_search_algorithm
def k_massimi_casuali_binary(S, N, K):
    '''estrae i K maggiori valori interi tra N generati a caso a partire dal seed S'''
    random.seed(S)
    massimi = []                                        # inizialmente i K valori massimi sono la lista vuota
    for i in range(N):                                  # per N volte
        X = random.randint(-1000000000, 1000000000)     # estraggo un valore intero a caso tra -1000000000 e +100000000000
        #if i < 10:
        #    print(X)                                   # stampo i primi 10 valori generati per testare il funzionamento
        aggiorna_K_massimi_binary(massimi, X, K)            # aggiorno i K maggiori valori inserendoci X se necessario
    return massimi                                      # torno i K valori massimi

def aggiorna_K_massimi_binary(massimi: list, V: int, K: int):
    '''aggiorna i K massimi aggiungendo un nuovo valore V'''
    if len(massimi) < K:                    # se massimi contiene meno di K valori
        massimi.append(V)                   # aggiungiamo V
        massimi.sort(reverse=True)
        return                              # e usciamo

    # if value less than the last value (min) return
    if massimi[K - 1] > V:
        return 

    start = 0
    end = len(massimi) - 1
    while start <= end:
        med = (start + end) // 2
        if massimi[med] == V:
            return
        if massimi[med] < V:
            end = med - 1
        else:
            start = med + 1

    massimi.insert(start, V)
    massimi.pop()


if __name__ == '__main__':
    # ex 1 test
    import time

    # lecture_8 prof
    start_time = time.time()
    k_massimi_casuali_prof(0, 1000000, 3)
    print("k_massimi_casuali_prof(0, 1000000, 3) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_prof(0, 1000000, 30)
    print("k_massimi_casuali_prof(0, 1000000, 30) -> %s seconds" % (time.time() - start_time))
    
    start_time = time.time()
    k_massimi_casuali_prof(0, 1000000, 300)
    print("k_massimi_casuali_prof(0, 1000000, 300) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_prof(0, 1000000, 3000)
    print("k_massimi_casuali_prof(0, 1000000, 3000) -> %s seconds" % (time.time() - start_time))

    # my
    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 3)
    print("k_massimi_casuali_my(0, 1000000, 3) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 30)
    print("k_massimi_casuali_my(0, 1000000, 30) -> %s seconds" % (time.time() - start_time))
    
    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 300)
    print("k_massimi_casuali_my(0, 1000000, 300) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 3000)
    print("k_massimi_casuali_my(0, 1000000, 3000) -> %s seconds" % (time.time() - start_time))

    # binary
    start_time = time.time()
    k_massimi_casuali_binary(0, 1000000, 3)
    print("k_massimi_casuali_binary(0, 1000000, 3) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_binary(0, 1000000, 30)
    print("k_massimi_casuali_binary(0, 1000000, 30) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_binary(0, 1000000, 300)
    print("k_massimi_casuali_binary(0, 1000000, 300) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_binary(0, 1000000, 3000)
    print("k_massimi_casuali_binary(0, 1000000, 3000) -> %s seconds" % (time.time() - start_time))

    #python3 lecture_8.py
    #k_massimi_casuali_prof(0, 1000000, 3) -> 1.246842622756958 seconds
    #k_massimi_casuali_prof(0, 1000000, 30) -> 1.6349496841430664 seconds
    #k_massimi_casuali_prof(0, 1000000, 300) -> 5.65403938293457 seconds
    #k_massimi_casuali_prof(0, 1000000, 3000) -> 50.485573053359985 seconds
    #k_massimi_casuali_my(0, 1000000, 3) -> 1.337632179260254 seconds
    #k_massimi_casuali_my(0, 1000000, 30) -> 1.5415916442871094 seconds
    #k_massimi_casuali_my(0, 1000000, 300) -> 3.6739466190338135 seconds
    #k_massimi_casuali_my(0, 1000000, 3000) -> 26.644742012023926 seconds
    #k_massimi_casuali_binary(0, 1000000, 3) -> 1.121171236038208 seconds
    #k_massimi_casuali_binary(0, 1000000, 30) -> 1.1237034797668457 seconds
    #k_massimi_casuali_binary(0, 1000000, 300) -> 1.1618597507476807 seconds
    #k_massimi_casuali_binary(0, 1000000, 3000) -> 1.280822992324829 seconds

    # updated 2021-10-16
    #python3 lecture_8.py
    #k_massimi_casuali_prof(0, 1000000, 3) -> 1.3435778617858887 seconds
    #k_massimi_casuali_prof(0, 1000000, 30) -> 1.7178945541381836 seconds
    #k_massimi_casuali_prof(0, 1000000, 300) -> 5.232067108154297 seconds
    #k_massimi_casuali_prof(0, 1000000, 3000) -> 47.043272733688354 seconds
    #k_massimi_casuali_my(0, 1000000, 3) -> 1.2666878700256348 seconds
    #k_massimi_casuali_my(0, 1000000, 30) -> 1.2948362827301025 seconds
    #k_massimi_casuali_my(0, 1000000, 300) -> 1.2701592445373535 seconds
    #k_massimi_casuali_my(0, 1000000, 3000) -> 1.7441291809082031 seconds
    #k_massimi_casuali_binary(0, 1000000, 3) -> 1.2009193897247314 seconds
    #k_massimi_casuali_binary(0, 1000000, 30) -> 1.227834939956665 seconds
    #k_massimi_casuali_binary(0, 1000000, 300) -> 1.2440893650054932 seconds
    #k_massimi_casuali_binary(0, 1000000, 3000) -> 1.4425880908966064 seconds
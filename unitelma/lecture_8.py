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
        return                              # e usciamo
    
    # sort in reverse order the maximum list
    massimi.sort(reverse=True)
    
    if massimi[K - 1] < V:
        massimi[K - 1] = V
        massimi.sort(reverse=True)

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
        return                              # e usciamo
    
    # sort in reverse order the maximum list
    massimi.sort(reverse=True)
    
    # if value less than the last value (min) return
    if massimi[K - 1] > V:
        return 

    start = 0
    end = K - 1
    while start <= end
        med = (start + end) // 2
        if massimi[med] == V:
            massimi.insert(med, V)
            return
        if massimi[med] > V:
            end = med - 1
        else:
            start = med + 1
    
    massimi.insert(start, V)
    ## to be continued


if __name__ == '__main__':
    # ex 1 test
    import time

    # lecture_8 prof
    start_time = time.time()
    k_massimi_casuali_prof(0, 1000000, 3)
    print("k_massimi_casuali_prof(0, 1000000, 3) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    print(k_massimi_casuali_prof(0, 1000000, 30))
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
    print(k_massimi_casuali_my(0, 1000000, 30))
    print("k_massimi_casuali_my(0, 1000000, 30) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 300)
    print("k_massimi_casuali_my(0, 1000000, 300) -> %s seconds" % (time.time() - start_time))

    start_time = time.time()
    k_massimi_casuali_my(0, 1000000, 3000)
    print("k_massimi_casuali_my(0, 1000000, 3000) -> %s seconds" % (time.time() - start_time))

    #using an ordered list to retrieve the max numbers
    #make the function about twice fast than search the minimum
    #when the number of max retrieved grows

    #python3 lecture_8.py
    #k_massimi_casuali_prof(0, 1000000, 3) -> 1.2600388526916504 seconds
    #k_massimi_casuali_prof(0, 1000000, 30) -> 1.64522385597229 seconds
    #k_massimi_casuali_prof(0, 1000000, 300) -> 5.171779155731201 seconds
    #k_massimi_casuali_prof(0, 1000000, 3000) -> 48.244898557662964 seconds
    #k_massimi_casuali_my(0, 1000000, 3) -> 1.3393447399139404 seconds
    #k_massimi_casuali_my(0, 1000000, 30) -> 1.5240411758422852 seconds
    #k_massimi_casuali_my(0, 1000000, 300) -> 3.6553397178649902 seconds
    #k_massimi_casuali_my(0, 1000000, 3000) -> 27.139545679092407 seconds
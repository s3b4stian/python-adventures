# -*- coding: utf-8 -*-
'''Nel gioco "chi la spara più grossa" si sfidano due concorrenti A e
B che generano delle sequenze di valori di lunghezza variabile,
rappresentati da un singolo carattere. Le sequenze possono essere di
lunghezza diversa poiché i valori possono essere separati da uno (o
più) spazi bianchi e tab ('\t'). Il numero di caratteri non spazio è,
comunque, uguale per ogni sequenza.

Ogni elemento della sequenza di A viene confrontato con l'elemento
corrispondente della sequenza di B e viene assegnato un punto
- al concorrente che ha generato il valore più alto (per esempio A),
  se la differenza fra il valore di A e il valore di B è inferiore o
  uguale ad un parametro k deciso all'inizio della sfida
- al concorrente che ha generato il valore più basso (per esempio B),
  se la differenza fra il valore di A e il valore di B è superiore
  a k (cioè A ha sballato)
- a nessuno, in caso di pareggio.
Al termine dell'assegnazione, vince chi ha ottenuto più punti. In caso
di pareggio, vince il giocatore che ha generato la sequenza con somma
totale dei valori inferiore.  In caso di ulteriore pareggio, il punto
è assegnato al giocatore con la prima sequenza in ordine
lessicografico. Non può capitare che due giocatori generino
esattamente la stessa sequenza di valori.

Si deve realizzare una funzione che prende in input il parametro k e
una lista di stringhe corrispondenti a un torneo di "chi la spara più
grossa" e restituisce la classifica finale del torneo. La stringa in
posizione i corrisponde alla sequenza dei valori generati dal
giocatore i.

Nel torneo, ogni giocatore sfida tutti gli altri con la propria
sequenza: ovvero, se ci sono n giocatori, ogni giocatore farà n-1
sfide. Il numero di sfide vinte determina la posizione in
classifica. In caso di parità di sfide vinte, i giocatori sono
ordinati in modo crescente in base alla posizione.

Esempio di partite a chi la spara più grossa fra tre giocatori.
    Se k=2 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2.
        Alla fine 0 ha 1 sfida, 1 ha 2 sfide e 2 ha 0 sfide, per cui
            la classifica finale sarà [1, 0, 2].

    Se k=1 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 0 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 2 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        Alla fine 0 ha 2 sfide, 1 ha 0 sfide e 2 ha 1 sfida, per cui
            la classifica finale sarà [0, 2, 1].

    Se k=10 e la lista è  [ "abc",  "dba" , "eZo"]
        La sfida 0, 1 è un pareggio, ma vince 0 perché la sua sequenza
            ha somma inferiore.
        La sfida 0, 2 è vinta da 0 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'c'.
        La sfida 1, 2 è vinta da 1 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'a'
        Alla fine 0 ha 2 sfide, 1 ha 1 sfida e 2 ha 0 sfide, per cui
            la classifica finale sarà [0, 1, 2].

    Se k=50 e la lista è  [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        La sfida 0, 1 è vinta da 1 per 4 punti a 0.
        La sfida 0, 2 è vinta da 2 per 3 punti a 1.
        La sfida 1, 2 è vinta da 1 per 3 punti a 1.
        Alla fine 0 ha 0 sfide, 1 ha 1 sfida e 2 ha 2 sfide, per cui
        la classifica finale sarà [1, 2, 0].

Il timeout per l'esecuzione di ciascun test è di 6 secondi (*2 sualla VM)

'''
# play a match between two players
def do_match(player_a: str, player_b: str, k:int) -> int:
    # create a var for two players points
    # add +1 if player a wins the round
    # add -1 if player b wins the round
    player_points = 0

    # - match rounds
    for ord_a, ord_b in zip(player_a, player_b):

        # - point attribution
        if ord_a > ord_b:
            player_points += 1 if ord_a - ord_b <= k else -1
        elif ord_a < ord_b:
            player_points += -1 if ord_b - ord_a <= k else 1

        # other solution
        # use only one if-elif but math operations are more expensive
        # in terms of time
        # complexity fall to 5
        #if ord_a > ord_b:
        #    player_points += 1 + int(ord_a - ord_b > k) * -2
        #elif ord_a < ord_b:
        #    player_points += -1 + int(ord_b - ord_a > k) * 2

        # - end point attribution
    # - end match rounds

    return player_points

# prepare matches data to be used
# calculate the ord() of all char
# remove space or tabulation characters
def create_matches(matches: list) -> tuple:
    m_final = []
    p_final = []

    for i, s in enumerate(matches):
        # create a list of ord values for every char
        tmp = [ord(c) for c in s if c != " " and c != "\t"]
        # append values
        m_final.append(tuple(tmp))
        # append values to the list to track points
        p_final.append((0, i))
    return p_final, m_final

# https://en.wikipedia.org/wiki/Combination
# k is always 2
def combinations(n: int) -> list:
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

# return the id of the player with more points after the match
def calculate_winner(player_points: int, player_a_id: int, player_b_id: int):

    if player_points > 0:
        return player_a_id

    if player_points < 0:
        return player_b_id
    
    return None

# return the id of the player if the match is even
def calculate_playoff(player_a_id: int, player_b_id:int , tup_a: tuple, tup_b: tuple) -> int:

    sum_a = sum(tup_a)
    sum_b = sum(tup_b)

    if sum_a < sum_b:
        return player_a_id

    # lexicographical order
    # if sum are equals
    if sum_a == sum_b:
        # is this really needed?
        if tup_a > tup_b:
            return player_b_id
        return player_a_id

    return player_b_id

def ex(matches, k):

    # create a list of tuples where every tuple contains
    # - the ord of every char
    # - th index of the string into the list
    # create a tuple to insert results
    points_final, matches = create_matches(matches)

    # calculate matches combination to avoid to repeat matches
    matches_combination = combinations(len(matches))

    # do matches
    for i, c in matches_combination:

        # calculate the winner
        # the match as first argument of this function
        # returns the result of the match
        winner = calculate_winner(do_match(matches[i], matches[c], k), i, c)

        # go play off if the match has a even result
        if winner == None:
            winner = calculate_playoff(i, c, matches[i], matches[c])

        points_final[winner] = (points_final[winner][0] + 1, winner)

    # return the result list
    # from points_final sorted considering the first element of the tuple (points)
    # list comprehension using the second element of the tuple (player id)
    return [x[1] for x in sorted(points_final, reverse=True, key=lambda x: x[0])]


if __name__ == "__main__":
    # Inserisci qui i tuoi test
    k        = 2
    matches  = ["aac","ccc","caa"]
    expected = [1, 0, 2]

    ex(matches, k)

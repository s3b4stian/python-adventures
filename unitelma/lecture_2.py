## ESERCIZI
#
#1. Scrivere una funzione 'scontato' che prende in input un importo e una percentuale di sconto e ritorna
#   l'importo scontato. Ad esempio, se l'importo è 1000 e lo sconto è 20 , la funzione ritorna 800 .
#
#2. Scrivere una funzione 'secondi' che prende in input un lasso di tempo espresso tramite numero di ore
#   hh , numero di minuti mm e numero secondi ss e ritorna l'equivalente numero di secondi. Ad esempio,
#   se hh = 2 , mm = 1 e ss = 11 , la funzione ritorna 7271 .
#
#3. Scrivere una funzione 'invest' che prende in input un capitale C , un interesse annuale i e un numero di
#   anni n e ritorna come intero il capitale maturato dopo un investimento di n anni all'interesse i .
#   (usando la formula     maturato = capitale * (1+interesse/100)**anni )
#   Ad esempio, se gli argomenti sono  C = 1000 , i = 10 e n = 2 , la funzione ritorna 1210 .

# ex. 1
def scontato(importo, sconto):
    return importo - (importo * sconto / 100)

# ex 2
def secondi(ore: int, minuti: int, secondi: int) -> int :
    return secondi + (minuti * 60) + (ore * 3600)

# ex 3
def invest(capitale, interesse, anni):
    return int(capitale * (1+interesse/100)**anni)


if __name__ == '__main__':
    # ex 1 test
    print(scontato(1000, 20)) # print 800.0

    # ex 2 test
    print(secondi(2, 1, 11)) # print 7271

    # ex 3 test
    print(invest(1000, 10, 2)) # print 1210
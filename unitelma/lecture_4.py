## ESERCIZI

# Scrivere le funzioni seguenti.
# 1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
#   o uguale alla data g2, m2, a2 .
#   Esempi
#   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
#   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
#   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True

# 2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
#   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
#   elementi di lst . Esempio
#   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]

# 3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
#   ripetizioni.
#   Esempi
#   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
#   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']

# 4. search(lst, andc, orc, notc) ritorna una nuova lista di stringhe che contiene le stringhe s della lista
#   lst tali che tutte le stringhe della lista andc sono sottostringhe di s, almeno una delle stringhe della
#   lista orc (se orc non è vuota) è una sottostringa di s e nessuna delle stringhe della lista notc è una
#   sottostringa di s. 
#   Esempi, sia lst = ['mela','pera','melo']
#   search(lst,['el','a'],['ra','pe','m'],['tt','lo'])	ritorna ['mela']
#   search(lst,[],['ra','pe','m'],['tt','lo'])		ritorna ['mela','pera']
#   search(lst,['el','a'],[],['tt''lo'])			ritorna ['mela']
#   search(lst,[],['ra','pe','m'],[])			ritorna ['mela','pera','melo']

# ex. 1
def prec(g1: int, m1: int, a1: int, g2: int, m2: int, a2: int) -> bool:
    # turn on iso8601 date format
    g1 = "%02d" % g1
    g2 = "%02d" % g2
    m1 = "%02d" % m1
    m2 = "%02d" % m2
    a1 = "%04d" % a1
    a2 = "%04d" % a2
    return int(f"{a1}{m1}{g1}") <= int(f"{a2}{m2}{g2}")

# ex. 1 shortest solution
#def prec(g1: int, m1: int, a1: int, g2: int, m2: int, a2: int) -> bool:
#    return [a1,m1,g1] <= [a2,m2,g2]

# ex. 2
def l2d(lst: list) -> list:
    numbers = {'zero':0, 'uno':1, 'due':2, 'tre':3, 'quattro':4, 'cinque':5, 'sei':6, 'sette':7, 'otto':8, 'nove':9}
    final = []
    for s in lst:
        if s in numbers.keys():
            final.append(numbers[s])

    return final

# ex. 3
def distinct(lst: list) -> list:
    final = [lst[0]]
    for e in lst:
        if e in final:
            continue
        final.append(e)
    return final    

# ex. 4
def search(lst: list, andc: list, orc: list, notc: list) -> list:
    
    def andc_f(el: str, andc_l: list) -> bool:
        # all must be true
        # at least one false return false
        for c in andc_l:
            if c not in el:
                return False
        return True

    def orc_f(el: str, orc_l: list) -> bool:
        # if void return true
        if not len(orc_l):
            return True
        # at least one true return true
        for c in orc_l:
            if c in el:
                return True
        return False

    def notc_f(el: str, notc_l: list) -> bool:
        # notc is exactely the opposite of orc
        # at least one false return false
        for c in notc_l:
            if c in el:
                return False
        return True

    final = []
    for e in lst:
        if andc_f(e, andc) and orc_f(e, orc) and notc_f(e, notc):
            final.append(e)

    return final



if __name__ == '__main__':
    # ex 1 test
    print(prec(13, 11, 2012,  2,  3, 2013)) # print True
    print(prec(13, 11, 2012, 27, 12, 2011)) # print False
    print(prec( 1, 10, 2013,  1, 11, 2013)) # print True
    
    # ex 2 test
    print(l2d(['nove','due','due','tre'])) # print [9,2,2,3]

    # ex 3 test
    print(distinct([3,1,3,2,6,6])) # print [3, 1, 2, 6]
    print(distinct(['a','ab','a','ab'])) # print ['a', 'ab']

    # ex 4 test
    lst = ['mela','pera','melo']
    print(search(lst,['el','a'],['ra','pe','m'],['tt','lo'])) # print ['mela']
    print(search(lst,[],['ra','pe','m'],['tt','lo'])) # print ['mela','pera']
    print(search(lst,['el','a'],[],['tt''lo'])) # print ['mela']
    print(search(lst,[],['ra','pe','m'],[])) # print ['mela','pera','melo']
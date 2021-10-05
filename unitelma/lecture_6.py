## ESERCIZI
#Scrivere le funzioni seguenti.
#
#1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None . 
#	Esempio
#>>> t = '''Quant’è bella giovinezza
#che si fugge tuttavia!
#Chi vuol esser lieto, sia:
#del doman non c’è certezza.'''
#	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'
#
#2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t . 
#	Esempio
#	t = 'le cose non sono solo cose, ma anche cosette'
#	countw(t, 'cose') 		ritorna		2
#
#3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t . 
#   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale. 
#	Esempio
#	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
#	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']
#
#4. column(table, k) ritorna una lista che contiene i valori della colonna k della tabella table . 
#   La tabella è rappresentata in modo che ogni linea di table contiene una riga e i valori delle colonne sono separati
#   dal carattere ';' . Se table ha n colonne, allora ogni linea di table conterrà esattamente n-1 caratteri ';' .
#	Esempio
#	table = '''Milano;12;23
#Roma;16;25
#Napoli;15;27
#Firenze;11;20'''
#	column(table, 1)		ritorna		['12', '16', '15', '11']

# ex. 1
def firstline(t: str, s: str):
    for l in t.splitlines():
        #if l.count(s):
        if s in l:
            return l
    return None

# ex. 2
def countw(t: str, w: str) -> int:
    count = 0
    for el in t.split(" "):
        if el.strip(',.:;?!*^%&\\/"\'') == w:
            count += 1
    return count

# ex. 3
def digits(t: str) -> list:
    final = []
    tmp = ''
    for c in t:
        if c.isdecimal():
            tmp = tmp + c
            continue
        
        if tmp:
            final.append(tmp)
            tmp = ''

    return final

# ex. 4
def column(table, k):
    rows = table.splitlines()
    final = []

    if k < 0 and k > rows[0].count(';'):
        return final

    for r in rows:
        final.append(r.split(';')[k])

    return final


if __name__ == '__main__':
    # ex 1 test
    t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''
    print(firstline(t, 'non')) # print 'del doman non c’è certezza.'
    
    # ex 2 test
    t = 'le cose non sono solo cose, ma anche cosette'
    print(countw(t, 'cose')) # print 2

    # ex 3 test
    t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
    print(digits(t)) # print ['23', '06', '7867555', '345', '675665676', '34565']

    # ex 4 test
    table = '''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20'''
    print(column(table, 1)) # print ['12', '16', '15', '11']
## ESERCIZI

# Scrivere le funzioni seguenti.

# 1. clines(fname, s) ritorna il numero di linee del file di testo fname che contengono la stringa s senza
#   differenziare tra maiuscole e minuscole. Esempi: se il file testo.txt contiene le 4 righe

# SUGLI ERRORI
# Gli errori sono inevitabili. Errare è umano,
# perseverare è diabolico. Non ci sono rimedi
# a questo stato di cose (su questa terra).

# allora
# 	clines('testo.txt', 'err')	ritorna 3
# 	clines('testo.txt', 'Errori')	ritorna 2

# 2. all_char(fname, enc) ritorna una stringa unicode contenente tutti i caratteri, senza ripetizioni e in
#   ordine di apparizione, nel file fname decodificato con la codifica enc . Ad esempio se il file è quello
#   dell'esercizio precedente, assumendo che sia codificato in UTF-8, si ha:

# >>> allc = all_char('testo.txt', 'utf8')
# >>> allc
# 'SUGLI ERO\nlierosnvtab.èum,pdcNq()'
# >>> print(allc)
# SUGLI ERO
# lierosnvtab.èum,pdcNq()

# 3. anagrams(fname, w) ritorna una lista contenente tutti gli anagrammi, senza ripetizioni e senza
#   differenziare tra maiuscole e minuscole, della parola w nel file fname . Un anagramma di una parola w è
#   un'altra parola che usa esattamente le stesse lettere di w ma in ordine diverso, ad esempio mangiare e
#   germania, torre e retro. La lista ritornata deve includere anche la parola w stessa, se è presente.
#   Possono risultare utili la funzione built-in sorted() e il metodo join() delle stringhe.
#   Nel risultato non ci devono essere doppioni.
#   Esempi, sia fname il file 'alice.txt' :

# >>> anagrams(fname, 'read')	ritorna ['dear', 'read', 'dare']
# >>> anagrams(fname, 'elbow')	ritorna ['elbow', 'below']

# 4. log_update(filelog, evento) aggiorna il file filelog aggiungendo una nuova linea che inizia con la data e l'orario
#   della chiamata e dopo ': ' la stringa in evento . Per ottenere la data e l'orario si possono usare le funzioni
#   ctime() e time() del modulo time della libreria standard. Esempio, se il file log contiene:

# Mon Oct 7 17:48:22 2013: first event
# Mon Oct 7 17:48:32 2013: second event
# Mon Oct 7 17:49:15 2013: Event n. 3

# e se dopo 84 secondi dall'ultimo aggiornamento viene effettuata la chiamata log_update(log, 'New event!') , il file log diventa:

# Mon Oct 7 17:48:22 2013: first event
# Mon Oct 7 17:48:32 2013: second event
# Mon Oct 7 17:49:15 2013: Event n. 3
# Mon Oct 7 17:50:39 2013: New event!

# 5. findurl(lista_url, s, k) ritorna in una lista gli URL contenuti nella lista lista_urls tali che le pagine da essi puntate contengano almeno k
#   occorrenze della stringa s . Si assume che gli URL in urls siano relativi a pagine HTML e quindi documenti di testo. 
#   Esempi, sia

# >>> urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
# >>> findurl(urls, 'Python', 2) ritorna 
# ['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
# >>> findurl(urls, 'Python', 7) ritorna 
# ['http://python.org', 'http://docs.python.org/2.7/index.html']

# ex. 1
def clines(fname: str, s: str) -> int:

    count = 0
    
    # using functions
    #f = open(fname, encoding='utf8')
    #for l in f.readlines():
    #    if s.lower() in l.lower():
    #        count += 1
    #f.close()

    # using statement
    # no file close needed
    with open(fname, encoding='utf8') as f:
        for l in f.readlines():
            if s.lower() in l.lower():
                count += 1

    return count

# ex. 2
def all_char(fname: str, enc: str) -> str:
    chars = []
    with open(fname, encoding='utf8') as f:
        for l in f.read():
            if l not in chars:
                chars.append(l)
    
    return ''.join(chars)

# ex. 3
def anagrams(fname: str, w: str) -> list:

    # return a list of all words in text
    # all words are converted in lowercase for
    # further comparation
    def words(text: str) -> list:
        final = ''
        for c in text:
            if c.isalpha() or c.isspace():
                final += c.lower()
            else:
                final += ' '
        
        return final.split()
    
    # remove duplicated words in a list
    def unique(word_list: list) -> list:
        final = []
        for el in word_list:
            if el not in final:
                final.append(el)
        return final

    with open(fname, encoding='utf8') as f:
        # create a list of unique words in text
        words_unique = unique(words(f.read()))
        # order the letters in the word passed as second argument
        ordered_param_w = ''.join(sorted(list(w)))

        final = []
        for word in words_unique:
            ordered_list_w = ''.join(sorted(list(word)))
            # if the ordered word match with the ordered word passed
            # as second argument, the word in list is an anagram
            if ordered_list_w == ordered_param_w:
                final.append(word)

    return final

# ex. 4
import time
def log_update(filelog: str, evento: str):
    with open(filelog, mode="a") as f:
        f.write(f"{time.ctime()}: {evento}\n")

# ex. 5
import requests
def findurl(lista_url: list, s: str, k: int) -> list:
    
    final = []

    for url in lista_url:    
        r = requests.get(url=url)
        if r.text.count(s) >= k:
            final.append(url)

    return final


if __name__ == '__main__':
    # ex 1 test
    print(clines('lec_09_files/testo.txt', 'err')) # print 3
    print(clines('lec_09_files/testo.txt', 'Errori')) # print 2

    # ex 2 test
    print(all_char('lec_09_files/testo.txt', 'utf8')) # print 'SUGLI ERO\nlierosnvtab.èum,pdcNq()'

    # ex 3 test
    print(anagrams('lec_09_files/alice.txt', 'read')) # print ['dear', 'read', 'dare']
    print(anagrams('lec_09_files/alice.txt', 'elbow')) # print ['elbow', 'below']

    # ex 4 test
    ## delete  he file if exists
    import os
    filename = 'lec_09_files/log.log'

    if os.path.exists(filename):
        os.unlink(filename)

    ## write first batch of logs
    log_update(filename, 'inzio del log')
    log_update(filename, 'seconda riga del log')
    log_update(filename, 'terza riga del log')

    ## sleep
    #time.sleep(4)

    ## write next batch of logs
    log_update(filename, 'quarta riga del log')
    log_update(filename, 'quinta riga del log')

    ## check the log
    with open(filename) as f:
        print(f.read())

    # ex 5 test
    urls = ['http://python.org', 'http://google.com', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html']
    print(findurl(urls, 'Python', 2)) # print ['http://python.org', 'http://docs.python.org/2.7/index.html', 'http://pellacini.di.uniroma1.it/teaching/fondamenti13/index.html'] 
    print(findurl(urls, 'Python', 7)) # print ['http://python.org', 'http://docs.python.org/2.7/index.html']
    print(findurl(urls, 'Python', 50)) # print ['http://python.org']
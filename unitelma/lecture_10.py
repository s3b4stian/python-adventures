## ESERCIZI

# Scrivere le funzioni seguenti.
# 1. wset(fname) ritorna un insieme contenente le parole (distinte) del file fname . Le parole sono ridotte
#   alle minuscole e il file è decodificato con UTF-8-SIG. 
#   Esempio
# >>> wset('alice.txt') ritorna un insieme di cardinalità 3007

# 2. wsub(fn1, fn2) ritorna un insieme contenente le parole (distinte) che appaiono nel file fn1 e che non
#   appaiono nel file fn2 . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
#   Esempio
# >>> wsub('alice.txt', 'holmes.txt') ritorna un insieme di cardinalità 710

# 3. wdict(fname) ritorna un dizionario che ad ogni parola del file fname associa il numero di occorrenze
#   della parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
#   Esempio
# >>> d = wdict('alice.txt')
# >>> d['alice'] --> 403
# >>> d['rabbit'] --> 51
# >>> d['queen'] --> 75

# 4. nextw(fname) ritorna un dizionario che ad ogni parola del file fname associa l'insieme delle parole che
#   seguono la parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
#   Esempio
# >>> d = nextw('alice.txt')
# >>> d['go']
# {'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for', 
# 'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
# >>> d['write']
# {'that', 'this', 'it', 'one', 'with', 'out'}

# 5. mostf(fname, l) ritorna un insieme contenente le parole di lunghezza l di massima frequenza nel file
#   fname . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG. 
#   Esempi
# >>> mostf('holmes.txt', 7)
# {'nothing', 'however'}
# mostf('holmes.txt', 8)
# {'sherlock'}
# mostf('frankenstein.txt', 16) 
# {'unenforceability', 'impracticability', 'perpendicularity', 'indiscriminately', 'inextinguishable'}

# utility funcs

## returns words in a text
def words(text: str) -> list:
    final = ''
    for c in text:
        if c.isalpha() or c.isspace():
            final += c.lower()
        else:
            final += ' '
        
    return final.split()

# ex. 1
def wset(fname: str) -> set:
    with open(fname, encoding='utf-8-sig') as f:
        # create a list of unique words in text using a set
        return set(words(f.read()))

# ex. 2
def wsub(fn1: str, fn2: str) -> set:
    # open first file
    with open(fn1, encoding='utf-8-sig') as f1:
        # open second file
        with open(fn2, encoding='utf-8-sig') as f2:
            # return the difference between two sets
            return set(words(f1.read())) - set(words(f2.read()))

# ex. 3
# first version
def wdict(fname: str) -> dict:
    with open(fname, encoding='utf-8-sig') as f:
        list_sorted = sorted(words(f.read()))
    
    final = {}
    current = list_sorted[0]
    count = 1

    for i in list_sorted:

        if i != current:
            current = i
            count = 1

        final[i] = count
        count +=1

    return final

# more concise version
def wdict_1(fname: str) -> dict:
    with open(fname, encoding='utf-8-sig') as f:
        list_sorted = sorted(words(f.read()))

    # starting condition
    current = list_sorted[0]
    final = {current:0}

    for i in list_sorted:
        # every time the key change
        # remember the ordered list?
        # set new current and initialize final[i] with zero
        if i != current:
            current = i
            final[i] = 0

        final[i] += 1

    return final

# ex. 4
def nextw(fname: str) -> dict:
    with open(fname, encoding='utf-8-sig') as f:
        list_words = words(f.read())

    final = {}

    for i in range(len(list_words) - 1):
        if list_words[i] not in final:
            final[list_words[i]] = set()
        
        # the worst method to add an element to a set
        #final[list_words[i]] = set(list(final[list_words[i]]) + [list_words[i+1]])
        # a bit more elegant
        final[list_words[i]].add(list_words[i+1])

    return final


# ex. 5
# "a braccio" version
# reuse wdict_1 function to get the occurrences of a word in a text
def mostf(fname: str, l: int) -> set:
    # retrieve the dict of occurrences
    # should perform in O(N)
    d_wdict_1 = wdict_1(fname)
    # initial values
    max_words = set()
    max_freq = 0
    # for every key in dict, and every key is a word of the text
    # should perform in O(N)
    for key in d_wdict_1:
        # check the len of the word
        if len(key) == l:
            # the word has a frequency greather than the previous max frequency
            if d_wdict_1[key] > max_freq:
                # set new frequency
                max_freq = d_wdict_1[key]
                # reset the word set
                max_words = set([key])
                continue
            # the word has a frequency equal to max. add it to the set
            if d_wdict_1[key] == max_freq:
                max_words.add(key)

    return max_words


if __name__ == '__main__':

    # ex 1 test
    print(len(wset('lec_09_files/alice.txt'))) # print 3007

    # ex 2 test
    print(len(wsub('lec_09_files/alice.txt', 'lec_09_files/holmes.txt'))) # print 710

    # ex 3 test
    d = wdict_1('lec_09_files/alice.txt')
    print(d['alice']) # print 403
    print(d['rabbit']) # print 51
    print(d['queen']) # print 75

    # ex 4 test
    d = nextw('lec_09_files/alice.txt')
    print(d['go']) # print {'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for', 'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
    print(d['write']) # print {'that', 'this', 'it', 'one', 'with', 'out'}

    # ex 5 test
    print(mostf('lec_09_files/holmes.txt', 7)) # print {'nothing', 'however'}
    print(mostf('lec_09_files/holmes.txt', 8)) # print {'sherlock'}
    print(mostf('lec_09_files/frankenstein.txt', 16)) # print {'unenforceability', 'impracticability', 'perpendicularity', 'indiscriminately', 'inextinguishable'}

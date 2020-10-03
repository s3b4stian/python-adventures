####################
# function parameter
####################


##############################################################
# argument vs parameter
# parameter -> in the code of the function, during declaration
# arguments -> variables passed when there is a functino calls
##############################################################

def _my_func(a, b): # a and b are parameter
    return a + b

x = 10
y = 10

_my_func(x, y) # x and y are arguments


###################################
# positional and keywiord arguments
###################################

## positional arguments
def my_func_0(a, b, c):
    print(f"a={a}, b={b}, c={c}")

my_func_0(1, 2, 3)

## default arguments
def my_func_1(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")

my_func_1(10)
my_func_1(10, 20)
my_func_1(10, 20, 30)

## keyword arguments (named arguments)
def my_func_2(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")

my_func_2(a=10, c=30)
my_func_2(a=10, b=20)
my_func_2(10, c=30)
my_func_2(10, b=20)
my_func_2(10, b=20, c=30)
my_func_2(10, c=30, b=20)
my_func_2(c=30, b=20, a=10)


#####################
# unpacking iterables
#####################

## side note about tuples
## in python the thin that define the tuple is the comma
## (1) isn't a tuple with 1 element but a int
## ('a') isn't a tuple with 1 element but a str
## 1, create a tuple with one element (1,) with parethesis
## () must be used for create an empty tuple
a = (1,2,3) # is equal to
b = 1, 2, 3

print(a, b)

## packed values
## any iterable is considered a packed value
## unpack into individual element

## unpack list
a, b, c = [1, 'b', 3.14]
print(a)
print(b)
print(c)
## or, works same
(a, b, c) = [1, 'b', 3.14]
print(a)
print(b)
print(c)

## unpack tuple
### python evaluate first, right hand side completely
a, b, c = (1, 'b', 3.14)
print(a)
print(b)
print(c)

### parallelment assignement (it is also unpacking)
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

### easily swap variables due to RHS evaluation
a = 10
b = 20
print(a, b)
a, b = b, a # instead of use a tmp variable
print(a, b)

## unpack strings
for e in 'ABC': ## iterate string
    print(e)

a, b, c = "ABC"
print(a)
print(b)
print(c)

## unpack set
## can unpack but no order is guaranted
a, b, c = {1, 2, 3}
print(a)
print(b)
print(c)

s = {"p", "y", "t", "h", "o", "n"}
print(s)

for e in s:
    print(e)

## unpack dictionaries
d = {'a':1, 'b':2, 'c':3}
for e in d:
    print(e) # iterate the keys

### unpack do the same
a, b, c = d
print(a)
print(b)
print(c)

### works well due to RHS
d = {'a':1, 'b':2, 'c':3, 'd': 4}
a, b, c, d = d
print(a)
print(b)
print(c)
print(d)

d = {'a':1, 'b':2, 'c':3, 'd': 4}
for e in d.values():
    print(e) # iterate the keys

### unpack values
a, b, c, d = d.values()
print(a)
print(b)
print(c)
print(d)

d = {'a':1, 'b':2, 'c':3, 'd': 4}
for e in d.items():
    print(e) # iterate a tuple (key, value)
    key, value = e # unpack the tuple
    print(key, value)

for key, value in d.items(): # more concise
    print(key, value)

### unpack values
a, b, c, d = d.items()
print(a)
print(b)
print(c)
print(d)


####################
# extended unpacking
# python >= 3.5
####################


## standard assign
l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]

print(a, b)

## ununpacking
l = [1, 2, 3, 4, 5, 6]
a, b = l[0], l[1:]

print(a, b)

## extended unpacking
## more simple syntax
## works with any iterable not just for sliceable types (list, tuple)
## star expression return every time a list
l = [1, 2, 3, 4, 5, 6]
a, *b = l

print(a, b)

### strings, are also iterables
s = 'python'
a, *b = s
print(a, b)

s = 'python'
a, b, *c = s
print(a, b, c)

s = 'python'
a, b, *c, d = s
print(a, b, c, d)

### last example is equal to did with slicing
### but c contain a str instead of a list
s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a, b, c, d)

## extended unpacking LHS
l1 = [1, 2, 3]
l2 = [4, 5, 6]
### unpack and merge into list
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
l2 = 'abc'
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
l2 = {'x', 'y', 'z'}
l = [*l1, *l2]
print(l)

s1 = 'abc'
s2 = 'cde'
l = [*s1, *s2]
print(l)

### unpack into set, duplicated values removed
s1 = 'abc'
s2 = 'cde'
l = {*s1, *s2}
print(l)

## extended unpacking and sets
s = {10, -99, 2 , 'd'}
a, b, c, d = s
print(a, b, c, d)

### works well but the order isn't guaranteed
s = {10, -99, 2 , 'd'}
a, b, *c = s
print(a, b, c)

### set to list
### comma isn't a typo
s = {10, -99, 2 , 'd'}
*c, = s
print(s)
print(c)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s = {*s1, *s2}
print(s)
### same as
print(s1.union(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
u = s1.union(s2).union(s3).union(s4)
print(u)
u = s1.union(s2, s3, s4)
print(u)
u = [*s1, *s2, *s3, *s4]
print(u)
u = {*s1, *s2, *s3, *s4}

## dictionaries
d1 = {'key1':1, 'key2':2}
d2 = {'key2':3, 'key4':4}
### only keys, ad duplicated removed
print({*d1, *d2})
### works well
### key2 of d2 overwrite key2 of d1
print({**d1, **d2})

### also unpack into another dictionary
d3 = {'a': 1, 'b': 2, **d1, 'c': 3}
print(d3)

## neosted unpacking
a, b, c = [1, 2, 'XY']
print(a, b, c)

a, b, (c, d) = [1, 2, 'XY']
print(a, b, c, d)

a, b, (c, d, *e) = [1, 2, 'python']
print(a, b, c, d, e)

### same with slicing
l = [1, 2, 3, 4, 'python']

a, *b, (c, d, *e) = l
print(a, b, c, d, e)
print(l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:]))

l = (1, 2, 3, 4, ['a', 'b', 'c', 'd'])
a, b, c, d, e = l[0], list(l[1:-1]), l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)


######################################################
# *args
# scoop up as tuple, remaining of positional arguments
######################################################

## * return a tuple not a list
## args parameter is a name conventions
## it can have any other name
def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

## * args is also optional
func1(10, 20)
## can pass lot of arguments
func1(10, 20, 30, 40, 50)

## if user must insert at least one parameter use:
## def avg(a, *args):
## else
def avg(*args):
    count = len(args)
    total = sum(args)

    #if count == 0:
    #    return 0
    #else:
    #    return count and total / count

    ## short circuiting, shortest and more readable solution
    return count and total / count

print(avg())
print(avg(2,2,4,4))

## unpack on argumnet passing
def func2(a, b, c):
    print(a)
    print(b)
    print(c)

### element number bust be the same of parameter
l = [10, 20, 30]
func2(*l)

### passing a list of unknown length
def func3(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 50, 60, 70, 80]
func3(*l)


###################
# keyword arguments
###################

def func4(a, b, c):
    print(a, b, c)

func4(1, 2, 3)
func4(1, c=3, b=2)

## here d is mandatory keyword parameter
## *args define the end of positional parameters and
## return a tuple with passed arguments
def func5(a, b, *args, d):
    print(a, b, args, d)

## return: TypeError: func5() missing 1 required keyword-only argument: 'd' 
## func5(1, 2, 3, 4, 5)
func5(1, 2, 3, 4, d=5)

## same thing
def func6(*args, d):
    print(args, d)

func6(1, 2, 3, 4, d=5)

## no positional arguments allowed
## * indicates the end of positional parameters
def func7(*, d):
    print(d)

### doesn't work, wrong
#func7(5)
#func7(5, d=4)
func7(d=4)

## positional parameters, max 2 and after a named parameter
def func8(a, b, *, d):
    print(a, b, d)

### doesn't work, wrong
#func8(1, 2, 3, d=4)
#func8(1, 2, 4)
func8(1, 2, d=4)

## positional parameters with default value
def func9(a, b=2, *args, d):
    print(a, b, args, d)

func9(1, 5, 7, 8, d=10)
### parameter b now have default value
func9(1, d=10)

## positional parameters with default value for keyword parameter
def func10(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)

func10(5, 4, 3, 2, 1, e='go')
func10(5, 4, 3, 2, 1, d='lets', e='go')


#######################################################################
# **kwargs
# scoop up as dictionary, remaining of keyword arguments
# can be specified even if positional arguments have not benn exhausted
# no parameters after
#######################################################################

def func11(**kwargs):
    print(kwargs)

func11(a='pippo', b=0, c=1.1)

## combining with *args
def func12(*args, **kwargs):
    print(args)
    print(kwargs)

func12(1, 2, a=3, b=4)

## with positional parameters
def func13(a, b, **kwargs):
    print(a,b)
    print(kwargs)

func13(1, 2, x=3, y=4)

## after named parameter
#def func13(a, b, *, **kwargs): # not allowed because only named arguments must follow the *
def func14(a, b, *, d, **kwargs):
    print(a,b)
    print(d)
    print(kwargs)

func14(1, 2, d=23, x=3, y=4)


######################
# putting all togheter
######################

## two positional parameters a and b
def p_func_0(a, b):
    pass

## two positional parameters a and b, b has default value and this make it optional
def p_func_1(a, b=10):
    pass

## two positional parameters a and b plus the positional parameters' collector *args
def p_func_2(a, b, *args):
    pass

## two positional parameters a and b, positional parameters' collector *args,
## keyword parameters kw1 and kw2, kw2 is optional, kw1 mandatory
def p_func_3(a, b, *args, kw1, kw2=100):
    pass

## two positional parameters a and b, positional parameters' end sign *,
## keyword parameters kw1 and kw2, kw2 is optional, kw1 mandatory
def p_func_4(a, b, *, kw1, kw2=100):
    pass

## two positional parameters a and b, positional parameters' collector *args,
## keyword parameters kw1 and kw2, kw2 is optional, kw1 mandatory
## keyword parameters' collector **kwargs
def p_func_5(a, b, *args, kw1, kw2=100, **kwargs):
    pass

## two positional parameters a and b, positional parameters' end sign *,
## keyword parameters kw1 and kw2, kw2 is optional, kw1 mandatory
## keyword parameters' collector **kwargs
def p_func_6(a, b, *, kw1, kw2=100, **kwargs):
    pass

## only positional parameters' collector
def p_func_7(*args):
    pass

## only keyword parameters' collector
def p_func_8(**kwargs):
    pass

## positional parameters' collector and keyword parameters' collector
## accept arbitray number of both parameters' type
def p_func_9(*args, **kwargs):
    pass
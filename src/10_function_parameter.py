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


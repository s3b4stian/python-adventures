###########################################
# docstrings and annotations
# PEP 257
# https://www.python.org/dev/peps/pep-0257/
###########################################

## if the first line of a function is a string, only a string is a docstring
## docstring are not comments

## single line docstring
def my_func_0(a, b=1):
    "returns a * b"
    return a * b

#help(my_func_0)

## multi line docstring
def my_func_1(a, b=1):
    """returns a * b
    
    Some additional information about
    this function    
    """
    return a * b

#help(my_func_1)

## docstring storage dunder property
print(my_func_0.__doc__)
print(my_func_1.__doc__)

## annotations
def my_func_3(a: 'annotation for a', b: 'annotation for b' = 1) -> 'something long annotation':
    "returns a * b"
    return a * b

### annotation in funcion header
##help(my_func_3)

## annotation storage dunder property
print(my_func_3.__annotations__)

## pay attention
x = 3
y = 5
def my_func_4(a: 'some character') -> 'charaqcted a repeated ' + str(max(x,y)) + ' times':
    return a * max(x, y)

### annotation calulated ad parssing time, creation time
print(my_func_4.__annotations__)

x = 3
y = 8

### annotation doesn't change
print(my_func_4.__annotations__)


####################
# lambda expressions
####################

def regular_func(x):
    return x**2

print(type(regular_func))

## it is the same as regular_func
my_var_0 = lambda x: x ** 2

print(type(my_var_0))

other_var = my_var_0

print(my_var_0)
print(other_var)
print(my_var_0(2))
print(other_var(2))

print(id(my_var_0), id(other_var))

## more than one 
my_var_1 = lambda x, y: x + y

## more than one with default
my_var_2 = lambda x, y=10: x + y

print(my_var_1(2,2))
print(my_var_2(2))

## other parameters
## like other function
my_var_3 = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

print(my_var_3(1, 'a', 'b', y=100, kw1=1, kw2=2))

## as argument of function
def apply_func(x, fn):
    return fn(x)

print(apply_func(3, my_var_0))
print(apply_func(25, my_var_0))

print(apply_func(3, lambda x: x**2))
print(apply_func(25, lambda x: x**2))

print(apply_func(3, lambda x: x**3))

## as argument of function, arbitraty arguments
def apply_func_generic(fn, *args, **kwargs):
    ## argument unpacking
    return fn(*args, **kwargs)

print(apply_func_generic(my_var_0, 3))
print(apply_func_generic(my_var_0, 25))

print(apply_func_generic(lambda x: x**2, 3))
print(apply_func_generic(lambda x: x**2, 25))

print(apply_func_generic(lambda x, y: x+y, 3, 5))

print(apply_func_generic(lambda x, *, y: x+y, 3, y=5))
print(apply_func_generic(lambda *args: sum(args), 2, 3, 5, 10, 80))
## equivalent to
print(apply_func_generic(sum, (2, 3, 5, 10, 80)))

## lambda and sorting
l = [1, 5, 4, 10, 9, 6]
print(l, sorted(l))

l = ['c', 'B', 'D', 'a']
print(l, sorted(l))
### change sort method
print(l, sorted(l, key=lambda s: s.upper()))

d = {"def": 200, "abc": 300 ,"ghi": 100}

for e in d:
    print(e)

### sorted by key
print(d, sorted(d))
### sorted by value
print(d, sorted(d, key=lambda e: d[e]))

def dist_sq(x):
    return (x.real) ** 2 + (x.imag) ** 2

print(dist_sq(1+1j))

l = [3+3j, 1-1j, 0, 3+0j]
### sorted doesn't have builtin function for complex nu mber
print(l, sorted(l, key=dist_sq))
print(l, sorted(l, key=lambda x: (x.real) ** 2 + (x.imag) ** 2))

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(l, sorted(l))
### sort for last character
### for equal chars original order is preserved
print(l, sorted(l, key=lambda s: s[-1]))

## challenge
## randomize an Iterable using sorted
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## like a shuffle
print(l, sorted(l, key=lambda x: random.random()))
print(l, sorted(l, key=lambda x: random.random()))
print(l, sorted(l, key=lambda x: random.random()))
print(l, sorted(l, key=lambda x: random.random()))


########################
# function introspection
########################
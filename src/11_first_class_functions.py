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

# dummy code
i = 100

# TODO: fix this function
# really useless function
def my_func_5(a: "mandatory positional", 
            b: "optional positonal" = 1, 
            c=2, 
            *args: "add extra positional here", 
            kw1, 
            kw2=100, 
            kw3=200, 
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """This function does nothing but 
    accept lot of garbage
    """
    i = 10
    j = 20
    a = i + j
    return a

## show docstring
print(my_func_5.__doc__)
## show information about parameter
print(my_func_5.__annotations__)

## functions is a object with properties
my_func_5.short_description = "this is a fcuntion that does nothing much"
print(my_func_5.short_description)

## show all methods and properties
print(dir(my_func_5))
print(my_func_5.__name__)

## example
def func_call(f):
    print(id(f), f.__name__)

func_call(my_func_5)

## default parameter values
print(my_func_5.__defaults__)
print(my_func_5.__kwdefaults__)

## code attribute
## look to the funciton source code at runtime
print(dir(my_func_5.__code__))

print(my_func_5.__code__.co_varnames)
## pay attention, it show only positional arguments without default values
print(my_func_5.__code__.co_argcount)

## inspect module
import inspect
from inspect import isfunction, ismethod, isroutine

a = 10

class MyClass:
    def f(self):
        pass

my_obj = MyClass()

print("Function")
print("a", isfunction(a))         # variable
print("my_func_5", isfunction(my_func_5)) # function
print("MyClass", isfunction(MyClass))   # class
print("my_obj", isfunction(my_obj))    # object
print("my_obj.f", isfunction(my_obj.f))  # object method

print("Method")
print("a", ismethod(a))         # variable
print("my_func_5", ismethod(my_func_5)) # function
print("MyClass", ismethod(MyClass))   # class
print("my_obj", ismethod(my_obj))    # object
print("my_obj.f", ismethod(my_obj.f))  # object method

print("Routine")
print("a", isroutine(a))         # variable
print("my_func_5", isroutine(my_func_5)) # function
print("MyClass", isroutine(MyClass))   # class
print("my_obj", isroutine(my_obj))    # object
print("my_obj.f", isroutine(my_obj.f))  # object method

## show the source code
print(inspect.getsource(my_func_5))

## show where objects live
print(inspect.getmodule(my_func_5))
print(inspect.getmodule(print))

## show comments
print(inspect.getcomments(my_func_5))

## signature of the function
## return an object
print(inspect.signature(my_func_5))

print(my_func_5.__annotations__)
print(inspect.signature(my_func_5).return_annotation)

sig = inspect.signature(my_func_5)
print(sig.parameters)

## example,. show all parameter with signature
for k, param in sig.parameters.items():
    ## param is an object
    #print(f"Key: \t\t{k}")
    print(f"Name: \t\t{param.name}")
    print(f"Default: \t{param.default}")
    print(f"Annotation: \t{param.annotation}")
    print(f"Kind: \t\t{param.kind}")
    print("--------------------------------")


###########
# callables
###########

## object that can be called using round brackets operator ()
## every callable return a value

print(callable(print)) # true

l = [1, 2, 3]
print(callable(l.append)) # true

result = l.append(4)
print(result) # None

s = 'abc'
print(callable(s.upper)) # true
print(callable(s.upper())) # false

## classes
from decimal import Decimal

print(callable(Decimal)) # true

### object not callable
### some objects are callable
a = Decimal('10.5')
print(callable(a)) # false

## objects
class MyClass1:
    def __init__(self, x=0):
        print("initializing...")
        self.counter = x

print(callable(MyClass1)) # true

a = MyClass1(100)
print(callable(a)) # false

class MyClass2:
    def __init__(self, x=0):
        print("initializing...")
        self.counter = x
    
    def __call__(self, x=1):
        print("updating counter...")
        self.counter += x

print(callable(MyClass2)) # true

## callable instance
a = MyClass2(100)
a()
print(a.counter) # 101
### equal to
MyClass2.__call__(a)
print(a.counter) # 102

print(callable(a)) # false


#########################################
# map, filter, zip and list comprehension
#########################################

## map
def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(3))
print(fact(6))
### don't return list or tuple, return generator
result = list(map(fact, [1, 2, 3, 4, 5, 6]))
print(result)

## map with more than one list
l1 = [1,2,3,4,5]
l2 = [10, 20, 30]
l3 = (100, 200, 300, 400)

result = list(map(lambda x, y: x+y, l1, l2))
print(result)

result = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(result)

### return error
### func with 2 positional args but 3 iterables provided
#result = list(map(lambda x, y: x+y, l1, l2, l3))

## filter
x = range(25)
print(x)

for i in x:
    print(i)

print(list(filter(lambda x: x % 3 == 0, range(25))))

### test only for truthness
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))

## zip
l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'

### return a generator
result = zip(l1, l2, l3)

for x in result:
    print(x)

### reusable
result = list(zip(l1, l2, l3))

### shortest
print(list(zip(range(10000), 'python')))

l = range(10)

print(list(l))

## factorial with comprehension
result = list(map(fact, l))
print(result)

### list comprehension
result = [fact(n) for n in range(10)]
print(result)

### generator object, one shot
result = (fact(n) for n in range(10))
for x in result:
    print(x)

## same result with map and zip
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

result = list(map(lambda x, y: x+y, l1, l2))
print(result)

result = [x+y for x, y in zip(l1, l2)]
print(result)

## filter with map
result = list(filter(lambda x: x % 2 == 0, map(lambda x, y: x+y, l1, l2)))
print(result)

## same filter with comprehension and zip
result = [x+y for x, y in zip(l1, l2) if (x+y) % 2 == 0]
print(result)


####################
# reducing functions
####################

## our reduce function
l = [5, 8, 6, 10, 9]

## reducing condition
_max = lambda x, y: x if x > y else y

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

_min = lambda x, y: x if x < y else y

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(min_sequence(l))

_add = lambda x, y: x + y

def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

print(add_sequence(l))

## generic reduction function
## works only with sequences that support indexing
def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print("-----")
print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))

## built in recude function
from functools import reduce

print("-----")
print(reduce(_max, l))
print(reduce(_min, l))
print(reduce(_add, l))

print("-----")
print(reduce(_max, [5, 8, 6, 10, 9])) # list, indexable
print(reduce(_min, (5, 8, 6, 10, 9))) # tuple, indexable
print(reduce(_add, {5, 8, 6, 10, 9})) # set, not indexable, also works well

## built functions
## also it supports indexable elements
print("-----")
print(min(l))
print(max(l))
print(sum(l))
print(any(l))
print(all(l))

### any and all
### any return true if at leat one element is true, like or
### all return true if all alements are true, like and

## all and any equivalent with reduce

s1 = {10, 20, 30, 'a', 'b'}
s2 = {10, 20, False, 'a', 'b'}
s3 = {False, 0, '', None}

### all like behavior
print("-----")
print(reduce(lambda a, b: bool(a) and bool(b), s1))
print(reduce(lambda a, b: bool(a) and bool(b), s2))
print(reduce(lambda a, b: bool(a) and bool(b), s3))
### any like behavior
print("-----")
print(reduce(lambda a, b: bool(a) or bool(b), s1))
print(reduce(lambda a, b: bool(a) or bool(b), s2))
print(reduce(lambda a, b: bool(a) or bool(b), s3))

## product of values
## factorial function
## 4! = 4 * 3 * 2 * 1
l = [1, 2, 3, 4]
print(reduce(lambda a, b: a * b, l))

print(reduce(lambda a, b: a * b, range(1, 5+1)))

### defined above
### def fact(n):
###     return 1 if n < 2 else n * fact(n-1)

print(fact(4))
print(fact(5))

def fact1(n):
    return reduce(lambda a, b: a * b, range(1, n+1))

print(fact1(4))
print(fact1(5))

## reduce with initializer

def _reduce1(fn, sequence, initial):
    result = initial#sequence[0]
    for x in sequence:
        result = fn(result, x)
    return result

l = [1, 2, 3, 4]
print(_reduce1(_add, l, 0))
print(_reduce1(_add, l, 10))
print(_reduce1(_add, l, 100))

### rewrote with initializer, works also with not indexable sequences
l = {1, 2, 3, 4}
print(_reduce1(_add, l, 0))
print(_reduce1(_add, l, 10))
print(_reduce1(_add, l, 100))


###################
# partial functions
###################

## custom solution
def my_func_6(a, b, c):
    print(a, b, c)

my_func_6(10, 20, 30)

### reduction of my_func_6
def f(x, y):
    return my_func_6(5, x, y)

f(50, 500)

f1 = lambda x, y: my_func_6(10, x, y)
f1(100, 1000)

## built in partial function
from functools import partial

f2 = partial(my_func_6, 20)
f2(200, 2000)

### it is possible reduce more than one patameter
### if f3 is called with more than one parameter, python return a type error
### my_func_6 has originally three parameters
f3 = partial(my_func_6, 30, 300)
f3(3000)

## reduction with various parameter
def my_func_7(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

my_func_7(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

def f7_reduction(x, *vargs, kw, **kwvargs):
    return my_func_7(10, x, *vargs, k1='a', k2=kw, **kwvargs)

f7_reduction(20, 100, 200, kw='b', k3=1000, k4=2000) # same output of my_func_7

f4 = partial(my_func_7, 10, k1='a')
f4(20, 100, 200, k2='b', k3=1000, k4=2000) # same output of my_func_7

## specific the parameter for reduction
def pow(base, exponent):
    return base**exponent

sq = partial(pow, exponent=2)
print(sq(5))

cu = partial(pow, exponent=3)
print(cu(5))
print(cu(base=5))
print(cu(5, exponent=2)) # works but bad practice

## variable usage, be carefull
a = 2
sq = partial(pow, exponent=a)
print(sq(5)) # 25

a = 3
print(sq(5)) # expected 125 but 25 returned
### this happens because partial take the reference to the object
### assign another value to a create another object in memory

def my_func_8(a, b):
    print(a, b)

a = [1, 2]
f5 = partial(my_func_8, a)
f5(100) # [1, 2] 100

a.append(3)
f5(100) # [1, 2, 3] 100
### it is only mutate the internal state of the same object, reference to list
### is the same

## applications examples

### distance between two points
origin = (0,0)
l = [(1,1), (0,2), (-3,2), (0,0), (10,10)]

dist2 = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
print(dist2((1,1), origin)) # 2

print(sorted(l)) # doesn't work well

dist_from_origin = partial(dist2, origin)
print(dist_from_origin((1,1))) # 2
print(sorted(l, key=dist_from_origin)) # works well

### another method

dist_from_origin = lambda x: dist2(origin, x) # reduciton
print(sorted(l, key=dist_from_origin)) # also works well

### or
print(sorted(l, key=lambda x: dist2(origin, x))) # also works well

### or
print(sorted(l, key=partial(dist2, origin))) # also works well


########################
# the operator module
# operators as functions
########################


#########################
# global and local scopes
#########################

## global scope is the module scope
## exception to this are the built-in objects like, True, False, None etc..

## variabl ein global scope
a = 10
print(a)

def my_func_0(n):
    ## c local
    c = n ** 2
    return c

def my_func_1(n):
    ## retrieve global a because
    ## there isn't an assignement
    ## inside function
    print(f"global a: {a}")

my_func_1(1)


def my_func_2(n):
    ## this also works because there isn't an
    ## assigment, python search a value in global scope
    print(f"global a: {a}")
    c = a ** n
    return c

print(my_func_2(2))

def my_func_3(n):
    ## local assignement
    ## a will be solved in local scope
    a = 20
    c = a ** n
    return c

print(my_func_3(2))

def my_func_4(n):
    ## a declared global
    ## value changed for the variable a in the global scope
    global a
    a = 20
    c = a ** n
    return c

print(a)
print(my_func_4(2))
print(a)

def my_func_5():
    global var
    var = "hello word"
    return

## result in an error
## because var isn't declared in global scope
#print(var)
my_func_5()
print(var)
## after function call, var exists in global scope
## no error returned

def my_func_6():
    ## this doesn't work because python
    ## find the assignement to var a
    ## and create a local a
    print(f"global a: {a}")
    a = 'hello'
    print(a)
    return

try:
    my_func_6()
except UnboundLocalError as e:
    print(f"error: {e}")

## reusing built in names

def print(x):
    return f"hello {x}"

try:
    ## prind will be resolved in global scope instead of built in scope
    print('word') ## return hello word as programmer defined
    print('word', 1) ## programmer defined
except TypeError as e:
    ## delete global scope programmer defined print
    del print
    ## built in print function
    print(f"error: {e}")


##################
# non local scopes
##################

## functions inside other funcitons
## and non local keyword

def outer_func_0():
    x = "hello"

    def inner_function():
        ## x of the outer_func_0 scope
        print(f"inner: {x}")

    inner_function()

outer_func_0()

def outer_func_1():
    x = "hello"

    def inner_function_1():
        def inner_function_2():
            ## x of the outer_func_1 scope
            print(f"inner: {x}")
        inner_function_2()
    inner_function_1()

outer_func_1()

## python search ultil it finds the
## first declation of the required variable
def outer_func_3():
    x = "hello"

    def inner_function():
        x = "python"
        ## x of the inner_function scope
        ## python resolve local because there is an assigment
        print(f"inner: {x}")

    inner_function()
    ## x of the outer_func_3
    print(f"outer_3: {x}")

outer_func_3()

def outer_func_4():
    x = "hello"

    def inner_function():
        ## tell python that x is from the above scope
        ## outer_func_4 scope
        nonlocal x 
        x = "python"
        ## x of the outer_function scope
        ## python resolve outer because there is non local declaration
        print(f"inner: {x}") # python

    print(f"outer_4 before: {x}") # hello
    inner_function()
    ## x of the outer_func_4
    print(f"outer_4 after: {x}") # python

outer_func_4()

def outer_func_5():
    x = "hello"

    def inner_function_1():
        def inner_function_2():
            nonlocal x 
            ## modify the x of outer_func_5 scope
            x = "python"

        inner_function_2()

    inner_function_1()
    ## x of the outer_func_4
    print(f"outer_5: {x}") # python

outer_func_5()


## nonlocal chain until outer funciton scope
def outer_func_6():
    x = "hello"

    def inner_function_1():
        nonlocal x
        ## modify the x of outer_func_5 scope
        x = "python"
        def inner_function_2():
            nonlocal x 
            ## modify the x of outer_func_5 scope
            x = "monty"

        inner_function_2()

    inner_function_1()
    ## x of the outer_func_4
    print(f"outer_6: {x}") # python

outer_func_6()

## global x
x = "python"

def outer_func_7():
    ## this make python unable to find x inside function
    ## if there is nonlocal inside inner function
    global x
    x = "monty"

    def inner_function_1():
        ## python check upper scope for variable x
        ## but it doesn't find any x variable because
        ## x is global
        ## declare x nonlocal in this case raise an SyntaxError
        
        ## non local commented to avid errors
        #nonlocal x
        x = "hello"
        print(f"inner: {x}") # hello
    
    inner_function_1()
    print(f"outer_7: {x}") # monty

outer_func_7()


##########
# closures
##########

## in this case, x in local scope and x
## in inner function poits to a cell
## python the function return inner, return also x
## x is called technically freevar
def closure_func_0():
    
    x = "python"
    def inner():
        print(f"inner: {x}") 
    
    return inner

fn = closure_func_0()
print(fn.__code__.co_freevars)
print(fn.__closure__)

def closure_func_1():
    
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    
    return inner

## equal reference
fn = closure_func_1()
print(fn.__code__.co_freevars)
print(fn.__closure__)
fn()

## closuire example
def closure_func_2():
    count = 0

    def inner():
        ## count refer to count var in the closure_func_2 scope
        nonlocal count
        count += 1
        return count
    return inner

## the id of the object pointed from the cell
## change every time the function is called
## because int is an immutable object
fn = closure_func_2()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(fn())
print(fn.__closure__)
print(fn())
print(fn.__closure__)
print(fn())
print(fn.__closure__)
print(fn())
print(fn.__closure__)

## closure in same scope that reference the same variable
def closure_func_3():
    count = 0

    ## inner1 and inner2 internal count var
    ## point to count var in closure_func_3 scope
    def inner1():
        nonlocal count
        count += 1
        return count

    def inner2():
        nonlocal count
        count += 1
        return count

    ## return a tuple of function
    return inner1, inner2

fn1, fn2 = closure_func_3()
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
## cell point to same object
print(fn1.__closure__)
print(fn2.__closure__)
print(fn1())
#print(fn2())
## cell point to same object
## but the object id changed
print(fn1.__closure__)
print(fn2.__closure__)
print(fn2())
## cell point to same object
## but the object id changed
## one more time
print(fn1.__closure__)
print(fn2.__closure__)

## closure in different scopes
def closure_func_4(n):
    def inner(x):
        ## n var point to closure_func_4 scope
        return x ** n
    
    ## return a tuple of function
    return inner

square = closure_func_4(2) ## square
cube = closure_func_4(3) ## cube
print(square.__code__.co_freevars)
print(square.__closure__)
print(cube.__code__.co_freevars)
print(cube.__closure__)

print(square(2))
print(cube(2))

## caveats
## adder function, correct and working
def closure_func_5(n):
    def inner(x):
        return x + n
    return inner

## different scopes
## different cell
add_1 = closure_func_5(1)
add_2 = closure_func_5(2)
add_3 = closure_func_5(3)

print(add_1.__closure__)
print(add_2.__closure__)
print(add_3.__closure__)
print(add_1(10))
print(add_2(10))
print(add_3(10))

## adder function, bad and wrong
adders = []
for n in range(1,4):
    ## n is the n of the for cicle
    adders.append(lambda x: x + n)
print(n) # global n
print(adders)

## don't have a closure here
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))

## now it is a closure
## return a list of closures
def closure_func_6():
    adders = []
    for n in range(1,4):
        ## n is the n of the for cicle
        adders.append(lambda x: x + n)
    return adders

adders = closure_func_6()
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
## the value is the same because all closures point the same object
## there is a bug :)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))

## return a list of functions
## not closures
## and it works
def closure_func_7():
    adders = []
    for n in range(1,4):
        ## n is the n of the for cicle
        ## cosure doesn't exist because in the body of the lamba
        ## there isn't a var of the upper local scope
        adders.append(lambda x, y = n: x + y)
    return adders

adders = closure_func_7()
## closures don't exist
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))


######################
# closure applications
######################

## first solution, class averager
## every time need to calculate the total and the count
class Averager_0:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager_0()
print(a.add(10))
print(a.add(20))
print(a.add(30))

## second solution, using closures
def averager_0():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    
    return add

a = averager_0()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(30))

## third solution, using closures
## optmizing, instead of storing numbers and recalculate all every time
## the function store the total and the count
def averager_1():
    total = 0
    count = 0
    def add(number):
        ## mandatory because there is an assignement
        nonlocal total, count
        total = total + number
        count = count + 1
        return total / count
    
    return add

a = averager_1()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(30))

## fourt solution
## optimizing the class
class Averager_1:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

a = Averager_1()
print(a.add(10))
print(a.add(20))
print(a.add(30))

## another example with timer
from time import perf_counter

## first solution, class timer
class Timer_0:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer_0()
print(t1())
print(t1())

## second solution, using closures
def timer_0():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    
    return poll

t1 = timer_0()
print(t1())
print(t1())

## another example with counter

## first solution
## this function is a closure because in function is referrencing
## variable initial_value of the upper local scope
def counter_0(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter0 = counter_0()
print(counter0())
print(counter0())
print(counter0())
print(counter0())

## second solution, function counter
def counter_1(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"{fn.__name__} has been called {cnt} times")
        return fn(*args, **kwargs)
    return inner

def add_c(a, b):
    return a + b

def mul_c(a, b):
    return a * b

counter_add = counter_1(add_c)
print(counter_add.__closure__)
print(counter_add(10, 20))
print(counter_add(20, 20))

counter_mul = counter_1(mul_c)
print(counter_mul.__closure__)
print(counter_mul(10, 20))
print(counter_mul(20, 20))

## third solution, function counter with global counters
counters = dict()

def counter_2(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        ## global variable, but global declaration no needed because
        ## there isn't an assignement
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counter_add = counter_2(add_c)
counter_add(10, 20)
counter_add(20, 20)

counter_mul = counter_2(mul_c)
counter_mul(10, 20)
counter_mul(20, 20)

print(counters)

## fourt solution, function counter with global counters

def counter_3(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        ## free variable, but nonlocal declaration no needed because
        ## there isn't an assignement
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

c = dict()

counter_add = counter_3(add_c, c)
print(counter_add(10, 20))
print(counter_add(20, 20))
print(counter_add(30, 20))

counter_mul = counter_3(mul_c, c)
print(counter_mul(10, 20))
print(counter_mul(20, 20))

print(c)

## another example with factorial function

def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

counter_fact = counter_3(fact, c)
print(counter_fact(1))
print(counter_fact(2))
print(counter_fact(3))
print(counter_fact(4))
print(counter_fact(5))

print(c)


###################
# decorators part 1
###################

## in general decorator
## - takes a function as argument
## - return a closure
## - the closure accepts any combination of parameters
## - run some code in the inner function
## - the closure function calls the original function using the arguments passed to the closure

def counter_decorator_0(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"{fn.__name__} id({id(fn)}) has been called {cnt} times")
        return fn(*args, **kwargs)
    return inner

def add_decorated(a: int, b: int):
    """
    adds two values
    """
    return a + b

## decorator work like this
add_decorated = counter_decorator_0(add_decorated)
add_decorated(10,20)
add_decorated(20,30)
add_decorated(40,50)

@counter_decorator_0
def mul_decorated(a: int, b: int):
    """
    multiplicates two values
    """
    return a * b

## decorated during definition using @ simbol
## it works like add decorated example
mul_decorated(10, 1)
mul_decorated(10, 2)
mul_decorated(10, 3)

## function mul_decorated took the name of the closure, inner
## and lose the the docstring
print(mul_decorated.__name__)
print(mul_decorated.__doc__)


## method to preserve the name of the function and the docstring
def counter_decorator_1(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"{fn.__name__} id({id(fn)}) has been called {cnt} times")
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return fn(*args, **kwargs)
    return inner

@counter_decorator_1
def mul_decorated_1(a: int, b: int):
    """
    multiplicates two values
    """
    return a * b

mul_decorated_1(10, 1)
mul_decorated_1(10, 2)
mul_decorated_1(10, 3)

## now works well, it is possible to see the name of mul_decorated_1
## and it docstring, but the signature of the function isn't still correct yet
#help(mul_decorated_1)
print(mul_decorated_1.__name__)
print(mul_decorated_1.__doc__)

## there is another way to solve
from functools import wraps

def counter_decorator_2(fn):
    cnt = 0
    ## decorate our closure with functool utility
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"{fn.__name__} id({id(fn)}) has been called {cnt} times")
        ## or, and it is the same 
        # inner = wraps(fn)(inner)
        return fn(*args, **kwargs)
    return inner

@counter_decorator_2
def mul_decorated_2(a: int, b: int):
    """
    multiplicates two values
    """
    return a * b

mul_decorated_2(10, 1)
mul_decorated_2(10, 2)
mul_decorated_2(10, 3)

## now all works well
#help(mul_decorated_2)
print(mul_decorated_2.__name__)
print(mul_decorated_2.__doc__)


#################################
# decorator application -> timing
#################################

def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        ## start timing
        start = perf_counter()
        ## run the passed function
        result = fn(*args, **kwargs)
        ## stop timing
        end = perf_counter()
        ## rnu time
        elapsed = end - start

        ## collect positional arguments
        args_ = [str(a) for a in args] ## list comprehension
        ## collect keyword arguments
        kwargs_ = [f"{k}={v}" for (k,v) in kwargs.items()]
        ## merge arguments
        all_args = args_ + kwargs_
        ## to string
        args_str = ','.join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run")

        return result

    ## return decorated function
    return inner

## function that calculate fibonacci number
## decorator target

### recursive mode
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

### print(fibonacci_recursive(6))

### for avoid timing of every recursive call
### need to creare a wrapper
@timed
def fibonacci_recursive_wrapper(n):
    return fibonacci_recursive(n)

print(fibonacci_recursive_wrapper(6))
print(fibonacci_recursive_wrapper(20))
print(fibonacci_recursive_wrapper(25))
print(fibonacci_recursive_wrapper(30))
#print(fibonacci_recursive_wrapper(35))

### loop mode
@timed
def fibonacci_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        ## equal to
        ## tmp = fib_2
        ## fib_2 = fib_1 + fib_2
        ## fib_1 = tmp
        ## this is python :)
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2
    
print(fibonacci_loop(6))
print(fibonacci_loop(20))
print(fibonacci_loop(25))
print(fibonacci_loop(35))

### reduce mode
### n = 1
### (1,0) --> (1,1) --> result t[0] = 1
### n = 2
### (1,0) --> (1,1) --> (2,1) --> result t[0] = 2
### n = 3
### (1,0) --> (1,1) --> (2,1) --> (3,2) --> result t[0] = 3
### n = 4
### (1,0) --> (1,1) --> (2,1) --> (3,2) --> (5,3) --> result t[0] = 5
### first element of every tuple is the sum of previous tuple
### second element of every tuple is the first element of previous tuple
from functools import reduce
@timed
def fibonacci_reduce(n):
    initial = (1,0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n[0]

print(fibonacci_reduce(6))
print(fibonacci_reduce(20))
print(fibonacci_reduce(25))
print(fibonacci_reduce(30))
print(fibonacci_reduce(35))


#####################################################
# decorator application -> logger, stacked decorators
#####################################################

## simple loggin decorator
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        return result
    return inner

@logged
def func_logged_1():
    pass

@logged
def func_logged_2():
    pass

@logged
def func_logged_3():
    pass

@logged
def func_logged_4():
    pass

func_logged_1()
func_logged_2()
func_logged_3()
func_logged_4()

## another timed decorator
def timed_2(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        ## start timing
        start = perf_counter()
        ## run the passed function
        result = fn(*args, **kwargs)
        ## stop timing
        end = perf_counter()
        ## rnu time
        elapsed = end - start

        ## collect positional arguments
        args_ = [str(a) for a in args] ## list comprehension
        ## collect keyword arguments
        kwargs_ = [f"{k}={v}" for (k,v) in kwargs.items()]
        ## merge arguments
        all_args = args_ + kwargs_
        ## to string
        args_str = ','.join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run")

        return result

    ## return decorated function
    return inner

@logged
@timed
def fact_1(n):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n+1))

fact_1(5)

## previous decoration is equal to
## fact_1 = logged(timed(fact_1))
## stacked decorator

### printing then call the function
def decorator_1(fn):
    def inner():
        print("Running decorator 1")
        return fn()
    return inner

def decorator_2(fn):
    def inner():
        print("Running decorator 2")
        return fn()
    return inner

@decorator_1
@decorator_2
def dec_func_0():
    print("Running dec_func")

dec_func_0()

### call the function then printing
def decorator_3(fn):
    def inner():
        result = fn()
        print("Running decorator 3")
        return result
    return inner

def decorator_4(fn):
    def inner():
        result = fn()
        print("Running decorator 4")
        return result
    return inner

@decorator_3
@decorator_4
def dec_func_1():
    print("Running dec_func")

dec_func_1()


######################################
# decorator application -> memoization
######################################

## a very inefficent solution
def fibonacci(n):
    print(f"Calculating fibonacci({n})")
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

## a more efficent solution
class Fib:
    def __init__(self):
        self.cache = {1:1, 2:1}

    def fib(self, n):
        if n not in self.cache:
            print(f"Calculating fib({n})")
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
print(f.fib(10))

## solution with closure
def fib_closure():
    cache = {1:1, 2:1}
    def calc_fib(n):
        if n not in cache:
            print(f"Calculating calc_fib({n})")
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

f = fib_closure()
print(f(10))

## rewrite as decorator
def fib_memoization(fib):
    cache = {1:1, 2:1}
    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    return inner

@fib_memoization
def fibonacci_dec(n):
    print(f"Calculating fibonacci_dec({n})")
    return 1 if n < 3 else fibonacci_dec(n-1) + fibonacci_dec(n-2)

print(fibonacci_dec(10))

## general pattern
def decorator_memoization(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@decorator_memoization
def fibonacci_dec_1(n):
    print(f"Calculating fibonacci_dec_1({n})")
    return 1 if n < 3 else fibonacci_dec_1(n-1) + fibonacci_dec_1(n-2)

## calculate only for the first call
print(fibonacci_dec_1(10))
print(fibonacci_dec_1(10))

@decorator_memoization
def fact_dec(n):
    print(f"Calculating fact_dec({n})")
    return 1 if n < 2 else n * fact_dec(n-1)
## calculate only for the first call
print(fact_dec(10))
print(fact_dec(10))

## built in memoization
## decorator last recently used cache
from functools import lru_cache

@lru_cache(maxsize=8)
def fibonacci_dec_lru(n):
    print(f"Calculating fibonacci_dec_lru({n})")
    return 1 if n < 3 else fibonacci_dec_lru(n-1) + fibonacci_dec_lru(n-2)

print(fibonacci_dec_lru(10))
print(fibonacci_dec_lru(10))
print(fibonacci_dec_lru(12))
print(fibonacci_dec_lru(3))


###################
# decorators part 2
###################

## how to parametrize a decorator
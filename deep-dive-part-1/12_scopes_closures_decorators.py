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
## normal decorator
def timed_1(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f"Run time: {elapsed:.6f}s")
        return result
    return inner


def fibonacci_recursive_1(n):
    #print(f"Calculating fibonacci_recursive_1({n})")
    return 1 if n < 3 else fibonacci_recursive_1(n-1) + fibonacci_recursive_1(n-2)

## using @ notation is equal to do
## fibonacci_recursive_wrapper_1 = timed_1(fibonacci_recursive_wrapper_1)
@timed_1
def fibonacci_recursive_wrapper_1(n):
    return fibonacci_recursive_1(n)

print(fibonacci_recursive_wrapper_1(20))

## timed that runs test n times
def timed_3(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start
        
        average_run_time = total_elapsed / 10
        print(f"Average run time: {average_run_time:.6f}s ({reps} reps)")
        return result

    return inner

## @timed_3
## decorating in this mode doesnt work
## throw a TypeError
def fibonacci_recursive_wrapper_2(n):
    return fibonacci_recursive_1(n)

## must use the other syntax
fibonacci_recursive_wrapper_2 = timed_3(fibonacci_recursive_wrapper_2, 150)
## calc fibonacci of number 10 and test run 15 times
print(fibonacci_recursive_wrapper_2(10))

## for solve previous problem need to create a decorator factory
## general example
def dec_factory():
    print("Running dec_factory")
    def dec(fn):
        print("Running dec")
        def inner(*args, **kwargs):
            print ("Running inner")
            return fn(*args, **kwargs)
        
        return inner
    return dec

def my_func_7():
    print("Running my_func_7")

## create decorator
dec = dec_factory() # running dec factory
## decorate function
my_func_7 = dec(my_func_7)## running dec
## call function
my_func_7() ## running inner and my_func_7

## or with standard syntax
dec = dec_factory()

@dec
def my_func_8():
    print("Running my_func_8")

my_func_8()

## --- IMPORTANT ----
## it is possible call directly the decorator factory
## using the function call operator
## --- IMPORTANT ----

@dec_factory() ## call the factory that return the decorator
def my_func_9():
    print("Running my_func_9")

my_func_9()

## decorating with factory is equal to
def my_func_10():
    print("Running my_func_10")

my_func_10 = dec_factory()(my_func_10)
my_func_10()

## with decorator factory it is possible inject arguments to build
## specific decorator
def timed_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            
            average_run_time = total_elapsed / 10
            print(f"Average run time: {average_run_time:.6f}s ({reps} reps)")
            return result
        return inner
    return timed

@timed_factory(100) ## return a decorator that runs 100 times
def fibonacci_recursive_wrapper_3(n):
    return fibonacci_recursive_1(n)

@timed_factory(1000) ## return a decorator that runs 1000 times
def fibonacci_recursive_wrapper_4(n):
    return fibonacci_recursive_1(n)

@timed_factory(10000) ## return a decorator that runs 10000 times
def fibonacci_recursive_wrapper_5(n):
    return fibonacci_recursive_1(n)

print(fibonacci_recursive_wrapper_3(10))
print(fibonacci_recursive_wrapper_4(10))
print(fibonacci_recursive_wrapper_5(10))


#################
# decorator class
#################

## basic decorator factory
def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print(f"Decorated function called: a={a}, b={b}")
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10,20)
def my_func_11(s):
    print(f"Hello {s}")

my_func_11("Python Decorator")

## decorator as a class
## class is the factory
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f"Decorated function called: a={self.a}, b={self.b}")
            return fn(*args, **kwargs)
        return inner

@MyClass(10,20)
def my_func_12(s):
    print(f"Hello {s}")

my_func_12("Python Class Decorator")


###########################################
# decorator applicaziont -> decorator class
###########################################

from fractions import Fraction

## a stupid example to modify classes at runtime
## monkey patch Fraction class
f = Fraction(2,3)
print(f.denominator)
print(f.numerator)

Fraction.speak = lambda self, message: print(f"Fraction says: {message}")
f.speak("This is a late parrot")

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)
f2 = Fraction(64, 8)

print(f1.is_integral())
print(f2.is_integral())

## decorating franction with function
def decorator_speak(cls):
    cls.speak = lambda self, message: print(f"{self.__class__.__name__} says: {message}")
    return cls

Fraction = decorator_speak(Fraction)

f1 = Fraction(2, 3)
f1.speak("I am decorated by function")

class Person:
    pass

Person = decorator_speak(Person)

p = Person()
p.speak("I am a Person")

from datetime import datetime, timezone

def info(self):
    results = []
    results.append(f"time: {datetime.now(timezone.utc)}")
    results.append(f"class: {self.__class__.__name__}")
    results.append(f"id: {hex(id(self))}")
    for k,v in vars(self).items():
        results.append(f"{k}: {v}")
    return results

def debug_info(cls):
    cls.debug = info
    return cls

## decorate with decorator syntax
@debug_info
class Person_1:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        return f"{self.name} says Hello there!"

p = Person_1('John', 1939)
print(p.debug())

@debug_info
class Automobile:
    def __init__(self, make: str, model: str, year: int, top_speed: int):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0
    
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: int):
        if new_speed > self.top_speed:
            raise ValueError("Speed cannot exeed top_speed.")
        else:
            self._speed = new_speed

favorite = Automobile("Ford", "Model T", 1908, 45)
print(favorite.debug())
favorite.speed = 40
print(favorite.debug())


## decorate a class another example
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x **2 + self.y **2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return False


p1, p2, p3, p4 = Point(2,3), Point(2,3), Point(0,0), Point(10,10)

print(abs(p1))
print(p1 is p2)
print(p2 is p3)
print(p1 == p2)
print(p3 < p1)
print(p4 > p1)
print(p1 < p4)

del Point

## a <= b iff a < b or a == b
## a > b  iff not(a < b) and a != b
## a >= b iff not (a < b) 

## do not considerate this good python, only to explain pourpose
def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not(self == other)
        cls.__ge__ = lambda self, other: not(self < other)
    return cls

@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x **2 + self.y **2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return False

p1, p2, p3, p4 = Point(2,3), Point(2,3), Point(0,0), Point(10,10)

print(abs(p1))
print(p1 is p2)
print(p2 is p3)
print(p1 == p2)
print(p3 < p1)
print(p4 > p1)
print(p1 < p4)
print(p1 <= p4)
print(p4 >= p2)

## it is possible to obtain the same result with
## the functools decorator
## from functools import total_ordering


############################################################
# decorator application -> single dispatch generic functions
############################################################

from html import escape
from decimal import Decimal

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return f"{a}(<i>{str(hex(a))}</i>)"

def html_real(a):
    return f"{round(a):.2f}"

def html_str(s):
    return html_escape(s).replace("\n", "<br />\n")

def html_list(l):
    items = (f"<li>{html_escape(item)}</li>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n<ul>"

def html_dict(d):
    items = (f"<li>{html_escape(k)}={html_escape(v)}</li>" for k, v in d.items())
    return "<ul>\n" + "\n".join(items) + "\n<ul>"

## ex usage
print(html_str("""this is
a multi line string
with special characters: 10 < 100"""))

print(html_int(40))

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set):
        return html_set(arg)
    else:
        return html_escape(arg)

## all works fine
print(htmlize(100))
print(htmlize("""Python
rocks!
"""))
print(htmlize([1,2,3,4,5]))

## but there is a problem if is passed argument like below
print(htmlize(["""Python
Rocks! 0<1
""", (10,20,30), 100]))
## for fix need to call htmlize inside html_list
del html_list
del html_dict

def html_list(l):
    items = (f"<li>{htmlize(item)}</li>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n<ul>"

def html_dict(d):
    items = (f"<li>{html_escape(k)}={htmlize(v)}</li>" for k, v in d.items())
    return "<ul>\n" + "\n".join(items) + "\n<ul>"

def html_set(arg):
    return html_list(arg)

## now should run correctly
print(htmlize(["""Python
Rocks! 0<1
""", (10,20,30), 100]))

print(htmlize({1,2,3}))

## a better apporach to htmlize
del htmlize

def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict
    }

    ## get from registry the key corresponding the type of
    ## the argument, if not found, return object key
    fn = registry.get(type(arg), registry[object])
    return fn(arg)

## all works fine
print(htmlize(100))
print(htmlize("""Python
rocks!
"""))
print(htmlize([1,2,3,4,5]))

## rewrite all in more general term, without hardcoded registry
del htmlize
del html_int
del html_list

## decorator
def singledispatch(fn):
    registry = {}
    ## default function
    registry[object] = fn
    
    ## decorated function
    ## geth te functino from registry and call it
    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    ## decorator factory
    ## use decorator only for populate registry
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    ## return the function in the registry associated to the type
    def dispatch(type_):
        return registry.get(type_, registry[object])

    ## create a new property for the decorated function
    ## assign the function that expand the registry
    decorated.register = register
    
    ## permit the access to the content of the registry
    ## decorated.registry = registry

    ## return the function in the registry associated to the type
    decorated.dispatch = dispatch

    return decorated

## become singledispatch.decorated
## htmlize gain the property register
## that is a function
## htmlize -> singledispatch.decorated
@singledispatch
def htmlize(arg):
    return escape(str(arg))

## become singledispatch.register
## a decorator factory that expand the register
## before return the function
## same to
## html_int = htmlize.register(int)(html_int)
@htmlize.register(int)
def html_int(a):
    return f"{a}(<i>{str(hex(a))}</i>)"

## it is possible stack decorators
## decorator doesnt change the original funciton in this case
@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = (f"<li>{htmlize(item)}</li>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n<ul>"


print(htmlize(100))
print(htmlize([1,2,3]))
print(htmlize((1,2,3)))
#print(htmlize.registry)
print(htmlize.dispatch(int))

## use singledispatch from standard library
## it works well with instances of classes
## pervious exampe works with data types
del singledispatch
del htmlize

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

@singledispatch
def htmlize(arg):
    return escape(str(arg))

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return f"{a}(<i>{str(hex(a))}</i>)"

@htmlize.register(Sequence)
def htmlize_sequence(l):
    items = (f"<li>{htmlize(item)}</li>" for item in l)
    return "<ul>\n" + "\n".join(items) + "\n<ul>"

@htmlize.register(str)
def htmlize_str(s):
    return html_escape(s).replace("\n", "<br />\n")

print(htmlize(10))
print(htmlize(True))
print(htmlize([1,2,3]))
print(htmlize((1,2,3)))
## this is also a sequence, but there is the str type
## registered and python handle it as string
print(htmlize("python"))

@htmlize.register(tuple)
def htmlize_tuple(t):
    items = (escape(str(item)) for item in t)
    return "tuple(" + ", ".join(items) + ")"

## now a tuple use the function writtef specifically 
## to handle the tuple
print(htmlize((1,2,3)))
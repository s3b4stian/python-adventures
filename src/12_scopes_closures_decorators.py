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
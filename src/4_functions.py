###########
# functions
###########

## built in functions
s = [1, 2, 3]
print(len(s))

## user defined functions
def func_1():
    print('function func_1 is running')

func_1()

## user defined functions with arguments
def func_2(a, b):
    return a * b

print(func_2(2, 3))

## user defined functions with arguments with annotation
## annotation is only informational
def func_3(a: int, b: int) -> int:
    return a * b

print(func_3(2, 3))

## lamba functions
lam = lambda x: x ** 2
print(lam(2))

lam = lambda a, b: a ** b
print(lam(2, 3))
#########
# numbers
#########


##########
# integers
##########

## integer object uses 24 bytes for zero value
## value grows with number increase
import sys
import math

print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**64))
print(sys.getsizeof(2**128))

## operators result
print(type(1+1))  #int
print(type(2*3))  #int
print(type(4-10)) #int
print(type(3**6)) #int
print(type(2/3))  #float
print(type(10/2)) #float

## floor method
## the larger integer less than or equal the value
print(math.floor(3.999999))  # 3
print(math.floor(-3.999999)) # 4
print(math.floor(-3.000001)) # 4

## limited precision
print(math.floor(-3.000000000000001)) # 4
print(math.floor(-3.000000000000000001)) # 3

## comparing operator result
def comparing(a, b):
    print(a/b)
    print(a//b)
    print(math.floor(a/b))
    print(math.trunc(a/b))

a = 33
b = 16
comparing(a, b)

a = -33
b = 16
comparing(a, b)

a = -33
b = 16
comparing(a, b)

## mod operator
## a = b * (a//b) + (a%b)
def mod_operator(a, b):
    print(f"{a} / {b} = {a/b}")   # division
    print(f"{a} // {b} = {a//b}") # floor division that is: a // b == floor(a / b)
    print(f"{a} % {b} = {a%b}")   # modulus
    print(a == b * (a//b) + (a%b))

a = 13
b = 4
mod_operator(a,b)

a = -13
b = 4
mod_operator(a,b)

a = -13
b = -4
mod_operator(a,b)

a = 13
b = -4
mod_operator(a,b)


#####################
# integer constructor
#####################

print(int(10))   # 10
print(int(-10)) # -10
print(int(10.9)) # 10
print(int(True)) # 1
print(int("10")) # 10

## base conversion on constructor
## default 10
print(int("a", base=16)) # 10
print(int("a", base=11)) # 10
print(int("1010", base=2)) # 10
## reverse process
print(bin(10)) # 0b1010
print(oct(10)) # 0o12
print(hex(10)) # 0x10

## assign using base notation
a = 0b1010 # 10 from binary
a = 0o12   # 10 from octal
a = 0xa    # 10 from hexa

print(a)


####################################################
# base conversion (different representation) formula
####################################################

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    
    if n == 0:
        return [0]

    digits = []

    while n > 0:
        # m, n = n% b, n//b
        # return the division and the modulus
        n, m = divmod(n, b)
        digits.insert(0, m)

    return digits


def base_encode(digits, digits_map):
    if max(digits) >= len(digits_map):
        raise ValueError("digit_mpa is not long enough to encode the digists")

    ## use for loop
    # encoding = ""
    # for d in digits:
    #     encoding += digits_map[d]
    # return encoding    


    ## use comprehension
    return "".join([digits_map[d] for d in digits])


def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 32")
    
    ## check the sign
    sign = -1 if number < 0 else 1
    ## multiply for the sign for obtain a positive number
    number *= sign
    
    digits = from_base10(number, base)
    encoding = base_encode(digits, digit_map)

    if sign == -1:
        encoding = "-" + encoding
    
    return encoding


print(from_base10(10, 2))
print(from_base10(255, 16))

print(base_encode([15, 15], "0123456789ABCDEF"))

print(rebase_from10(10, 2))
print(rebase_from10(255, 16))
print(rebase_from10(-10, 2))
print(rebase_from10(-255, 16))


###################
# ractional numbers
###################

from fractions import Fraction

print(Fraction(1))
print(Fraction(2, 4))
print(Fraction(numerator=2, denominator=4))
print(Fraction(0.125))
print(Fraction("0.125"))
print(Fraction("22/7"))

x = Fraction(2, 3)
y = Fraction(3, 4)
print(x + y)
print(x * y)
print(x / y)

## automatic reduction
print(Fraction(8, 16)) # 1/2

x = Fraction(1, -4)
print(x.numerator)
print(x.denominator)

## finite precision
x = Fraction(math.pi)
print(x)

y = Fraction(math.sqrt(2))
print(float(y))

a = 0.125
print(a)
b = 0.3
print(b)

print(Fraction(a))
print(Fraction(b))

print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))

f = Fraction(math.pi)
print(math.pi)
print(f.limit_denominator(10))
print(f.limit_denominator(100))
print(f.limit_denominator(1000))


################################
# floats internal representation
################################

print(float(10))
print(float(10.4))
print(float("12.5"))
print(float(Fraction('22/7')))

## not exactely representation
b = 0.1
print(b)
print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))
## exactely representation
b = 0.125
print(b)
print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))


###########################################
# float equaliy testing
# PEP 485 for equality testing
# https://www.python.org/dev/peps/pep-0485/
###########################################

x = 0.1
print(x)
print(format(x, ".25f"))

## exact representation
## works in comparison
x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)

## not exact representation
## diesn't work in comparison
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)

## round
## it works, but not definitive solution
print(round(x, 3) == round(y, 3))

## absolute tollerance
## very cole numbers, relatively
x = 10000.01
y = 10000.02

## not close numbers, relatively
x = 0.01
y = 0.02

# is close function for comparison
x = 0.1 + 0.1 + 0.1
y = 0.3
from math import isclose
print(isclose(x, y))

## is close relative tollerance
x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01)) # true

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01)) # false

x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01)) # false

## is close absolute tollerance
x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01)) # true

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01)) # true

x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01, abs_tol=0.0001)) # true

## for small number look a absolute tollerances
## for big number look a relative tollerances
x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print(isclose(x, y, rel_tol=0.01, abs_tol=0.0001)) # true
print(isclose(a, b, rel_tol=0.01, abs_tol=0.0001)) # true


##########################################################################################
# float coercing integers
# truncation, simply return the integer portion of the number: 10.6 -> 10, -10.6 -> -10
# floor, the largest integer less than or equal the number: 10.6 -> 10, -10.6 -> -11
# ceiling, the smallest integer greater than or equal the number: 10.6 -> 11, -10.6 -> -10
##########################################################################################

## truncation
from math import trunc

print(trunc(10.6))
print(trunc(-10.6))

### int constructor does a truncation
print(int(10.6))
print(int(-10.6))

## floor
from math import floor

print(floor(10.6))  # 10
print(floor(-10.6)) # -11

## ceiling
from math import ceil
print(ceil(10.6))  # 11
print(ceil(-10.6)) # -10


############################################
# float rounding
# use Banker's Rounding standard -> IEEE 754
# round function is built-in
############################################

print(round(1.9)) # 2 int
print(round(1.9, 0)) # 2.0 float

## n > 0 examples
print(round(1.8888, 0)) # 2.0
print(round(1.8888, 1)) # 1.9
print(round(1.8888, 2)) # 1.89
print(round(1.8888, 3)) # 1.889

## n < 0
print(round(888.88, -4)) # 0.0, round to multiples of 10000
print(round(888.88, -3)) # 1000.0
print(round(888.88, -2)) # 900.0
print(round(888.88, -1)) # 890.0
print(round(888.88, 0)) # 889.0
print(round(888.88, 1)) # 888.9

## ties
## round to closest even
print(round(1.25, 1)) # 1.2
print(round(1.35, 1)) # 1.4
print(round(-1.25, 1)) # -1.2
print(round(-1.35, 1)) # -1.4

## round up function
def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5)) # 2
print(_round(1.5)) # 2

print(round(2.5)) # 2
print(_round(2.5)) # 3


###############################
# decimals
# decimal module PEP 327
# alternative to use float type
###############################

import decimal
from decimal import Decimal

g_ctx = decimal.getcontext()

print(g_ctx) # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
print(g_ctx.prec) # 28

## change precision
g_ctx.prec = 6
print(g_ctx)

## change rounding
g_ctx.rounding = decimal.ROUND_HALF_UP
print(g_ctx)

## reset
g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN

## local context
x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    #print(ctx)
    #print(decimal.getcontext())
    print(round(x, 1)) # 1.3
    print(round(y, 1)) # 1.4

### at global context
print(round(x, 1)) # 1.2
print(round(y, 1)) # 1.4

##########################################################################
# decimals constructor and contexts
# accepts integers, other Decimal object, strings, tuples and floats
# float usually not used because Decimal store the exacltly representation
##########################################################################

print(Decimal(10))
print(Decimal(-10))
print(Decimal("10.1"))
print(Decimal("-3.1234"))
print(Decimal((1,(3,1,2,3,4),-4)))
print(Decimal((0,(3,1,2,3,4),-4)))
print(Decimal((0,(3,1,2,3,4),-3)))

## avoid floats, use instead strings
print(Decimal("0.1"))
print(Decimal(0.1))
print(Decimal(0.1) == Decimal('0.1'))

## constructor context
decimal.getcontext().prec = 2
### does not affect the constructor, the storage of the number
print(Decimal("0.123456789"))

a = Decimal("0.12345")
b = Decimal("0.12345")

print(a)
print(b)
print(a+b) # 0.25, the precision affects operations

## set global context to 6
decimal.getcontext().prec = 6

## local context example
a = Decimal("0.12345")
b = Decimal("0.12345")
print(a+b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(f"local context {c}") # c created in context with precision 2

print(f"global context {c}")

## set global context to default
decimal.getcontext().prec = 28


######################################################################
# decimals math operations
# // for integers perform floor division -> a // b == floor(a/b)
# // for Decimals perform a truncated division -> a // b == trunc(a/b)
######################################################################

## // and % operators
## n = d * (n//d) + (n%d)
x = 10
y = 3
print(x//y, x%y) # 3 1
print(x == y * (x//y) + (x%y)) # true

x = Decimal(10)
y = Decimal(3)
print(x//y, x%y) # 3 1
print(x == y * (x//y) + (x%y)) # true

x = -10
y = 3
print(x//y, x%y) # -4 2
print(x == y * (x//y) + (x%y)) # true

x = Decimal(-10)
y = Decimal(3)
print(x//y, x%y) # -3 -1
print(x == y * (x//y) + (x%y)) # true

## other math functions
a = Decimal("0.1")
print(a.ln())
print(a.exp())
print(a.sqrt())

print(math.sqrt(a))

### differences
x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, "1.27f"))
print(format(root_mixed, "1.27f"))
print(format(root_dec))

print(format(root_float * root_float, "1.27f"))
print(format(root_mixed * root_mixed, "1.27f"))
print(format(root_dec * root_dec))


#####################################
# decimals performance considerations
#####################################

## memory footprint
a = 3.1415
b = Decimal("3.1415")

print(sys.getsizeof(a)) # 24 bytes
print(sys.getsizeof(b)) # 104 bytes

## cpu footprint
import time

def create_float(n=1):
    for i in range(n):
        a = 3.1415

def create_decimal(n=1):
    for i in range(n):
        a = Decimal("3.1415")

## uncomment operation to test
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        #math.sqrt(a)
        a + a
        #a * a
        #a - a
        #a / a

## uncomment operation to test
def run_decimal(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        #a.sqrt()
        a + a
        #a * a
        #a - a
        #a / a

#n = 10_000_000
n = 1_000_000 # for test sqrt

start = time.perf_counter()
#create_float(n)
run_float(n)
end = time.perf_counter()
print(f"Float: {end - start}")

start = time.perf_counter()
#create_decimal(n)
run_decimal(n)
end = time.perf_counter()
print(f"Decimal: {end - start}")


#################
# complex numbers
#################

a = complex(1, 2)
b = 1 + 2j
print(a == b)

## represented internally as float type
print(a.real)
print(type(a.real))

print(a.imag)
print(type(a.imag))

print(a.conjugate())

## operations
## // doesn't work
## % doesn't work
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

## equality
a = 0.1j
print(format(a.imag, ".25f"))
print(a + a + a == 0.3j) # false

print(format((a+a+a).imag, ".25f"))
print(format((0.3j).imag, ".25f"))

## cmath library
## math library for complex numbers
import cmath

print(cmath.pi)
print(cmath.sqrt(a))

a = 1 + 1j
## rectangular to polar
print(cmath.phase(a))
print(abs(a))
## polar to rectangular
print(cmath.rect(math.sqrt(2), math.pi/4)) # wrong

rhs = cmath.exp(cmath.pi * 1j) + 1
print(rhs)

print(cmath.isclose(rhs, 0)) # false
print(cmath.isclose(rhs, 0, abs_tol=0.0001)) # true


######################
# booleans
# descrived in PEP 285
# https://www.python.org/dev/peps/pep-0285/
# subclass of int
######################

print(issubclass(bool, int)) # true
print(type(True))
print(id(True))
print(int(True))
print(type(False))
print(id(False))
print(int(False))

print(3 < 4) # true
print(id(3 < 4)) # same id of True
print((3 < 4) == True) # true
print((3 < 4) is True) # true
print((1 == 2) == False) # true
print((1 == 2) is False) # true

## integer values
print(int(True)) # 1
print(int(False)) # 0
print(1 + True) # 2
print(True > False) # false
print((True + True + True) % 2) # 1

## int to bool
print(bool(0)) # true
print(bool(1)) # false


#######################
# booleans truth values
#######################

## 0 is the only integer value that evaluate to false
print(bool(1)) # true
print(bool(0)) # false

## under the hood
## int class has __bool__ method
print(bool(100), (100).__bool__())

a = []
print(bool(a), a.__len__())
## other numeric types
print(bool(0.0), bool(0+0j), bool(Decimal(0)), bool(Fraction(0, 1))) # all false

## maps
a = []
b = ""
c = ()
print(bool(a), bool(b), bool(c)) # all false

a = [1, 2]
b = "abc"
c = (1, 2)
print(bool(a), bool(b), bool(c)) # all true

a = {}
b = set()
print(bool(a), bool(b)) # all false

a = {"a": 1}
b = {1, 2}
print(bool(a), bool(b)) # all true

## none object
print(bool(None)) # false

a = [1, 2, 3]
#a = []
#a = None

if a is not None and len(a) > 0:
    print(a[0])
else:
    print("a is empty")

## short version
if a: # evaluate to bool, trigger __len__ method
    print(a[0])
else:
    print("a is empty")


#############################################################################
# booleans precedence and short circuiting
# boolean operator not and or
# commutativity property: A or B == B or A, A and B == B and C
# distribuitivity property: A and (B or C) == (A and B) or (A and c)
# distribuitivity property: A or (B and C) == (A or B) and (A or c)
# associativity property: A or (B or C) == (A or B) or C -> A or B or C
# associativity property: A and (B and C) == (A and B) and C -> A and B and C
# De Morgan's Theoreme: not(A or B) == (not A) and (not B)
# De Morgan's Theoreme: not(A and B) == (not A) or (not B)
#############################################################################

## precedence not -> and -> or, or is the last to be avaluated
print(True or True and False) # true
print(True or (True and False)) # true
print((True or True) and False) # false

## short circuiting
a = 10
b = 2
### if b is 0 in this case we have an exception
if a / b > 2:
    print("a is at least twice b")

a = 10
b = 0
### with short circuiting
### if b is greater than zero, python does not evaulate the division
if b and a / b > 2:
    print("a is at least twice b")

import string
a = 'c'
print(a in string.ascii_uppercase)

name = "Bob"
### if name is empty this return an error
if name[0] in string.digits:
    print("Name cannot start with a digit")

name = "Bob"
# name = ""
# name = None
### works in all cases
if name and name[0] in string.digits:
    print("Name cannot start with a digit")


##################
# boolean operator
##################

## or evaluate x, if true return x, if false evaluate y and return it
## return a
print("a" or [1,2]) # a
## return the list
print("" or [1,2]) # [1,2]

s1 = None
s2 = ''
s3 = 'abc'

## return the first that evaluate to true that is s3
print(s1 or s2 or s3 or 'n/a')

## and evaluate x if false return x, if true evaluate y and return it
print(None and [1,2]) # None
print([1,2] and None) # None

a = 2
b = 4

if b  == 0:
    print(0)
else:
    print(a/b)

### can write the same thing as
a = 2
b = 0
print(b and a/b)

### othere example
s1 = None
s2 = ''
s3 = 'abc'

print(s1 and s1[0]) # None
print(s2 and s2[0]) # empty string ''
print(s3 and s3[0]) # 'a'

print((s1 and s1[0]) or 'n/a') # 'n/a'
print((s2 and s2[0]) or 'n/a') # 'n/a'
print((s3 and s3[0]) or 'n/a') # 'a'

## not operator
print(not True) # false
print(not False) # true
print(not None) # true
print(not 'abc') # false


######################
# comparison operators
######################

## membership operators
print(0.1 is (3+4j)) # false
print(3 is 3) # true
print([1, 2] is [1, 2]) # false

print('a' in 'this is a test') # true
print(3 not in [1, 2, 3, 4]) # false

print('key' in {'key': 1}) # true
print(1 in {'key': 1}) # false

## ordering operators
## not supported for complex numbers
print(3 < 5) # true
print(4 < Decimal('10.5')) # true
print(Fraction(2, 3) < Decimal('0.5')) # false
print(Fraction(2, 2) == True) # true

## chained comparison
print(1 < 2 < 3) # true
## equal to
print(1 < 2 and 2 < 3) # true

## not a best practice, confusing
print('A' < 'a' < 'z' > 'Z' in string.ascii_letters) # true

## make more sense
min = 0
max = 100
age =37
print(min < age < max) # true
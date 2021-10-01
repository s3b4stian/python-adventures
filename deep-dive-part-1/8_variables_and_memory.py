import sys
import ctypes
import gc

###########################
# variable memory reference
###########################

my_var_ = 10

## find memory address of variable
## base 10 memory address
print(id(my_var_))
## base 16 memory address
print(hex(id(my_var_)))


#####################################################
# reference counting
# python keep track of the references between objects
#####################################################

## assigned by reference
my_var = 20

## creates an extra reference
print(sys.getrefcount(my_var))

## do not affect reference count, pass memory address as integer
print(ctypes.c_long.from_address(id(my_var)).value)

other_my_var = my_var

print(sys.getrefcount(my_var))
print(ctypes.c_long.from_address(id(my_var)).value)


####################################################################
# garbage collection
# gc module for controll garbage collector
# it is always on, but may be turned off, off garbage collector does 
# not prevent memory leaks due to circular references
####################################################################

def ref_count(address):
    return ctypes.c_long.from_address(id(address)).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"

    return "Not Found"

## classes for simulate circular reference
class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self: {hex(id(self))}, b: {hex(id(self.b))}")

class B:
    def __init__(self, a_instance):
        self.a = a_instance
        print(f"B: self: {hex(id(self))}, a: {hex(id(self.a))}")

## disable garbage collector
gc.disable()

## istantiate class with circular reference
my_var_a = A()
print(my_var_a)

a_id = id(my_var_a)
b_id = id(my_var_a.b)

print(hex(a_id))
print(hex(b_id))

## check if the object exists in garbage collector
## it exists
print(object_by_id(a_id))
print(object_by_id(b_id))

## erase the content of my_var_a
my_var_a = None

print(ref_count(a_id))
print(ref_count(b_id))

## object still exists because garbage collector is turned off
print(object_by_id(a_id))
print(object_by_id(b_id))

## run garbage collector
gc.collect()

## now object does not exist
print(object_by_id(a_id))
print(object_by_id(b_id))


#########################
# variable re-assignement
#########################

my_var_b = 10

## re-assign does not replace the value of the object in memory 
## but create a new with the new value
## because value inside int object is immutable
my_var_b = 20

## same thing happens with
my_var_b = my_var_b + 10

## when the value of variable is the same, them point the same object
my_var_c = 10
my_var_d = 10
## same id
print(id(my_var_c))
print(id(my_var_d))


#################################################################################################################
# object mutability
# when the internal state of an object change, python only update it and does not create new object in memory
# object mutable    -> internal state can change [lists, sets, dictionaries, user-defined classes]
# object immutable  -> internal state cannot change [numbers, strings, tuples. frozen sets, user-defined classes]
#################################################################################################################

## particular case
my_list_a = [1, 2]
my_list_b = [3, 4]

my_tuple = (my_list_a, my_list_b)

print(my_tuple)

my_list_a.append(3)
my_list_b.append(5)

## elements inside tuble are mutated, state changed, but tuple no, it has same references inside, this is also valid
print(my_tuple)


################################################################################
# function arguments and mutability
# when pass a immutable object as argument to a function, object does not change
# when pass a mutable object as argument to a function, object may be change
################################################################################

## strings are immutable and as argument to fucntion does not change
## id of the argument s in the function change after updade
## because python create a new string object
my_string = "sebastian"

def say_hello(s: str) -> str:
    print(id(s))
    s = "Hello, " + s
    print(id(s))
    return s

print(say_hello(my_string))
print(my_string)

## list are mutable and changes made inside a function, can alter it
## id of the argument list_to_update does not change
## because list is a mutable object
my_list_c = [1, 2, 3]

def modify_list(list_to_update: list) -> None:
    print(id(list_to_update))
    list_to_update.append(len(list_to_update) + 1)
    print(id(list_to_update))

print(my_list_c)

modify_list(my_list_c)
modify_list(my_list_c)
modify_list(my_list_c)

print(my_list_c)


################################################################
# shared references and mutability
# happens when two variables points to the same object in memory
################################################################

## with a immutable object python share reference
a = "hello"
b = a

print(id(a))
print(id(b))

a = "hello"
b = "hello"

print(id(a))
print(id(b))

## when the value change, python reference new object
b = "hello world"

print(id(b))

## mutable object
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

## if b is updated, also a is affected
b.append(4)
print(a)
print(b)

## with mutable objects python don't share references
a = [1, 2, 3]
b = [1, 2, 3]
## id are not the same
print(id(a))
print(id(b))


###############################################
# varible equality
# python compare memory address or object state
###############################################

## memory address compare is is, for negation is is not
## object state compare is ==, for negation is !=
a = 10
b = 10
print(a is b) # true
print(a == b) # true

a = "hello"
b = "hello"
print(a is b) # true, but may not return true
print(a == b) # true

a = [1, 2, 3]
b = [1, 2, 3]
## false because mutable object doesn't have shared reference
print(a is b) # false
## true because elements are equal
print(a == b) # true

a = 10
b = 10.0
## different type, differente reference object in memoty, value is the same
print(a is b) # false
print(a == b) # true

## None is a object managed by python and all variales with this value point the same object
a = None
b = None
c = None
print(a is b) # true
print(a == b) # true
print(a is c) # true


#########################
# everithing is an object
#########################

a = 20
print(type(a))

## int is an object and we can istantiate it as normal object
a = int(20)
print(type(a))

## python has built in help
## return information about int class
## help(int)

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

print(type(square))

f = square
print(f is square)
print(f(2))

## return a function object
def select_function(fn: str):
    if fn == "square":
        return square
    elif fn == "cube":
        return cube
    else:
        return None

a = select_function("square")
print(a is square)
print(a(2))

## shortcut
print(select_function("square")(2)) # 4
print(select_function("cube")(2)) # 8

## take function as argument
def exec_function(fn, n):
    return fn(n)

print(exec_function(square, 2)) # 4
print(exec_function(cube, 2)) # 8

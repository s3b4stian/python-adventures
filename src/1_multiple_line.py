##########
# implicit
##########

## list multiple line
## works also with tuples, dictionaries
[1, # item 1
2,  # item 2
3]  # item 3

## function arguments in declaration
def my_func(a, 
            b, # a comment
            c):
    print(a, b, c)

## function arguments in call
my_func(10, # comment
         20, 30)


##########
# explicit
##########

## backslash character
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
    and c > 20:
    print(a, b, c)

# multi-line string literals

a = '''this is 
a multi-line string'''

b = """this is 
a multi-line string"""


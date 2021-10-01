##############
# conditionals
##############

## if statement
a = 2

if a < 5:
    print('yes')

## if else statement
a = 7

if a < 5:
    print('yes')
else:
    print('no')

b = 10

if b < 5:
    print('b < 5')
else:
    if b < 10:
        print('5 <= b < 10')
    else:
        print('b >= 10')

## elif statement
c = 10

if c < 5:
    print('c < 5')
elif c < 10:
    print('5 <= c < 10')
elif c < 15:
    print('10 <= c < 15')
elif c < 20:
    print('15 <= c < 20')
else:
    print('c >= 20')

## ternary operator
a = 25
b = 'a < 5' if a < 5 else 'a >=5'
print(b)
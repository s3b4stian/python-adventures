#######################################################################
# for loop
# works with iterables, objects capable of returning values one at time
#######################################################################

for i in range(5):
    print(i)

## list
for i in [0, 1, 2, 3, 4]:
    print(i)

## string
for c in "String is iterable":
    print(c)

## tuple
for i in ('a', 'b', 'c', 4):
    print(i)

## list of tuples
for i in [(0, 1), (2, 3), (4, 5)]:
    print(i)

## list of tuples unpacked
for i, j in [(0, 1), (2, 3), (4, 5)]:
    print(i, j)

## break
for i in range(5):
    if i == 3:
        break
    print(i)

## else statement
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print("multiple of 7 found")
        break
else:
    print("no multiples of 7 in the range")

## with try except statement
for i in range(5):
    print('-------------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print("division by 0")
        continue # works also for break keyword
    finally:
        print("always execute")
    
    print(i)

## index of iterable
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

### better
for i in range(len(s)):
    print(i, s[i])

### best
for i, c in enumerate(s):
    print(i, c)
############
# while loop
############

i = 0

while i < 5:
    print(i)
    i += 1

## while true and break
i = 5

while True:
    print(i)
    if i >= 5:
        break # break the loop

min_length = 2
name = input("Please enter your name:")

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name:")

print(f"Hello {name}")

### refactor
min_length = 2

while True:
    name = input("Please enter your name:")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break

print(f"Hello {name}")

## continue statement
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue # skip next instruction and continue from the next loop
    print(a)

## while else
## else executed when loop end normally, if a brake happens else will be skipped
l = [1, 2, 3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)

## break an continue with the try statement
a = 0
b = 2

while a < 4:
    print('-------------------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a}, {b} - division by 0")
        continue # works also for break keyword
    finally:
        print(f"{a}, {b} - always execute")
    
    print(f"{a}, {b} - main loop")


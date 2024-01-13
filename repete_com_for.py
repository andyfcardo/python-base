#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1, 11)

#Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print (number)
    else:
        continue
    print(f"mais codigo com {number}")
    




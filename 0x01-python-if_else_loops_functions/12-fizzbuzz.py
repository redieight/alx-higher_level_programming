#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 != 0 and i % 5 != 0:
            print(i, end=" ")
            continue
        if i % 3 == 0:
            print("Fizz", end=" ")
            continue
        if i % 5 == 0:
            print("Buzz", end=" ")
        print(" ", end="")

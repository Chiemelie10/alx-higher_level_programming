#!/usr/bin/python3
""" A function that prints numbers from 1 to 100 separated by a space.
  For multiples of three, it prints Fizz instead of the number,
  for multiples of five, it prints Buzz inplace of the number,
  and for multiples of three and five, it prints FizzBuzz instead
  of the number.
  """


def fizzbuzz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz ', end='')
        elif i % 3 == 0:
            print('Fizz ', end='')
        elif i % 5 == 0:
            print('Buzz ', end='')
        else:
            print("{} ".format(i), end='')

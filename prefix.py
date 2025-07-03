#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefix.py sum 5 2
7

$ prefix.py mul 10 5
50

$ prefix.py
operacao: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"
__author__ = "Rapha"

import sys

"""
sys.argv is a list of CLI arguments. index 0 is the name of the program,
index 1 is the first argument, index 2 the second and so on. ex:

$ python3 program.py arg1 arg2 arg3 ...
          [0]        [1]  [2]  [3]
"""

"""
in the first line we want everything that comes after the name
of the program (which is index 0, that's why [:1]) to be stored
inside the variable (arguments), and to be considered as a argument (sys.argv)
"""
arguments = sys.argv[1:]

"""
first thing is to treat the exceptions -> if the user does not give the program
any arguments then it should ask for the information needed to execute the
operations. or else if the user gives more arguments than the program needs for
the operation, it should print the error, print an example of usage and exit.
"""
if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

"""
unpacking the numbers and the operations from the arguments variable.
the first variable (operation) is storing the first item of the arguments list
(index 0, the other operation variable which contains the input), the second
variable (nums) is storing the other two items (n1, n2, indexes 1, 2, which
are storing the two numbers necessary for the calculations)
"""

operation, *nums = arguments

"""
next there's a tuple storing all the valid operations.

then we have a condition block that checks if the given operation is inside
the valid_operations variable, which contains the only valid operations, if
the given operation is not part of the tuple, it should print the tuple
elements and then exit. 
"""
valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

"""
now there's a condition block to check if the user's input is a number, and
if it is, it is a floating point number? if so, it parses the input to float()
(so we don't get any TypeErrors during the calc) if it's an integer number
it parses the input to int(). and at the end it appends the valid numbers to
the validated_nums list. Note: in order to check whether the user's input is a
digit, we need to get rid of the - potential - dots of the number that is being
verified - when the user wants to calculate with floating point numbers, e.g.
"""
validated_nums = []
for num in nums:
    if not num.replace(".","").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
        validated_nums.append(num)

# unpacks the numbers after the validation into their respective variables
n1, n2 = validated_nums

"""
finally, the last condition block that checks which operation the program
should do and prints the result
"""
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")
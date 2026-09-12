"""
Operators in Python are special symbols that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.
Python supports a variety of operators, including arithmetic, comparison, logical, assignment, and more.

Arithmetic Operators:
- Addition (+): Adds two operands.
- Subtraction (-): Subtracts the second operand from the first.
- Multiplication (*): Multiplies two operands.
- Division (/): Divides the first operand by the second operand.
- Floor Division (//): Divides the first operand by the second operand and returns the largest integer less than or equal to the result.
- Modulus (%): Returns the remainder of the division of the first operand by the second operand.
- Exponentiation (**): Raises the first operand to the power of the second operand.

1. Addition (+):
a = 5
b = 3
print(a + b)  # Output: 8

2. Subtraction (-):
a = 5
b = 3
print(a - b)  # Output: 2

3. Multiplication (*):
a = 5
b = 3
print(a * b)  # Output: 15

4. Division (/):
a = 5
b = 3
print(a / b)  # Output: 1.6666666666666667

5. Floor Division (//):
a = 5
b = 3
print(a // b)  # Output: 1

6. Modulus (%):
a = 5
b = 3
print(a % b)  # Output: 2

7. Exponentiation (**):
a = 5
b = 3
print(a ** b)  # Output: 125

Comparison Operators:
- Equal to (==): Returns True if both operands are equal.
- Not equal to (!=): Returns True if operands are not equal.
- Greater than (>): Returns True if the left operand is greater than the right operand.
- Less than (<): Returns True if the left operand is less than the right operand.
- Greater than or equal to (>=): Returns True if the left operand is greater than or equal to the right operand.
- Less than or equal to (<=): Returns True if the left operand is less than or equal to the right operand.

1. Equal to (==):
a = 5
b = 3
print(a == b)  # Output: False

2. Not equal to (!=):
a = 5
b = 3
print(a != b)  # Output: True

3. Greater than (>):
a = 5
b = 3
print(a > b)  # Output: True

4. Less than (<):
a = 5
b = 3
print(a < b)  # Output: False

5. Greater than or equal to (>=):
a = 5
b = 3

print(a >= b)  # Output: True

6. Less than or equal to (<=):
a = 5
b = 3
print(a <= b)  # Output: False

Assignment Operators:
- Assignment (=): Assigns a value to a variable.
- Addition Assignment (+=): Adds the right operand to the left operand and assigns the result to the left operand.
- Subtraction Assignment (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
- Multiplication Assignment (*=): Multiplies the left operand by the right operand and assigns the result to the left operand.
- Division Assignment (/=): Divides the left operand by the right operand and assigns the result to the left operand.
- Floor Division Assignment (//=): Performs floor division on the left operand by the right operand and assigns the result to the left operand.
- Modulus Assignment (%=): Computes the modulus of the left operand by the right operand and assigns the result to the left operand.
- Exponentiation Assignment (**=): Raises the left operand to the power of the right operand and assigns the result to the left operand.

Additonally, Python also supports logical operators (and, or, not) for combining boolean expressions, and bitwise operators (&, |, ^, ~, <<, >>) for performing operations on binary representations of integers.

Logical Operators:
- Logical AND (and): Returns True if both operands are True.
- Logical OR (or): Returns True if at least one of the operands is True.
- Logical NOT (not): Returns True if the operand is False, and False if the operand is True.
1. Logical AND (and):
a = True
b = False
print(a and b)  # Output: False

2. Logical OR (or):
a = True
b = False
print(a or b)  # Output: True

3. Logical NOT (not):
a = True
print(not a)  # Output: False

4. Bitwise Operators:
- Bitwise AND (&): Performs a bitwise AND operation on two integers.
- Bitwise OR (|): Performs a bitwise OR operation on two integers.
- Bitwise XOR (^): Performs a bitwise XOR operation on two integers.

- Bitwise NOT (~): Performs a bitwise NOT operation on an integer.
- Left Shift (<<): Shifts the bits of the first operand to the left by the
      number of positions specified by the second operand.

- Right Shift (>>): Shifts the bits of the first operand to the right by the
      number of positions specified by the second operand.  

Bitwise AND (&):
a = 5  # Binary: 0101

b = 3  # Binary: 0011
print(a & b)  # Output: 1 (Binary: 0001)

Bitwise OR (|):
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(a | b)  # Output: 7 (Binary: 0111)

Bitwise XOR (^):
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(a ^ b)  # Output: 6 (Binary: 0110)

Bitwise NOT (~):
a = 5  # Binary: 0101
print(~a)  # Output: -6 (Binary: 1010, two's complement representation)

PRACTICE EXERCISES:
1. Write a Python program that takes two numbers as input from the user and performs addition,
2. Write a Python program that takes two numbers as input from the user and performs subtraction, multiplication, division, floor division, modulus, and exponentiation.

3. Answer True or False for the following statements:
a. The addition operator (+) can be used to concatenate strings. 
b. The modulus operator (%) returns the quotient of a division operation. 
c. The logical AND operator (and) returns True if both operands are True. 
d. print(126>137)
e. print((124<=124 and 124>=124 and 123<124) != (136!=179 or 136==179 or 195=195)) 
---------------------------------------------------END--------------------------------------------------------------
"""
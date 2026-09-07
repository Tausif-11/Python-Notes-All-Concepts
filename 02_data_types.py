# What are Data types in Python?
# Data types in Python are classifications that specify the type of data a variable can hold. They define the operations that can be performed on the data and the way the data is stored in memory. Python has several built-in data types, including:
# 1. Integer (int)
# 2. Float (float)
# 3. String (str)
# 4. Boolean (bool)
# 5. List (list)
# 6. Tuple (tuple)
# 7. Dictionary (dict)
# 8. Set (set)

# Python has these built-in data types, and you can also create your own custom data types using classes. Each data type has its own characteristics and methods that can be used to manipulate the data. Understanding data types is essential for effective programming in Python, as it helps in writing efficient and error-free code.

# ---------------------------------------STRINGS & TYPE CONVERSIONS---------------------------------------------

# Strings are sequences of characters enclosed in single quotes (' ') or double quotes (" "). They are used to represent text data in Python. Strings can be manipulated using various methods and operations, such as concatenation, slicing, and formatting.

# Example of a string:
my_string = "Hello, World!"

# String also takes more space and memory than other data types, for eg. Int, float, etc. So, it is advisable to use string data type only when it is necessary.
# This happens because strings stores every character with their own unicode.

# Unicode is a universal character encoding standard that assigns a unique number (code point) to every character , regardless of language.

# You can check the unicode like this:
a =""
# print ("Unicode of character 'a' is:", ord(a))  # Output: Unicode of character 'a' is: 65

# you can also check character from unicode like this:
a = 65
# print ("Character of Unicode 65 is:", chr(a))  # Output: Character of Unicode 65 is: A

#                           STRING INDEXING & SLICING

"""
What is string indexing ?

So basically, string indexing is a way to access individual character in a string using their position or index. In Python, strings are zero-indexed, which means the first character of a string has an index of 0, the second character has an index of 1, and so on. You can also use negative indexing to access characters from the end of the string, where -1 refers to the last character, -2 refer to the second last character, and so on.

for eg:
      Name = " Mohammad "
      Postive Index:   0 1 2 3 4 5 6 7 8 9
      Negative Index:  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

      to check:
      print(Name[0])  # Output: M
      print(Name[-1]) # Output: d

      but if you try to access an index that is out of range, you will get an IndexError. For example, if you try to access Name[10] or Name[-11], you will get an error because the string only has 10 characters.

      eg:
      Name = " Raj "
      print(Name[10])  # Output: IndexError: string index out of range

Now, let's talk about string slicing.
What is string slicing ?
String slicing is a way to extract a portion of a string by specifying a range of indices. You can use the slice notation [start:stop:step] to extract a substring from a string. The start index is inclusive, while the stop index is exclusive. The step parameter is optional and specifies the number of characters to skip between each character in the slice.

let's take an example to understand string slicing better:
            Name = " Rahul "
            print(Name[0:3])  # Output: Rah
            print(Name[1:5])  # Output: ahu
            print(Name[::2])  # Output: Rhl

            what if we print
            print(Name[::])  # Output: Rahul

            print(Name[::-1])  # Output: luhar

            print (Name[1:5:2])  # Output: au

            So by these examples, we can see how string indexing and slicing work in Python. They are powerful tools for manipulating strings and extracting specific information from them.

                            #Type Conversions
Now, lets talk about Type Conversions

Type conversion, also known as type casting, is the process of converting a value from one data type to another. In Python, you can convert between different data types using built-in functions. Here are some common type conversions:
1. int() - Converts a value to an integer.
2. float() - Converts a value to a floating-point number.
3. str() - Converts a value to a string.
4. bool() - Converts a value to a boolean (True or False).
5. list() - Converts a value to a list.
6. tuple() - Converts a value to a tuple.

For understanding type conversions, you need to look at these examples:
1.FLOAT  2. INT  3. STRING  4. BOOLEAN

eg: 
converting int to a string:
a = 10
new_string = str(a)
it gives output as: '10' (string)

converting string to an int:
b = "20"
print(int(b)) # Output: 20 (int)

but you can't convert a string to an int if the string does not represent a valid integer. For example:
c = "Hello"
print(int(c)) # Output: ValueError: invalid literal for int() with base 10: 'Hello'

Now lets talk about boolean:

In Boolean we need to first understand what is truthy and falsy values in python. In Python, a truthy value is any value that is considered true when evaluated in a boolean context, while a falsy value is any value that is considered false. Here are some examples of truthy and falsy values:
Truthy values:
- Non-zero numbers (e.g., 1, -5, 3.14)
- Non-empty strings (e.g., "hello", "0")
- Non-empty lists, tuples, sets, and dictionaries

Falsy values:
- Zero (0)
- Empty strings ("")
- None
- Empty lists, tuples, sets, and dictionaries


for eg:
a = 10
print(bool(a))  # Output: True

b = 0
print(bool(b))  # Output: False

c = False
print(bool(c))  # Output: False

d = "" 
print(bool(d))  # Output: False

                                    Type of Conversions types
                                    1. Implicit Type Conversion (Type Casting)
                                    2. Explicit Type Conversion (Type Casting)

            Implicit Type Conversion (Type Casting):
            Implicit type conversion, also known as type coercion, is the automatic conversion of one data type to another by the Python interpreter. This usually happens when you perform operations involving different data types, and Python automatically converts one of the operands to a compatible type to avoid errors.
            For example:
            
            print(5 + 2.0)  # Output: 7.0 (int is converted to float)

            Explicit Type Conversion (Type Casting):
            Explicit type conversion, also known as type casting, is when you manually convert a value from one data type to another using built-in functions. This is done when you want to ensure that a value is of a specific type before performing operations on it.
            For example:

            a = "10"
            b = int(a)  # Explicitly converting string to int
            print(b)  # Output: 10 (int)


            


"""





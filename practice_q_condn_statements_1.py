# Problem.1 Accept two numbers and print the greatest between them.

# Accept two numbers from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and print the greatest
if num1 > num2:
      print("The greatest number is:", num1)
elif num2 > num1:
      print("The greatest number is:", num2)
else :
      print("Both numbers are equal.")
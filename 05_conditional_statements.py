""" Conditional Statements in Python allow decision-making by executing different blocks of code based on certain condtions.

Decision-making can be understood with an example:
eg- You will receive a number from the user, if the number is greater than 10 you will do task A and if the number is less than 10 you will do task B.

a = 157 

if a > 130:
      print ("I will do task A")

else:
      print ("I will do task B")





"""

""" LETS DO A REAL LIFE EXAMPLE OF CONDITIONAL STATEMENTS"""

# age = int(input("Enter your age: "))

# if age >= 18:
   # print("You are eligible to vote.")

# else:
   # print("You are not eligible to vote yet. Please wait until you turn 18.")

""" A more complex example of conditional statements can be seen in the following code snippet:"""  


 
 

# A student's Result Program:
# taking input from the user/student
name = input("Enter your name: ")

english = int(input("Enter your English marks: "))
maths = int(input("Enter your Maths marks: "))
physics = int(input("Enter your Physics marks: "))
chemistry = int(input("Enter your Chemistry marks: "))   
biology = int(input("Enter your Biology marks: "))

# Calculate total marks
total_marks = english + maths + physics + chemistry + biology 

# Calculate percentage
percentage = total_marks/5

# Determine the grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"                                                                                       
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

# Display result
print("\n----- RESULT -----")
print("Name:", name)
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
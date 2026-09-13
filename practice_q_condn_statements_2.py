"p.2 Accept the gender from user as character, and print the respective greeting message. "

gender = input("Enter your gender (M/F): ")

if gender == "M" or gender == "m":
    print("Hello Sir! Welcome.")
elif gender == "F" or gender == "f":
    print("Hello Ma'am! Welcome.")
else:
    print("Invalid gender entered.")
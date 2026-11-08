# Nicholas M. Pickett
# Mod2CaseStudy.py
# This program will take in a students first and last name and their GPA. It will then determine if they made the deans list, honor roll, graduated or did not graduate.

lastName = input("Enter Last Name: ")
firstName = input("Enter First Name: ")
gpa = float(input("Enter GPA: "))

if lastName == "zzz":
    print("Quitting program.")
    quit()


if gpa >= 3.5:
    print(f"Congratulations! {firstName} {lastName}, you have made the deans list.")
elif gpa >= 3.5:
    print(f"Congratulations! {firstName} {lastName}, you have made the honor roll.")
elif gpa >= 3.0:
    print(f"Congratulations! {firstName} {lastName}, you have graduated.")
else:
    print(f"Sorry, {firstName} {lastName}, you did not graduate.")
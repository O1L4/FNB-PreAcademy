#1.student info formatter-student_info.py
first_name=input("Enter your first name:")
surname=input("Enter your surname:")
age=int(input("Enter your age:"))
fav_number = float(input("Enter your favourite number:"))

#2.Display name
full_name = first_name + " " + surname
name_upper = full_name.upper()
name_title = full_name.title()

#3.calc & disp age in months
age_in_months = age*12

#4.rounding
fav_number_rounded = round(fav_number, 2)

#5.display profile card with f-strings
print(f"---STUDENT PROFILE CARD---")
print(f"Welcome, {full_name} !")
print(f"Full name in UPPERCASE: {name_upper}")
print(f"Full name in Title Case: {name_title}")
print(f"Age: {age} years")
print(f"in months: {age_in_months} months")
print(f"favourite number: {fav_number_rounded}")

#6.print data type
print(f"Type of first name:{type(first_name)}")
print(f"Type of surname:{type(surname)}")
print(f"Type of age:{type(age)}")
print(f"Type of fav_number:{type(fav_number)}")
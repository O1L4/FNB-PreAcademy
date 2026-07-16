#1. Ask the user to input their secret password
password = input("Enter your secret password:")

#2. Use .strip() to clean up accidental spaces
clean_password = password.strip()

#3. Grab first letter and last letter
first_letter = clean_password[0]
last_letter = clean_password[-1]

#4. print a hint using an f-string with uppercase letters
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")
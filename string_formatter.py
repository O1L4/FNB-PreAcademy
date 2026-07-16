#1. collect inputs
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
bio = input("Enter your bio message:")

#2. username: first initial + last name in lowercase
username = (first_name[0] + last_name).lower()

#3. full name in Title Case
full_name = (first_name + "" + last_name).title()

#4. trail whitespace from bio
clean_bio = bio.strip()

#5. Replace 'I'm' with 'I'm'
clean_bio = clean_bio.replace("I am" , "I'm")

#6. count characters in bio
bio_length = len(clean_bio)

#7. display all output using f-strings
print(f"\n--- userprofile ---")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {clean_bio}")
print(f"Bio Character Count: {bio_length}")
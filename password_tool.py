import random
import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    print("\nPassword Analysis:")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Moderate Password")
    else:
        print("Strong Password")

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("PASSWORD TOOL")
print("1. Check Password Strength")
print("2. Generate Password")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    password = input("Enter password: ")
    check_password(password)

elif choice == "2":
    length = int(input("Enter desired password length: "))
    new_password = generate_password(length)
    print("\nGenerated Password:")
    print(new_password)

else:
    print("Invalid Choice")
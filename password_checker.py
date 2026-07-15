import string

# Function to check password strength
def check_password_strength(password):
    # Check different conditions
    length_ok = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    if length_ok:
        score += 1
    if has_uppercase:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    # Decide password strength
    if score <= 1:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, length_ok, has_uppercase, has_number, has_symbol


print("Password Strength Checker")
print("-" * 30)

while True:
    # Take password from user
    password = input("Enter your password: ")

    # Check password
    strength, length_ok, has_uppercase, has_number, has_symbol = check_password_strength(password)

    print("\nPassword Report")
    print("-" * 30)
    print("Length (8+ chars):", length_ok)
    print("Has Uppercase    :", has_uppercase)
    print("Has Number       :", has_number)
    print("Has Symbol       :", has_symbol)

    print("\nPassword Strength:", strength)

    # Suggestions for improvement
    if strength == "Weak":
        print("\nSuggestions:")
        if not length_ok:
            print("- Password should be at least 8 characters long")
        if not has_uppercase:
            print("- Add at least one uppercase letter")
        if not has_number:
            print("- Add at least one number")
        if not has_symbol:
            print("- Add at least one special symbol")
    elif strength == "Medium":
        print("\nGood password, but it can be stronger.")
        print("Try adding more character variety.")
    else:
        print("\nStrong password. Well done!")

    choice = input("\nDo you want to check another password? (y/n): ")
    if choice.lower() != "y":
        break

print("\nProgram Finished.")

#Password Strength Checker
import re

#min 8 characters, at least 1 uppercase, 1 lowercase, 1 number and 1 special character
def check_pswd_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one number."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Your password is strong."

def pswd_checker():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Thank you for using the Password Strength Checker!")
            break
        result = check_pswd_strength(password)
        print(result)

if __name__ == "__main__":
    pswd_checker()


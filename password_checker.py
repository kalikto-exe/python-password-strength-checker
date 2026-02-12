"""
Password Strength Checker
Created by Kalikto (a.k.a. Smit Mehta)

A simple utility to evaluate password strength based on
length, character variety, and common security practices.
"""

import re

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "abc123", "password123", "admin", "letmein"
]


def check_password_strength(password):
    score = 0
    feedback = []

    # Check against common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common and easily guessable.")
        return 0, feedback

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("Password Strength Checker")
    print("Created by Kalikto (a.k.a. Smit Mehta)")
    print("-" * 40)

    password = input("Enter a password to check: ")

    score, feedback = check_password_strength(password)
    strength = get_strength_label(score)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password looks strong and secure.")


if __name__ == "__main__":
    main()
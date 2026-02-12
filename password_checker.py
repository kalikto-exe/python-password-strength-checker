import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
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
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("Password Strength Checker")
    print("-" * 30)

    password = input("Enter a password to check: ")

    score, feedback = check_password_strength(password)
    strength = get_strength_label(score)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password looks strong!")


if __name__ == "__main__":
    main()

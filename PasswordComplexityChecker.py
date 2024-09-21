import re

# List of common passwords
common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123', 'password1', 'admin']

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password)
    lower_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Strength calculation
    score = 0
    if length_criteria: score += 1
    if upper_criteria: score += 1
    if lower_criteria: score += 1
    if digit_criteria: score += 1
    if special_criteria: score += 1

    return score

def feedback_on_password(password):
    score = check_password_strength(password)

    # Check for common password
    if password in common_passwords:
        return "Weak: Your password is too common. Consider changing it."

    # Feedback based on score
    if score == 5:
        return "Very Strong: Your password is secure!"
    elif score == 4:
        return "Strong: Your password is good, but you could improve it."
    elif score == 3:
        return "Medium: Consider adding more variety to your password."
    elif score == 2:
        return "Weak: Your password lacks complexity. Add more characters."
    else:
        return "Very Weak: Use a longer password with uppercase, lowercase, digits, and special characters."

def suggest_improvement(password):
    improvements = []
    if len(password) < 8:
        improvements.append("Use at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        improvements.append("Add at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        improvements.append("Add at least one lowercase letter.")
    if not re.search(r'\d', password):
        improvements.append("Include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        improvements.append("Use at least one special character.")

    if improvements:
        return "Suggestions to improve your password: " + " ".join(improvements)
    else:
        return "Your password meets all criteria!"

# Main function
def main():
    password = input("Enter a password to check its strength: ")
    print(feedback_on_password(password))
    print(suggest_improvement(password))

if __name__ == "__main__":
    main()

def check_password(password):
    length = len(password) >= 8
    uppercase = any('A' <= char <= 'Z' for char in password)
    lowercase = any('a' <= char <= 'z' for char in password)
    number = any('0' <= char <= '9' for char in password)
    special_char = any(char in '!@#$%^&*(),.?":{}|<>' for char in password)

    if length and uppercase and lowercase and number and special_char:
        return "Strong password!"
    else:
        feedback = "Weak password.\n"
        if not length:
            feedback += "- Password should have at least 8 characters.\n"
        if not uppercase:
            feedback += "- Include at least one uppercase letter.\n"
        if not lowercase:
            feedback += "- Include at least one lowercase letter.\n"
        if not number:
            feedback += "- Include at least one number.\n"
        if not special_char:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>).\n"

        return feedback


def main():
    password = input("Enter your password: ")
    result = check_password(password)
    print(result)

if __name__ == "__main__":
    main()

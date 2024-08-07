import secrets
import string


def generate_secure_password(length=12, include_digits=True, include_punctuation=True):
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits if include_digits else ''
    punctuation = string.punctuation if include_punctuation else ''
    all_characters = letters + digits + punctuation

    if not all_characters:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password


def main():
    # Get user input
    try:
        length = int(input("Enter the desired password length: "))
        include_digits = input("Include digits (yes/no)? ").strip().lower() == 'yes'
        include_punctuation = input("Include special characters (yes/no)? ").strip().lower() == 'yes'

        if length < 1:
            raise ValueError("Password length must be at least 1")

        # Generate the password
        password = generate_secure_password(length, include_digits, include_punctuation)

        # Display the password
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")


# Run the script
if __name__ == "__main__":
    main()

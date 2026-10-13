ALLOWED_SYMBOLS = set("*@!?")
DIGIT_CHARACTERS = set("0123456789")
LOWERCASE_LETTERS = set("abcdefghijklmnopqrstuvwxyz")
UPPERCASE_LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def is_valid_password(password: str) -> bool:
    password_characters = set(password)
    allowed_characters = (
        DIGIT_CHARACTERS
        | LOWERCASE_LETTERS
        | UPPERCASE_LETTERS
        | ALLOWED_SYMBOLS
    )

    has_digit = bool(password_characters & DIGIT_CHARACTERS)
    has_lowercase = bool(password_characters & LOWERCASE_LETTERS)
    has_uppercase = bool(password_characters & UPPERCASE_LETTERS)
    has_symbol = bool(password_characters & ALLOWED_SYMBOLS)
    contains_only_allowed = password_characters <= allowed_characters

    return (
        8 <= len(password) <= 20
        and contains_only_allowed
        and has_digit
        and has_lowercase
        and has_uppercase
        and has_symbol
    )


def main() -> None:
    for _ in range(3):
        password = input("Password: ")
        if is_valid_password(password):
            print("Password is valid")
            return

    print("Password is invalid")


if __name__ == "__main__":
    main()
def is_integer(unchecked: str) -> bool:
    value = unchecked.strip()
    if not value:
        return False

    if value[0] in "+-":
        value = value[1:]

    return bool(value) and value.isdigit()


def remove_non_integer(unchecked: str) -> int:
    value = unchecked.strip()
    integer_text = "".join(
        character for character in value if not character.isalpha()
    )
    if not integer_text or integer_text in ("+", "-"):
        raise ValueError("The input does not contain an integer.")

    return int(integer_text)


def main():
    unchecked = input("Enter an integer: ")
    if is_integer(unchecked):
        print("Valid integer")
    else:
        print("Invalid integer")


if __name__ == "__main__":
    main()

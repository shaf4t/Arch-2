def unique_chars_dict(value: str) -> int:
    characters = {}
    for character in value:
        characters[character] = True
    return len(characters)


def unique_chars_set(value: str) -> int:
    characters = set()
    for character in value:
        characters.add(character)
    return len(characters)


def main() -> None:
    value = input("Enter a string: ")
    dictionary_count = unique_chars_dict(value)
    set_count = unique_chars_set(value)

    if dictionary_count != set_count:
        raise RuntimeError("The dictionary and set implementations disagree.")

    print(f"Unique characters: {dictionary_count}")


if __name__ == "__main__":
    main()
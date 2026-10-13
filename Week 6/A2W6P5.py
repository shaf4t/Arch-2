MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ",": "--..--",
    "?": "..--..",
    ".": ".-.-.-",
}

MORSE_TO_CHARACTER = {
    code: character for character, code in MORSE_CODE.items()
}


def message_to_morse(message: str) -> str:
    words = []
    for word in message.upper().split(" "):
        translated_word = []
        for character in word:
            if character not in MORSE_CODE:
                print(f"Can't convert char [{character}]")
                continue
            translated_word.append(MORSE_CODE[character])
        words.append(" ".join(translated_word))
    return "    ".join(words)


def morse_to_message(message: str) -> str:
    words = []
    for word in message.split("    "):
        translated_word = []
        for code in word.split():
            if code not in MORSE_TO_CHARACTER:
                print(f"Can't convert char [{code}]")
                continue
            translated_word.append(MORSE_TO_CHARACTER[code])
        words.append("".join(translated_word))
    return " ".join(words)


def translate_text(message: str) -> str:
    if all(character in ".- " for character in message):
        return morse_to_message(message)
    return message_to_morse(message)


def main() -> None:
    message = input("")
    print(translate_text(message))


if __name__ == "__main__":
    main()
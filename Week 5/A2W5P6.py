christmas_gifts = [
    "A partridge in a pear tree",
    "Two turtledoves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings (five golden rings)",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming",
]

ORDINAL_DAYS = [
    "1st", "2nd", "3rd", "4th", "5th", "6th",
    "7th", "8th", "9th", "10th", "11th", "12th",
]


def next_verse(vers_number: int) -> str:
    verse_gifts = list(reversed(christmas_gifts[:vers_number]))
    if len(verse_gifts) == 1:
        gift_text = verse_gifts[0]
    else:
        gift_text = ", ".join(verse_gifts[:-1]) + " And " + verse_gifts[-1]

    return (
        f"On the {ORDINAL_DAYS[vers_number - 1]} day of Christmas, "
        f"my true love sent to me {gift_text}"
    )


def main():
    for vers_number in range(1, 13):
        print(next_verse(vers_number))


if __name__ == "__main__":
    main()

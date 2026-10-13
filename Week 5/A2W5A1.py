import csv
import math
import re
from pathlib import Path


FIELD_NAMES = [
    "sender_firstname",
    "sender_lastname",
    "receiver_firstname",
    "receiver_lastname",
    "weight",
    "length",
    "width",
    "height",
    "street",
    "house_number",
    "postcode",
]

POSTCODE_PATTERN = re.compile(r"^\d{4}\s?[A-Za-z]{2}$")


def is_valid_name(value: str) -> bool:
    return bool(value.strip()) and all(
        character.isalpha() or character == " " for character in value
    )


def is_positive_float(value: str) -> bool:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    return math.isfinite(number) and number > 0


def is_valid_postcode(value: str) -> bool:
    return bool(POSTCODE_PATTERN.fullmatch(value.strip()))


def validate_row(row: dict[str, str]) -> list[str]:
    errors = []

    if not is_valid_name(row["sender_firstname"]) or not is_valid_name(
        row["sender_lastname"]
    ):
        errors.append("Invalid sender name")
    if not is_valid_name(row["receiver_firstname"]) or not is_valid_name(
        row["receiver_lastname"]
    ):
        errors.append("Invalid receiver name")

    for field in ("weight", "length", "width", "height"):
        if not is_positive_float(row[field]):
            errors.append(f"Invalid {field}")

    if not row["street"].strip():
        errors.append("Invalid street")
    if (
        not row["house_number"].strip()
        or not row["house_number"].strip().isdigit()
    ):
        errors.append("Invalid house number")
    if not is_valid_postcode(row["postcode"]):
        errors.append("Invalid postcode")

    return errors


def package_tuple(row: dict[str, str]) -> tuple[str, str, float]:
    volume = (
        float(row["length"])
        * float(row["width"])
        * float(row["height"])
    )
    address = f'{row["street"].strip()} {row["house_number"].strip()}'
    return row["postcode"].strip(), address, volume


def row_text(row: dict[str, str]) -> str:
    return ",".join(row[field] for field in FIELD_NAMES)


def read_rows(file_path: Path) -> list[dict[str, str]]:
    with file_path.open(newline="", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    if rows and [value.strip() for value in rows[0]] == FIELD_NAMES:
        rows = rows[1:]

    return [
        dict(zip(FIELD_NAMES, row))
        for row in rows
        if len(row) == len(FIELD_NAMES)
    ]


def process_dataset(file_path: Path) -> None:
    valid_rows = []
    organised_packages = []
    corrupt_rows = []

    for row in read_rows(file_path):
        errors = validate_row(row)
        if errors:
            corrupt_rows.append((row_text(row), errors))
        else:
            valid_rows.append(row_text(row))
            organised_packages.append(package_tuple(row))

    print("### VALID LINES ###")
    for row in valid_rows:
        print(row)

    print("--- Grouped Packages by Postcode ---")
    for postcode, address, volume in organised_packages:
        print(
            f"Postcode: {postcode}, Address: {address}, "
            f"Volume: {volume:.2f}"
        )

    print("### CORRUPT LINES ###")
    for row, errors in corrupt_rows:
        print(f"{row} --> {'; '.join(errors)}")


def main():
    csv_files = sorted(Path(__file__).parent.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(
            "No CSV dataset was found next to this program."
        )
    process_dataset(csv_files[0])


if __name__ == "__main__":
    main()

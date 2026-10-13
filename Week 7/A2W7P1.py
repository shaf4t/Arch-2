import os
import sys


MONTH_NAMES = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def load_txt_file(file_name: str) -> list[list[str]]:
    file_content = []

    file_path = os.path.join(sys.path[0], file_name)
    with open(file_path, newline="", encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


def convert_to_dict(data: list) -> dict[int, dict[int, list[float]]]:
    temperatures: dict[int, dict[int, list[float]]] = {}
    for row in data:
        if isinstance(row, str):
            values = row.replace(",", " ").split()
        else:
            values = list(row)

        if len(values) < 4:
            continue

        month, day, year, temperature = values[:4]
        temperatures.setdefault(int(year), {}).setdefault(
            int(month), []
        ).append(float(temperature))
    return temperatures


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5 / 9, 4)


def average_temp_per_month(
    temperatures_for_year: dict[int, list[float]],
) -> list[tuple[int, float]]:
    return [
        (month, sum(values) / len(values))
        for month, values in sorted(temperatures_for_year.items())
    ]


def average_temp_per_year(
    temperatures: dict[int, dict[int, list[float]]],
) -> list[tuple[int, float]]:
    yearly_averages = []
    for year, monthly_temperatures in sorted(temperatures.items()):
        values = [
            temperature
            for daily_values in monthly_temperatures.values()
            for temperature in daily_values
        ]
        yearly_averages.append((year, sum(values) / len(values)))
    return yearly_averages


def average_temp_per_month_celsius(
    temperatures_for_year: dict[int, list[float]],
) -> dict[int, float]:
    monthly_averages = average_temp_per_month(temperatures_for_year)
    return dict(
        map(
            lambda item: (item[0], fahrenheit_to_celsius(item[1])),
            monthly_averages,
        )
    )


def find_data_file() -> str:
    data_files = sorted(
        file_name
        for file_name in os.listdir(sys.path[0])
        if file_name.endswith(".txt")
    )
    if not data_files:
        raise FileNotFoundError("No temperature data file was found.")
    return data_files[0]


def print_menu() -> None:
    print(
        "[1] Print the average temperature per year (Fahrenheit)."
    )
    print("[2] Print the average temperature per year (Celsius).")
    print(
        "[3] Print the warmest and coldest year as a tuple "
        "based on the average temperature."
    )
    print(
        "[4] Print the warmest month of a year based on the input year "
        "(full month name)."
    )
    print(
        "[5] Print the coldest month of a year based on the input year "
        "(full month name)."
    )
    print(
        "[6] Print year and monthly averages in Celsius."
    )


def main() -> None:
    temperature_rows = load_txt_file(find_data_file())
    temperatures = convert_to_dict(temperature_rows)
    print_menu()
    option = input("Select an option: ")

    if option == "1":
        print(average_temp_per_year(temperatures))
    elif option == "2":
        yearly_averages = average_temp_per_year(temperatures)
        print(list(map(
            lambda item: (
                item[0],
                fahrenheit_to_celsius(item[1]),
            ),
            yearly_averages,
        )))
    elif option == "3":
        yearly_averages = average_temp_per_year(temperatures)
        warmest = max(yearly_averages, key=lambda item: item[1])[0]
        coldest = min(yearly_averages, key=lambda item: item[1])[0]
        print((warmest, coldest))
    elif option in ("4", "5"):
        year = int(input("Year: "))
        monthly_averages = average_temp_per_month(temperatures[year])
        month = (
            max(monthly_averages, key=lambda item: item[1])[0]
            if option == "4"
            else min(monthly_averages, key=lambda item: item[1])[0]
        )
        print(MONTH_NAMES[month - 1])
    elif option == "6":
        print([
            (year, average_temp_per_month_celsius(months))
            for year, months in sorted(temperatures.items())
        ])


if __name__ == "__main__":
    main()
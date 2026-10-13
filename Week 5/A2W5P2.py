def calculate_fare(distance):
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    charged_units = int((distance * 1000 + 139) // 140)
    return 4 + charged_units * 0.25


if __name__ == "__main__":
    distance = float(input("Distance traveled: "))
    print(f"Total fare: {calculate_fare(distance):.2f} EUR")
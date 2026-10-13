import random


def arithmetic_operation(arithmetic_type):
    correct_answers = 0
    mistakes = []

    for _ in range(10):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)

        if arithmetic_type == "summation":
            operator = "+"
            expected_answer = first_number + second_number
        elif arithmetic_type == "multiplication":
            operator = "*"
            expected_answer = first_number * second_number
        else:
            operator = "-"
            expected_answer = first_number - second_number

        user_answer = int(
            input(f"{first_number} {operator} {second_number} = ")
        )
        if user_answer == expected_answer:
            correct_answers += 1
        else:
            mistakes.append(
                f"{first_number} {operator} {second_number} = "
                f"{user_answer} (correct answer: {expected_answer})"
            )

    print(
        f'You had {correct_answers} correct and '
        f'{len(mistakes)} incorrect answers in "{arithmetic_type}"'
    )

    if mistakes:
        print("Mistakes:")
        for mistake in mistakes:
            print(mistake)


def main():
    while True:
        arithmetic_type = input(
            "Arithmetic operation (summation, multiplication, subtraction): "
        ).lower()
        if arithmetic_type in ("summation", "multiplication", "subtraction"):
            break
        print("Please choose summation, multiplication or subtraction.")

    arithmetic_operation(arithmetic_type)


if __name__ == "__main__":
    main()

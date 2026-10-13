import random


def generate_random_password() -> str:
    length = random.randint(7, 10)
    return "".join(chr(random.randint(33, 126)) for _ in range(length))


def main():
    print(generate_random_password())


if __name__ == "__main__":
    main()

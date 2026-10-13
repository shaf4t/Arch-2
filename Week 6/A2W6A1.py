import json
from pathlib import Path


USER_NAMES = (
    "Amina Ali", "Amina Petrov", "Anna Boer", "Anna Leeuwen",
    "Anna Meijer", "Bram Mulder", "Bram Smit", "Carlos Garcia",
    "Daan Boer", "Daan Dijk", "Emma Jong", "Emma Meijer", "Eva Berg",
    "Julia Bakker", "Julia Boer", "Julia Bos", "Kenji Nguyen",
    "Kenji Petrov", "Lars Dekker", "Lars Dijk", "Lars Smit",
    "Lisa Peters", "Lisa Visser", "Lotte Mulder", "Lucia Hernandez",
    "Lucia Martinez", "Luis Lopez", "Luuk Mulder", "Maud Jansen",
    "Milan Mulder", "Milan Visser", "Noah Leeuwen", "Raj Petrov",
    "Sara Hendriks", "Sara Meijer", "Sem Smit", "Sofia Hernandez",
    "Sophie Dijk", "Sophie Hendriks", "Sophie Visser", "Sven Meijer",
    "Tess Boer", "Tess Hendriks", "Tess Jansen", "Tess Meijer",
    "Tess Mulder", "Tess Smit", "Thijs Dekker", "Thijs Jong",
    "Thijs Visser",
)


def default_dataset() -> dict[str, set[str]]:
    network = {name: set() for name in USER_NAMES}
    network["Daan Dijk"] = {
        "Lisa Peters", "Raj Petrov", "Sara Meijer", "Thijs Jong"
    }
    candidates = {
        "Anna Meijer", "Carlos Garcia", "Emma Jong", "Eva Berg",
        "Kenji Petrov", "Lucia Hernandez", "Luis Lopez", "Milan Mulder",
        "Milan Visser", "Noah Leeuwen", "Tess Meijer", "Tess Mulder",
        "Thijs Visser",
    }
    network["Lisa Peters"] = candidates | {"Daan Dijk"}
    network["Raj Petrov"] = {
        "Eva Berg", "Lucia Hernandez", "Thijs Visser", "Daan Dijk"
    }
    return network


def load_social_network(file_path: Path) -> dict[str, set[str]]:
    if not file_path.exists():
        return default_dataset()

    with file_path.open(encoding="utf-8") as data_file:
        raw_data = json.load(data_file)

    return {
        username: set(friends)
        for username, friends in raw_data.items()
    }


read_dataset = load_social_network


def list_users(network: dict[str, set[str]]) -> str:
    users = list(network)
    return ",".join(sorted(users))


def show_friends(network: dict[str, set[str]], username: str) -> str:
    if username not in network:
        return "Error: User not found."
    if not network[username]:
        return "User has no friends."
    return ",".join(sorted(network[username]))


def recommend_friends(
    network: dict[str, set[str]], username: str
) -> list[tuple[str, int]]:
    if username not in network:
        return []

    direct_friends = network[username]
    mutual_counts: dict[str, int] = {}
    for friend in direct_friends:
        for possible_friend in network.get(friend, set()):
            if (
                possible_friend != username
                and possible_friend not in direct_friends
            ):
                mutual_counts[possible_friend] = (
                    mutual_counts.get(possible_friend, 0) + 1
                )

    return sorted(mutual_counts.items())


def print_recommendations(
    network: dict[str, set[str]], username: str
) -> None:
    if username not in network:
        print("Error: User not found.")
        return

    recommendations = recommend_friends(network, username)
    if not recommendations:
        print("No Recommendation.")
        return

    print(f"Recommended friends for {username}:")
    for name, mutual_count in recommendations:
        print(f"- {name} ({mutual_count} mutual friends)")


def main() -> None:
    file_path = Path(__file__).with_name("social_network.json")
    network = load_social_network(file_path)

    print("[L] List users (sorted alphabetically)")
    print("[S] Show friends of user (sorted alphabetically)")
    print("[R] Recommend friends (sorted alphabetically)")
    print("[Q] Quit program")
    while True:
        choice = input().strip().upper()

        if choice == "L":
            print(list_users(network))
        elif choice == "S":
            username = input("")
            print(show_friends(network, username))
        elif choice == "R":
            username = input("")
            print_recommendations(network, username)
        elif choice == "Q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
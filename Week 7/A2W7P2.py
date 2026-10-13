import csv
import os
import sys


def load_csv_file(file_name):
    file_path = os.path.join(sys.path[0], file_name)
    with open(
        file_path,
        newline="",
        encoding="utf8",
    ) as csv_file:
        return list(csv.reader(csv_file, delimiter=","))


def get_headers(file_content):
    return file_content[0] if file_content else []


def search_by_type(file_content, show_type):
    headers = get_headers(file_content)
    type_index = headers.index("type")
    return list(
        filter(
            lambda row: row[type_index].lower() == show_type.lower(),
            file_content[1:],
        )
    )


def search_by_director(file_content, director):
    headers = get_headers(file_content)
    director_index = headers.index("director")
    requested_director = director.strip().lower()
    return list(
        filter(
            lambda row: row[director_index].strip().lower()
            == requested_director,
            file_content[1:],
        )
    )


def get_directors(file_content):
    headers = get_headers(file_content)
    director_index = headers.index("director")
    directors = set()
    for row in file_content[1:]:
        director = row[director_index].strip()
        if director:
            directors.add(director)
    return directors


def director_statistics(file_content):
    headers = get_headers(file_content)
    type_index = headers.index("type")
    director_index = headers.index("director")
    directors = get_directors(file_content)
    statistics = []
    for director in directors:
        matching_rows = list(
            filter(
                lambda row: row[director_index].strip().lower()
                == director.lower(),
                file_content[1:],
            )
        )
        movies = sum(
            row[type_index].lower() == "movie"
            for row in matching_rows
        )
        tv_shows = sum(
            row[type_index].lower() == "tv show"
            for row in matching_rows
        )
        statistics.append((director, movies, tv_shows))
    return sorted(statistics)


def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else "netflix_titles.csv"
    file_content = load_csv_file(file_name)
    option = input("")

    if option == "1":
        print(len(search_by_type(file_content, "TV Show")))
    elif option == "2":
        print(len(search_by_type(file_content, "Movie")))
    elif option == "3":
        statistics = director_statistics(file_content)
        print(
            [
                director
                for director, movies, tv_shows in statistics
                if movies > 0 and tv_shows > 0
            ]
        )
    elif option == "4":
        print(director_statistics(file_content))


if __name__ == "__main__":
    main()
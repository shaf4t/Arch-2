def create_set(*args) -> list:
    my_set = []
    for item in args:
        if item not in my_set:
            my_set.append(item)
    return my_set


def has(my_set: list, item) -> bool:
    return item in my_set


def add(my_set: list, item) -> None:
    if not has(my_set, item):
        my_set.append(item)


def remove(my_set: list, item) -> None:
    if has(my_set, item):
        my_set.remove(item)


def union(my_set: list, other_set: list) -> list:
    union_set = create_set(*my_set)
    for item in other_set:
        add(union_set, item)
    return union_set


def intersect(my_set: list, other_set: list) -> list:
    intersection_set = []
    for item in my_set:
        if has(other_set, item):
            add(intersection_set, item)
    return intersection_set
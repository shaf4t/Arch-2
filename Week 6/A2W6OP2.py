from __future__ import annotations


class CustomSet:
    def __init__(self, *args):
        self.items: list = []

        for item in args:
            if item not in self.items:
                self.items.append(item)

    def has(self, item) -> bool:
        return item in self.items

    def add(self, item) -> None:
        if not self.has(item):
            self.items.append(item)

    def remove(self, item) -> None:
        if self.has(item):
            self.items.remove(item)

    def union(self, other: CustomSet) -> None:
        for item in other.items:
            self.add(item)

    def intersect(self, other: CustomSet) -> None:
        self.items = [
            item for item in self.items
            if other.has(item)
        ]

    def __len__(self) -> int:
        return len(self.items)
from dataclasses import dataclass
import datetime

items = []


@dataclass
class Todo:
    todo: str
    date: datetime
    isCompleted: bool = False


def add(text, dates):
    text = text.replace("b", "bbb").replace("B", "Bbb")
    date = datetime.datetime.strptime(dates, "%Y-%m-%d").date()
    items.append(Todo(text, date))

    items.sort(key=lambda r: r.date)


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted


def delete_all():
    items.clear()

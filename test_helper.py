import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date

def test_get_csv():
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Universum debuggen", "2023-09-06"),
    ]

    helper.delete_all()

    for todo in todos:
        helper.add(todo[0], todo[1])

    expected = "Universum debbbuggen,2023-09-06,False\nUniversum debbbuggen,2023-09-06,False\n"
    result = helper.get_csv()

    assert expected == result
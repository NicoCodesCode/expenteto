from expenteto import storage
from expenteto.expenses import (
    add_expense,
    update_expense,
    filter_expenses_by_month,
    delete_expense,
)
from datetime import date


def test_add_expense_appends_to_list(monkeypatch, tmp_path):
    monkeypatch.setattr(storage, "EXPENSES_FILE", tmp_path / "test_expenses.json")

    expense_list = []
    add_expense("coffee", 5, expense_list)

    assert len(expense_list) == 1
    assert expense_list[0]["description"] == "coffee"
    assert expense_list[0]["amount"] == 5


def test_add_expense_rejects_negative_amount(monkeypatch, tmp_path):
    monkeypatch.setattr(storage, "EXPENSES_FILE", tmp_path / "test_expenses.json")

    expense_list = []
    add_expense("coffee", -5, expense_list)

    assert len(expense_list) == 0


def test_update_expense_allows_zero_amount(monkeypatch, tmp_path):
    monkeypatch.setattr(storage, "EXPENSES_FILE", tmp_path / "test_expenses.json")

    expense_list = [
        {"id": 1, "description": "coffee", "amount": 5, "date": "2026-01-01"}
    ]
    update_expense(1, None, 0, expense_list)

    assert expense_list[0]["amount"] == 0


def test_filter_by_month_excludes_different_year():
    expense_list = [
        {"id": 1, "description": "old", "amount": 10, "date": "2020-03-15"},
        {
            "id": 2,
            "description": "new",
            "amount": 20,
            "date": f"{date.today().year}-03-15",
        },
    ]
    result = filter_expenses_by_month(3, expense_list)
    assert len(result) == 1
    assert result[0]["description"] == "new"


def test_delete_expenses(monkeypatch, tmp_path):
    monkeypatch.setattr(storage, "EXPENSES_FILE", tmp_path / "test_expenses.json")

    expense_list = [
        {"id": 1, "description": "coffee", "amount": 5, "date": "2026-01-01"}
    ]
    delete_expense(1, expense_list)

    assert len(expense_list) == 0

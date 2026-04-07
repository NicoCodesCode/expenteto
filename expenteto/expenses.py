from expenteto.storage import write_file
from datetime import date


def add_expense(description, amount, expense_list):
    if amount < 0 and not description.strip():
        print("Description or amount is invalid")
        return

    id = max((expense["id"] for expense in expense_list), default=0) + 1
    new_expense = {
        "id": id,
        "description": description,
        "amount": amount,
        "date": date.today().isoformat(),
    }
    expense_list.append(new_expense)

    if write_file(expense_list):
        print(f"{description} was added to the list")


def list_expenses(expense_list):
    print(f"{'ID':<12}{'Description':<21}{'Amount':<10}")
    for expense in expense_list:
        print(f"{expense['id']:<12}{expense['description']:<21}{expense['amount']:<10}")


def filter_expenses_by_month(month, expense_list):
    current_year = date.today().year
    return [
        expense
        for expense in expense_list
        if (expense_date := date.fromisoformat(expense["date"])).month == month
        and expense_date.year == current_year
    ]


def summary_expenses(expense_list):
    summary = sum(expense["amount"] for expense in expense_list)
    print(f"Total expenses: ${summary}")


def find_expense_by_id(expense_id, expense_list):
    return next(
        (expense for expense in expense_list if expense["id"] == expense_id),
        None,
    )


def update_expense(expense_id, new_description, new_amount, expense_list):
    expense = find_expense_by_id(expense_id, expense_list)

    if not expense:
        print(f"There is no expense with ID {expense_id}")
        return

    if new_description:
        expense["description"] = new_description
    if new_amount:
        expense["amount"] = new_amount

    if write_file(expense_list):
        print("The expense was successfully updated")

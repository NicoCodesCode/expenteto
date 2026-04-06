from expenteto.storage import write_file
from datetime import date


def add_expense(description, amount, expense_list):
    if amount > 0 and description.strip():
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
    else:
        print("Description or amount is invalid")


def list_expenses(expense_list):
    if len(expense_list):
        print(f"{'ID':<12}{'Description':<21}{'Amount':<10}")
        for expense in expense_list:
            print(
                f"{expense['id']:<12}{expense['description']:<21}{expense['amount']:<10}"
            )


def list_expenses_by_month(month, expense_list):
    if month in range(1, 12):
        current_year = date.today().year

        filtered_list = [
            expense
            for expense in expense_list
            if (expense_date := date.fromisoformat(expense["date"])).month == month
            and expense_date.year == current_year
        ]

        list_expenses(filtered_list)
    else:
        print("Please provide a valid month (1-12)")

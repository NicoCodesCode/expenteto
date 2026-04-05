from expenteto.storage import write_file


def add_expense(description, amount, expense_list):
    id = max((expense["id"] for expense in expense_list), default=0) + 1
    new_expense = {"id": id, "description": description, "amount": amount}
    expense_list.append(new_expense)

    if write_file(expense_list):
        print(f"{description} was added to the list")

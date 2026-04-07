import argparse
from expenteto.storage import load_file
from expenteto.expenses import *


def main():
    expense_list = load_file()

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title="Actions", dest="action")

    add_parser = subparsers.add_parser(
        "add", help="add an expense with description and amount"
    )
    add_parser.add_argument(
        "-d", "--description", required=True, help="a short description of the expense"
    )
    add_parser.add_argument(
        "-a", "--amount", type=int, required=True, help="the amount of the expense"
    )

    list_parser = subparsers.add_parser("list", help="list all the expenses")
    list_parser.add_argument(
        "-m",
        "--month",
        choices=range(1, 13),
        metavar="MONTH",
        type=int,
        help="list all the expenses of a certain month",
    )

    subparsers.add_parser("summary", help="show a summary of the expenses")

    update_parser = subparsers.add_parser("update", help="update an expense")
    update_parser.add_argument(
        "--id", type=int, required=True, help="the ID of the expense"
    )
    update_parser.add_argument(
        "-d", "--description", help="a short description of the expense"
    )
    update_parser.add_argument(
        "-a", "--amount", type=int, help="the amount of the expense"
    )

    delete_parser = subparsers.add_parser("delete", help="delete an expense")
    delete_parser.add_argument(
        "--id", type=int, required=True, help="the ID of the expense"
    )

    args = parser.parse_args()

    if args.action == "add":
        add_expense(args.description, args.amount, expense_list)
    elif args.action == "list":
        if not expense_list:
            print("The list is empty")
        elif args.month:
            list_expenses_by_month(args.month, expense_list)
        else:
            list_expenses(expense_list)
    elif args.action == "summary":
        if not expense_list:
            print("The list is empty")
        else:
            summary_expenses(expense_list)

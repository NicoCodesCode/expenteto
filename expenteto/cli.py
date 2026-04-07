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
        "-s", "--summary", action="store_true", help="show a summary of the expenses"
    )
    list_parser.add_argument(
        "-m",
        "--month",
        choices=range(1, 13),
        metavar="MONTH",
        type=int,
        help="list all the expenses of a certain month",
    )

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
        else:
            target_list = (
                filter_expenses_by_month(args.month, expense_list)
                if args.month
                else expense_list
            )

            if not target_list:
                print("There are no expenses for that month")
            else:
                handler = summary_expenses if args.summary else list_expenses
                handler(target_list)
    elif args.action == "update":
        if not any((args.description, args.amount)):
            print("Provide at least a new description or a new amount")
        else:
            update_expense(args.id, args.description, args.amount, expense_list)
    else:
        parser.print_help()

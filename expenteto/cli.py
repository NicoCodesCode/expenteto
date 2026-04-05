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
        "-a", "--amount", required=True, help="the amount of the expense"
    )

    list_parser = subparsers.add_parser("list", help="list all the expenses")
    list_parser.add_argument(
        "-m", "--month", type=int, help="list all the expenses of a certain month"
    )

    summary_parser = subparsers.add_parser(
        "summary", help="show a summary of the expenses"
    )
    summary_parser.add_argument(
        "-m",
        "--month",
        type=int,
        help="show a summary of the expenses of a certain month (of current year)",
    )

    update_parser = subparsers.add_parser("update", help="update an expense")
    update_parser.add_argument(
        "--id", type=int, required=True, help="the ID of the expense"
    )
    update_parser.add_argument(
        "-d", "--description", help="a short description of the expense"
    )
    update_parser.add_argument("-a", "--amount", help="the amount of the expense")

    delete_parser = subparsers.add_parser("delete", help="delete an expense")
    delete_parser.add_argument(
        "--id", type=int, required=True, help="the ID of the expense"
    )

    args = parser.parse_args()

    if args.action == "add":
        add_expense(args.description, args.amount, expense_list)

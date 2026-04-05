import json

EXPENSES_FILE = "expense_list.json"


def write_file(expense_list):
    try:
        with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
            json.dump(expense_list, f, ensure_ascii=False, indent=4)
        return True
    except OSError as e:
        print(f"Error saving expenses: {e}")
        return False


def load_file():
    try:
        with open(EXPENSES_FILE) as f:
            expense_list = json.load(f)
            return expense_list
    except (FileNotFoundError, json.JSONDecodeError):
        return []

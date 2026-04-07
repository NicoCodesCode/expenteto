# expenteto

A simple command-line expense tracker that stores your expenses in a JSON file.

Project made for: https://roadmap.sh/projects/expense-tracker

## Installation

```bash
git clone https://github.com/yourusername/expenteto.git
cd expenteto
pip install -e .
```

## Usage

```bash
expenteto <action> [options]
```

## Actions

### Add an expense

```bash
expenteto add -d <description> -a <amount>
```

| Flag                  | Description                                       |
| --------------------- | ------------------------------------------------- |
| `-d`, `--description` | Short description of the expense (required)       |
| `-a`, `--amount`      | Amount of the expense in whole numbers (required) |

**Example:**

```bash
expenteto add -d "Grocery shopping" -a 50
```

---

### List expenses

```bash
expenteto list [options]
```

| Flag              | Description                         |
| ----------------- | ----------------------------------- |
| `-s`, `--summary` | Show total sum instead of full list |
| `-m`, `--month`   | Filter by month number (1-12)       |

**Examples:**

```bash
# List all expenses
expenteto list

# Show total of all expenses
expenteto list --summary

# List expenses for March
expenteto list --month 3

# Show total for March
expenteto list --month 3 --summary
```

---

### Update an expense

```bash
expenteto update --id <id> [options]
```

| Flag                  | Description                            |
| --------------------- | -------------------------------------- |
| `--id`                | ID of the expense to update (required) |
| `-d`, `--description` | New description                        |
| `-a`, `--amount`      | New amount                             |

At least one of `--description` or `--amount` must be provided.

**Example:**

```bash
expenteto update --id 3 -d "Supermarket" -a 60
```

---

### Delete an expense

```bash
expenteto delete --id <id>
```

| Flag   | Description                            |
| ------ | -------------------------------------- |
| `--id` | ID of the expense to delete (required) |

**Example:**

```bash
expenteto delete --id 3
```

---

## Data Storage

Expenses are stored locally in a JSON file. Each expense contains an ID, description, amount, and date.

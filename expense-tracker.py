import argparse

from ExpenseFunctions import *

# Map month names to their numeric values
MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}


def parse_month(month):
    # Convert month name to numeric value
    if isinstance(month, str) and month.lower() in MONTHS:
        return MONTHS[month.lower()]
    # Return the month as an integer if it's already numeric
    return int(month)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="""
📒 Expense Tracker CLI Tool

Track your daily expenses easily via the command line.
You can add, delete, update, view summaries, and even export your data.

Choose one of the subcommands below to get started.
""",
        epilog="""
📌 Example Usage:

  $ python expense-tracker.py add --description "Lunch" --amount 12.50 --category Food
  $ python expense-tracker.py list
  $ python expense-tracker.py delete --id 3
  $ python expense-tracker.py summary
  $ python expense-tracker.py summary --month 7
  $ python expense-tracker.py check-budget-monthly --month 7 --budget 500
  $ python expense-tracker.py export

💡 Tip: Use --help after any command to see its arguments, e.g.:
  $ python expense-tracker.py add --help
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense (e.g., "Lunch")')
    add_parser.add_argument('--amount', required=True, type=float, help='Amount spent (e.g., 12.5)')
    add_parser.add_argument('--category', required=True, help='Category name (e.g., Food, Transport)')

    # List
    subparsers.add_parser('list', help='Lists all recorded expenses')

    # Delete
    delete_parser = subparsers.add_parser('delete', help='Delete an expense by ID')
    delete_parser.add_argument('--id', required=True, help='ID of the expense to delete')

    # Summary
    summary_parser = subparsers.add_parser('summary', help='View a total expense summary')
    summary_parser.add_argument('--month', type=str, help='(Optional) Month name or number to filter by')

    # Update
    update_parser = subparsers.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('--id', required=True)
    update_parser.add_argument('--description', required=True)
    update_parser.add_argument('--amount', required=True, type=float)
    update_parser.add_argument('--category', required=True)

    # Export
    subparsers.add_parser('export', help='Export all expenses to a CSV file')

    # Filter by category
    filter_parser = subparsers.add_parser('filter-category', help='Show expenses in a specific category')
    filter_parser.add_argument('--category', required=True)

    # Check budget
    budget_parser = subparsers.add_parser('check-budget-monthly', help='Check if expenses exceed a monthly budget')
    budget_parser.add_argument('--month', required=True)
    budget_parser.add_argument('--budget', required=True, type=float)

    # Set threshold
    threshold_parser = subparsers.add_parser('set-threshold', help='Set a spending warning threshold')
    threshold_parser.add_argument('--threshold', required=True, type=float)

    args = parser.parse_args()

    # === Command Handling ===

    if args.command == 'add':
        ExpenseFunctions.add_expense(args.description, args.amount, args.category)

    elif args.command == 'list':
        expenses = ExpenseFunctions.view_expenses()
        print(f"  ID   Description, Amount, Category, Date")
        for expense in expenses:
            print(f"{expense.id} {expense.description}, {expense.amount}, {expense.category}, {expense.date}")

    elif args.command == 'delete':
        ExpenseFunctions.delete_expense(args.id)

    elif args.command == 'summary':
        if args.month:
            try:
                month = parse_month(args.month)
                summary = ExpenseFunctions.summary_by_month(month)
                print(f"Total Amount for {args.month}: {summary['total_amount']}")
            except ValueError:
                print("Invalid month value. Please provide a valid month name or number.")
        else:
            summary = ExpenseFunctions.summary()
            print(f"Total Amount: {summary['total_amount']}")

    elif args.command == 'update':
        ExpenseFunctions.update(args.id, args.description, args.amount, args.category)
        print("Expense updated successfully.")

    elif args.command == 'export':
        ExpenseFunctions.export_expenses_as_csv()

    elif args.command == 'filter-category':
        expenses = ExpenseFunctions.filter_expenses_by_category(args.category)
        for expense in expenses:
            print(f"{expense.id}: {expense.description}, {expense.amount}, {expense.category}, {expense.date}")

    elif args.command == 'check-budget-monthly':
        if ExpenseFunctions.check_budget_by_month(args.month, args.budget):
            print(f"Expenses are within the budget for month {args.month}.")
        else:
            print(f"Expenses exceed the budget for month {args.month}.")

    elif args.command == 'set-threshold':
        ExpenseFunctions.set_threshold(args.threshold)

    else:
        parser.print_help()
    ExpenseFunctions.check_and_warn(ExpenseFunctions.get_threshold())

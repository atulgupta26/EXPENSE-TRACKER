import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.date.today()

    def __repr__(self):
        return f"{self.date} | {self.category} | ${self.amount:.2f} | {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)

    def summary_by_category(self):
        summary = {}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        return summary

    def total_expenses(self):
        return sum(exp.amount for exp in self.expenses)

    def show_expenses(self):
        for exp in self.expenses:
            print(exp)

    def show_summary(self):
        print("\nExpense Summary by Category:")
        for cat, amt in self.summary_by_category().items():
            print(f"{cat}: ${amt:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")

def main():
    tracker = ExpenseTracker()
    print("Simple Expense Tracker")
    while True:
        print("\n1. Add Expense\n2. Show Expenses\n3. Show Summary\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            try:
                amount = float(input("Amount: $"))
                category = input("Category: ")
                description = input("Description: ")
                tracker.add_expense(amount, category, description)
                print("Expense added.")
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            tracker.show_expenses()
        elif choice == '3':
            tracker.show_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
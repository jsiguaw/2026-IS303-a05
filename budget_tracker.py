"""
Joel Siguaw
IS 303 - A05

Budget Tracker
This program helps you create a budget. Users can add expenses, and see their total spending, 
remaining balance, if they are overbudget, and what their largest expense was.

Inputs:
- Expense name, amount, category
- Budget name

Processes:
- Expense class: stores name, amount, and category, displays expense
- Budget class: stores name, budget amount, adds expenses, finds total, finds remaining balance,
checks if over budget, checks for largest expesnse, displays budget summary
  
Outputs:
- Budget summary: budget name, budget amount, all expenses, total spend, remaining balance, 
over budget (yes/no), largest expense
"""

class Budget:

    def __init__(self, budget_name, budget_amount):
        self.budget_name = budget_name
        self.budget_amount = budget_amount
        self.expenses = []

    def __str__(self):
        return (
            f"--- {self.budget_name} Summary ---\n"
            f"Budget amount: ${self.budget_amount:.2f}\n"
            f"Total spent: ${self.total_spent():.2f}\n"
            f"Remaining balance: ${self.remaining_balance():.2f}\n"
            f"Within budget: {'Yes' if self.within_budget() else 'No'}\n"
            f"Largest Expense: {self.largest_expense()}\n"
            )
    
    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_spent(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    
    def remaining_balance(self):
        remaining_balance = self.budget_amount - self.total_spent()
        return remaining_balance
    
    def within_budget(self):
        if self.total_spent() > self.budget_amount:
            return False
        else: 
            return True
        
    def largest_expense(self):
        if not self.expenses:
            return "No expense added"
        largest = self.expenses[0]
        for expense in self.expenses:
            if expense.amount > largest.amount:
                largest = expense
        return f"{largest.name} - ${largest.amount:.2f}"

class Expense:

    def __init__(self, expense, amount, category):
        self.name = expense
        self.amount = amount
        self.category = category

    def __str__(self):
        return (
            f"Expense: {self.name}\n"
            f"Amount: ${self.amount:.2f}\n"
            f"Category: {self.category}"
        )

# Main flow

budget_1 = Budget("Monthly", 3500)

expense_1 = Expense("Rent", 800, "Housing")
expense_2 = Expense("Costco", 400, "Groceries")
expense_3 = Expense("Car payment", 350, "Transportation")
expense_4 = Expense("Date night", 127, "Entertainment")
expense_5 = Expense("Travel", 3000, "Travel")
expense_6 = Expense("Gas", 650, "Transportation")

budget_1.add_expense(expense_1)
budget_1.add_expense(expense_2)
budget_1.add_expense(expense_3)
budget_1.add_expense(expense_4)
budget_1.add_expense(expense_5)
budget_1.add_expense(expense_6)

print(budget_1)
print("--- Expense List ---")
for expense in budget_1.expenses:
    print(expense)
    print("--------------------")

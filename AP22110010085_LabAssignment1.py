class FinanceAgent:
    def __init__(self):
        self.income = 0
        self.expenses = {"Essentials": 0, "Discretionary": 0, "Savings": 0}
        self.savings_goal = 0
    
    def set_income(self, amount):
        self.income = amount
    
    def set_savings_goal(self, amount):
        self.savings_goal = amount
    
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            print("Invalid category. Choose from Essentials, Discretionary, or Savings.")
    
    def calculate_budget(self):
        total_expenses = sum(self.expenses.values())
        remaining = self.income - total_expenses
        return total_expenses, remaining
    
    def recommend_savings(self):
        _, remaining_budget = self.calculate_budget()
        if remaining_budget > self.savings_goal:
            return f"You have enough to save ${self.savings_goal:.2f} this month."
        elif remaining_budget > 0:
            return f"You can save ${remaining_budget:.2f}, but consider reducing expenses to meet your goal of ${self.savings_goal:.2f}."
        else:
            return "Your expenses exceed your income. Consider adjusting your budget to save."
    
    def provide_budgeting_suggestions(self):
        suggestions = []
        if self.income > 0:
            if self.expenses["Essentials"] > self.income * 0.5:
                suggestions.append("Reduce spending on essential expenses like rent and utilities.")
            if self.expenses["Discretionary"] > self.income * 0.3:
                suggestions.append("Cut back on non-essential expenses like entertainment and dining out.")
            if self.savings_goal > 0 and self.expenses["Savings"] < self.savings_goal:
                suggestions.append("Increase your savings contribution to reach your goal.")
        return suggestions if suggestions else ["Your budget looks balanced!"]
    
    def display_summary(self):
        total_expenses, remaining_budget = self.calculate_budget()
        print(f"Income: {self.income}")
        print(f"Total Expenses: {total_expenses}")
        print("Expenses Breakdown:")
        for category, amount in self.expenses.items():
            print(f"  {category}: ${amount:.2f}")
        print(f"Remaining Budget: {remaining_budget}")
        print(self.recommend_savings())
        print("Budgeting Suggestions:")
        for suggestion in self.provide_budgeting_suggestions():
            print(f"  - {suggestion}")

if __name__ == "__main__":
    agent = FinanceAgent()
    agent.set_income(float(input("Enter your monthly income: ")))
    agent.set_savings_goal(float(input("Enter your monthly savings goal: ")))
    categories = ["Essentials", "Discretionary", "Savings"]
    while True:
        print("Select an expense category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        choice = input("Enter the number (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            amount = float(input("Enter expense amount: "))
            agent.add_expense(category, amount)
        else:
            print("Invalid choice. Please select a valid category.")
    agent.display_summary()


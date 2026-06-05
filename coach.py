import json
from datetime import datetime
from collections import defaultdict

class AIFinanceCoach:

    def __init__(self):
        self.expenses = []

    def add_expense(self):

        category = input("Category: ")
        amount = float(input("Amount (₹): "))
        note = input("Description: ")

        self.expenses.append({
            "category": category,
            "amount": amount,
            "note": note,
            "date": str(datetime.now().date())
        })

        print("Expense Added Successfully.\n")

    def spending_report(self):

        if not self.expenses:
            print("No expenses found.")
            return

        total = sum(x["amount"] for x in self.expenses)

        print("\n========== REPORT ==========")
        print(f"Total Spending: ₹{total:.2f}")

        category_totals = defaultdict(float)

        for expense in self.expenses:
            category_totals[expense["category"]] += expense["amount"]

        print("\nCategory Breakdown:")

        for category, amount in category_totals.items():
            percentage = (amount / total) * 100

            print(
                f"{category}: ₹{amount:.2f} "
                f"({percentage:.1f}%)"
            )

    def financial_health_score(self):

        if not self.expenses:
            print("No data available.")
            return

        total = sum(x["amount"] for x in self.expenses)

        score = 100

        if total > 50000:
            score -= 30

        elif total > 25000:
            score -= 15

        categories = set(
            x["category"] for x in self.expenses
        )

        if len(categories) > 5:
            score -= 10

        score = max(score, 0)

        print(f"\nFinancial Health Score: {score}/100")

    def spending_prediction(self):

        if len(self.expenses) < 5:
            print(
                "Need at least 5 expenses "
                "for prediction."
            )
            return

        average = (
            sum(x["amount"] for x in self.expenses)
            / len(self.expenses)
        )

        predicted_month = average * 30

        print(
            f"\nPredicted Monthly Spending:"
            f" ₹{predicted_month:.2f}"
        )

    def ai_advice(self):

        if not self.expenses:
            return

        category_totals = defaultdict(float)

        for expense in self.expenses:
            category_totals[
                expense["category"]
            ] += expense["amount"]

        highest = max(
            category_totals,
            key=category_totals.get
        )

        print("\n========== AI COACH ==========")

        print(
            f"You spend the most on "
            f"{highest}."
        )

        if category_totals[highest] > 10000:

            print(
                f"Consider reducing "
                f"{highest} expenses "
                f"by 15-20%."
            )

        print(
            "Aim to save at least "
            "20% of your income."
        )

    def save_data(self):

        with open(
            "finance_data.json",
            "w"
        ) as file:

            json.dump(
                self.expenses,
                file,
                indent=4
            )

        print("Data Saved.")

    def load_data(self):

        try:
            with open(
                "finance_data.json",
                "r"
            ) as file:

                self.expenses = json.load(file)

        except:
            pass

coach = AIFinanceCoach()
coach.load_data()

while True:

    print("\n===== AI FINANCE COACH =====")

    print("1. Add Expense")
    print("2. Spending Report")
    print("3. Financial Health Score")
    print("4. Spending Prediction")
    print("5. AI Advice")
    print("6. Save & Exit")

    choice = input("Choose: ")

    if choice == "1":
        coach.add_expense()

    elif choice == "2":
        coach.spending_report()

    elif choice == "3":
        coach.financial_health_score()

    elif choice == "4":
        coach.spending_prediction()

    elif choice == "5":
        coach.ai_advice()

    elif choice == "6":
        coach.save_data()
        break

    else:
        print("Invalid Option")

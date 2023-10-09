class MonthBudget:
    def __init__(self):
        # Spending
        self.rent = 0.0  # House
        self.carInsurance = 0.0  # Car
        self.electricity = 0.0  # House
        self.otherUtilities = 0.0  # House
        self.wiFi = 0.0  # House
        self.groceries = 0.0  # House
        self.foodEntertainment = 0.0  # Personal
        self.funEntertainment = 0.0  # Personal
        self.gas = 0.0  # Car
        self.debt = 0.0  # Personal
        self.phone = 0.0  # Personal
        self.gym = 0.0  # Personal
        self.emma = 0.0
        self.savings = 0.0
        self.income = 0.0

    def set_income(self):
        self.income = float(input("How much money do you have this month? "))
        self.savings = float(input("What percentage of that would you like to save? (ENTER AS DECIMAL) "))
        print()

    def set_vehicle_expenses(self):
        self.carInsurance = 120.00

        miles_drive = (5 * 60) + (2 * 50)
        mpg = 30.0
        gallons = miles_drive / mpg
        self.gas = 4 * (gallons * 3.00)

        total_vehicle = self.carInsurance + self.gas
        return total_vehicle

    def set_housing_expenses(self):
        self.electricity = 100.00  # 100
        self.wiFi = 60.00  # 60
        self.otherUtilities = 50.00  # 50
        self.groceries = 500.00  # Split-ish? # 400
        total_housing = self.electricity + self.wiFi + self.otherUtilities + self.groceries
        return total_housing

    def set_personal_expenses(self):
        self.foodEntertainment = 350.00  # 350
        self.funEntertainment = 150.00  # 150
        self.emma = 50.00
        self.debt = 250.00  # 250
        self.phone = 10.00  # 10
        self.gym = 200.00  # 200
        total_personal = self.foodEntertainment + self.funEntertainment + self.debt + self.phone + self.gym + self.emma
        return total_personal

    def calc_remainder(self, veh, hou, per):
        remainder = self.income * (1 - self.savings)
        remainder = remainder - veh - hou - per
        return remainder

    def calc_rent(self, remainder):
        print("I can spend up to:", remainder, "on rent\n")


def main():
    month = MonthBudget()
    month.set_income()
    vehicle_expenses = month.set_vehicle_expenses()
    housing_expenses = month.set_housing_expenses()
    personal_expenses = month.set_personal_expenses()
    remainder = month.calc_remainder(vehicle_expenses, housing_expenses, personal_expenses)
    month.calc_rent(remainder)
    print("Saving: $", month.income * month.savings, "per month\n")


if __name__ == "__main__":
    main()

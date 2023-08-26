def find_months(annual_salary, portion_saved, total_cost):
    current_saving = 0
    monthly_salary = annual_salary / 12
    r_invest = 0.04
    portion_down_payment = total_cost * 0.25

    months_cnt = 0
    while current_saving < portion_down_payment:
        current_saving += current_saving * (r_invest / 12)
        current_saving += monthly_salary * portion_saved
        months_cnt += 1
    return months_cnt

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
num_months = find_months(annual_salary, portion_saved, total_cost)
print("Number of months: ", num_months)
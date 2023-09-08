def fct(annual_salary, portion_saved, total_cost, semi_annual_raise):
    current_saving = 0
    monthly_salary = annual_salary / 12
    r_invest = 0.04
    portion_down_payment = total_cost * 0.25
    month = 0
    while current_saving < portion_down_payment:
        current_saving += current_saving * (r_invest / 12)
        current_saving += monthly_salary * portion_saved
        month += 1
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    return month

def search_portion_saved(annual_salary):
    semi_annual_raise = .07
    total_cost = 1000000
    left = 0
    right = annual_salary
    months = 0
    while left <= right:
        mid = (left + right) // 2
        portion_saved = mid / annual_salary
        months = fct(annual_salary, portion_saved, total_cost, semi_annual_raise)
        if months <= 36:
            right = mid - 1
        else:
            left = mid + 1
    if months > 36:
        return -1
    return left / annual_salary

saving_rate = search_portion_saved(10000)
if saving_rate != -1:
    print("Best savings rate:", saving_rate)
else:
    print("It is not possible to pay the down payment in three years.")


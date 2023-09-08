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

print(fct(120000, .05, 500000, .03))
print(fct(80000, .1, 800000, .03))
print(fct(75000, .05, 1500000, .05))
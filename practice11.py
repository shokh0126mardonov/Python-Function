def calculate_tax(salary: float):
    if salary > 5_000_000:
        foiz = salary * 0.2
        return foiz
    else:
        foiz = salary * 0.13
    return foiz 

def calculate_net_salary(salary: float):
    sof_oylik = salary - calculate_tax(salary)
    return sof_oylik


salary = float(input("Oylik maoshingizni kiriting: "))

result = f"maoshingiz = {salary} soliq = {calculate_tax(salary)} va sof maoshingiz = {calculate_net_salary(salary)}"

print(result)


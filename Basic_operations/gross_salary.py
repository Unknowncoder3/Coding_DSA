# gross salary calculation
basic_salary=float(input("Enter the basic salary: "))
hra=0.20 * basic_salary
da=0.10 * basic_salary
gross_salary=basic_salary + hra + da
print("The gross salary is:", gross_salary)
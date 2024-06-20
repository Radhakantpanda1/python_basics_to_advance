# simple income tax calculation based upon income/salary

user_salary=int(input("Enter your salary- "))
if(user_salary>=0 and user_salary<=500000):
    income_tax_percentage=0
    print("Amount to be paid =",0)
elif (user_salary>500000 and user_salary<=1000000):
    income_tax_percentage=10
    tax_to_be_paid=(10/100)*user_salary
    print("Amount to be paid =",tax_to_be_paid)
elif(user_salary>1000000 and user_salary<=1500000):
    income_tax_percentage=15
    tax_to_be_paid=(15/100)*user_salary
    print("Amount to be paid =",tax_to_be_paid)
elif(user_salary>1500000 and user_salary<=10000000):
    income_tax_percentage=30
    tax_to_be_paid=(30/100)*user_salary
    print("Amount to be paid =",tax_to_be_paid)
else:
    income_tax_percentage=35
    tax_to_be_paid=(30/100)*user_salary
    print("Amount to be paid =",tax_to_be_paid)


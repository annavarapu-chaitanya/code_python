age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: $"))

if age >= 18:
    
    if salary >= 3000:
        print("Congratulations! You are eligible for a loan.")
    else:
        print("Loan denied: Salary is too low.")
else:
    print("Loan denied: You must be at least 18 years old.")

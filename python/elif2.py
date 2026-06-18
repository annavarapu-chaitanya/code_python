age = int(input("Enter the person's age: "))

if age < 0:
    print("Invalid age entered.")
elif age <= 12:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
else:
    print("Category: Adult")

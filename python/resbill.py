bill = 0

while True:
    print("\n1. Idli - 30")
    print("2. Dosa - 50")
    print("3. Biryani - 150")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bill += 30
        print("Idli Added")

    elif choice == 2:
        bill += 50
        print("Dosa Added")

    elif choice == 3:
        bill += 150
        print("Biryani Added")

    elif choice == 4:
        print("Total Bill =", bill)
        break

    else:
        print("Invalid Choice")

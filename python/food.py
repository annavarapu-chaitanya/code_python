km = int(input("Enter Distance: "))

if 1 <= km <= 9:
    amount = km * 10

elif 10 <= km <= 20:
    amount = (9 * 10) + ((km - 9) * 15)

elif 21 <= km <= 30:
    amount = (9 * 10) + (11 * 15) + ((km - 20) * 20)

elif 31 <= km <= 50:
    amount = (9 * 10) + (11 * 15) + (10 * 20) + ((km - 30) * 22)

else:
    print("Service Not Available")
    exit()

print("Auto Fare =", amount)

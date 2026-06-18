km = int(input("Enter Distance: "))
food = int(input("Enter Food Charge: "))

if 1 <= km <= 50:
    amount = (km * 17) + 200

elif 51 <= km <= 100:
    amount = (50 * 17) + ((km - 50) * 21) + 300 + food

elif 101 <= km <= 160:
    amount = (50 * 17) + (50 * 21) + ((km - 100) * 30) + 300 + food

elif 161 <= km <= 200:
    amount = (50 * 17) + (50 * 21) + (60 * 30) + ((km - 160) * 33) + 300 + food

else:
    print("Service Not Available")
    exit()

print("Car Fare =", amount)

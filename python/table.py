n = int(input("Enter N: "))
upto = int(input("Enter Upto: "))

for i in range(1, n + 1):
    print("\nTable of", i)

    for j in range(1, upto + 1):
        print(i, "*", j, "=", i * j)

l = [100, 20, 30, 120, 11, 13]

least = l[0]

for i in range(len(l)):
    if l[i] < least:
        least = l[i]

print("Least Element =", least)

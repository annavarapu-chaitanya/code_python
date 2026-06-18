l = ["abcde", "ab", "abc", "abcd"]

largest = l[0]

for i in l:
    if len(i) > len(largest):
        largest = i

print(largest)

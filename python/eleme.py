l = ["abcde", "ab", "abc", "abcd"]

max_len = len(l[0])

for i in l:
    if len(i) > max_len:
        max_len = len(i)

print(max_len)

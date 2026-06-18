x=["a","ab","sai","john","codegnan"]
g=0
wor=""
for i in x:
    if len(i)>g:
        g=len(i)
        wor=i
print(wor)
print(g)

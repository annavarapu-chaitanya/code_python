x="beautiful"
emp={}
for i in x:
    if i not in emp:
        emp[i]=1
    else:
        emp[i]+=1
print(emp)

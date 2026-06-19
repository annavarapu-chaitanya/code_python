def Details(name,marks,age,institute="codegnan"):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"marks:{marks}")
    print(f"institute:{institute}")
    
    
# Details("ramu",123,14)
# Details(432,12,"john")

# Details(age=34,name="kaleem",marks=345)
# print()
# Details("janu",345,34,"Techgnan")

n=input()
m=int(input())
a=int(input())
Details(n,m,a)
Details(name=n,age=a,marks=m)

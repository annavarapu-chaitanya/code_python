print("1.withdraw\n2.add\n3.check")
balance=1000
while True:
    n=int(input("choose the option:"))
    if n==1:
        amount=int(input())
        balance-=amount
        print(balance)
    elif n==2:
        amount=int(input())
        balance+=amount
        
        print(balance)
    else:
        print("Thank you")
        break

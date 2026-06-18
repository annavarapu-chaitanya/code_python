kms=int(input())
if kms>0 and kms<=5:
    price=5
    print(price,"is your amount")
elif kms>=6 and kms<=12:
    price=5+6
    print(price,"is your amount")
elif kms>=13 and kms<=20:
    price=5+6+8
    print(price,"is your amount")
elif kms>=21 and kms<=30:
    price=5+6+9+10
    print(price,"is your amount")
elif kms>=30:
    print("ride is not available")

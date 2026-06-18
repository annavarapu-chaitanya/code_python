s="madam"
x=""
for i in range(len(s)-1,-1,-1):
    x+=s[i]
  
print(x,s)
if x==s:
    print("palindrome")
    
else:
    print("not palindrome")

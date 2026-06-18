a=input()
v='aeiouAEIOU'
count1=0
count2=0
for i in a:
  if i in v:
    count1+=1
  else:
    count2+=1
print("vowels:",count1)
print("consonants:",count2)

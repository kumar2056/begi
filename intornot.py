#
s=[]
a=input()
b=0
for i in a:
  s.append(i)
#print(s)
for i in range(0,len(s)):
  if((s[i]>='a')and(s[i]<='z')):
    b=1
if(b==1):
  print("no")
else:
  print("yes")

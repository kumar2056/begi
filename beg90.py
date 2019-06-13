#
a=input()
s1=[]
c=0
for i in a:
  if i<='9' and i>='0':
    s1.append(i)
    c=1
if c==1:
  for i in s1:
    print(i,end="")
else:
  print(end="")

c=int(input())
d=0
for x in range(1,c+1):
  if(c%x==0):
    d=d+1
if(d==2):
  print("yes")
else:
  print("no")

k,l=input().split()
a=int(k)
c=int(l)
for x in range(a+1,c): 
  b=0
  for y in range(1,c):
    if(x%y==0):
      b=b+1
  if(b==2):
    print(x,end=" ")

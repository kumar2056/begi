m,n=input().split()
a=int(m)
b=int(n)
for l in range(a,b):
  su=0
  h=l
  while(l!=0):
    rem=l%10
    su=su+rem*rem*rem
    l=l//10
  if (h==su):
    print(h,end=" ")

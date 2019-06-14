#
s=[]
i,j=input().split()
a=int(i)
b=int(j)
for i in range(1,a+1):
  if((a%i==0)and(b%i==0)):
    s.append(i)
#print(s)
s.sort(reverse=True)
print(s[0])

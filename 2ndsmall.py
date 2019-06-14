#
s=[]
b=int(input())
a=input().split()
h=0
for i in a:
  if(h<b):
    s.append(int(i))
    h=h+1
#print(s)
s.sort()
print(s[1])

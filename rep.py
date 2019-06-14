#
s=[]
v=[]
a=int(input())
b=input().split()
for i in b:
  s.append(int(i))
#print(s)
for i in s:
  if(i<a):
    v.append(i)
#print(v)
for i in v:
  print(i,end=" ")

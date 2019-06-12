#
o=[]
b=int(input())
a=input().split()
h=0
for i in a:
  if(h<b):
    o.append(i)
    h=h+1
#o.sort()
for i in range(b):
  print(o[i],i)

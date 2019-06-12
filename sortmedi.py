o=[]
b=int(input())
a=input().split()
h=0
for i in a:
  if(h<b):
    o.append(i)
    h=h+1
o.sort()
for i in o:
  #print(i,end="")
  if(b%2!=0):
    c=b//2
print(o[c])

#
o=[]
a=input().split()
for i in a:
  o.append(i)
o.sort(reverse=True)
print(o[0])

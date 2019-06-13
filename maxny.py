#
s=[]
a=input().split()
for i in a:
  s.append(i)
s.sort(reverse=True)
print(s[0])

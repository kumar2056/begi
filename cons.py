b1=input()
if(((b1>='a')and(b1<='z'))or((b1>='A')and(b1<='Z'))):
  if(((b1=='a')or(b1=='e')or(b1=='i')or(b1=='o')or(b1=='u'))or((b1=='A')or(b1=='E')or(b1=='I')or(b1=='O')or(b1=='U'))):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")

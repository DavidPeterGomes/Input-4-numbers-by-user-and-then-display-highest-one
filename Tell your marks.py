A=int(input("enter your percentage of first subject"))
B=int(input("enter your percentage of second subject"))
C=int(input("enter your percentage of third subject"))

if(A>33):# to input marks of 3 subjects and then see weather pass hai ki else fail
  print("Pass in A")
else:
  print("fail in A")
if(B>33):
  print("Pass in B")
else:
  print("fail in B")
if(C>33):
  print("Pass in C")
else:
  print("fail in C")

Total_Percentage=(100*(A+B+C))/300 # this check percentage :)

if (Total_Percentage<=40 and A>=33 and B>=33 and C>=33):
  print("W dawg u passed")
else:
  print("failed in class sorry")

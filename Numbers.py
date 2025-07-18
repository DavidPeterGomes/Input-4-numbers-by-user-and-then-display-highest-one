A=int(input("Enter your first number"))
B=int(input("Enter your second number"))
C=int(input("Enter your third number"))
D=int(input("Enter your fourth number"))

if(A>B and A>C and A>D):
    print("A is the greatest number")
elif(B>A and B>C and B>D):
    print("B is the greatest number")
elif(C>A and C>B and C>D):
    print("C is the greatest number")
else:
    print("D is the greatest number")
print("Enter a Number (Numerator): ")
numn = int(input())
print("Enter a Number (Denominator): ")
numd = int(input())
if numn%numd==0:
    print("\n" + str(numn)+ " is divisble by " +str(numd))
else:
    print("\n" +str(numn)+ "is not divisble by " +str(numd))
    
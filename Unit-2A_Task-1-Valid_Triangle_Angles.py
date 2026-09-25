a=float(input("enter 1st angle:"))
b=float(input("enter 2nd angle:"))
c=float(input("enter 3rd angle:"))
sum=a+b+c
if a>0 and b>0 and c>0 and sum==180:
    print("it is a valid triangle")
else:
    print("it is not a valid traingle")           
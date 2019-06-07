yx=int(input())
if(yx%4==0 and yx%100!=0 or yx%400==0):
    print("yes")
else:
    print("no")

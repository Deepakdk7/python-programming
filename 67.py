ax=int(input())
a=b=ax
if ax in range(1,11):
    print('10')
elif(ax%10==0):
    print(ax)
else:
    while a%10!=0 and b%10!=0:
        a=a+1
        b=b-1
    if(ax%10<5):
        print(b)
    else:
        print(a)

ax=input()
c=d=0
for i in ax:
    if i.isalpha()==True:
        c=1
    if i.isnumeric()==True:
        d=1
if(c==1 and d==1):
    print("Yes")
else:
    print("No")

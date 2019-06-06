ak=int(input())
tk=ak
rk=0
while ak!=0:
    dk=ak%10
    rk=rk*10+dk
    ak=ak//10
if(tk==rk):
    print("yes")
else:
    print("no")
    

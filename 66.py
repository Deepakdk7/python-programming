ax=int(input())
for i in range(2,ax):
    if(ax%i==0):
        print("no")
        break
else:
    print("yes")

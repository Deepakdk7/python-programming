ax=int(input())
x=a=0
for i in range(1,ax):
    p=2**i
    if ax==p:
        x=i
        break
a=x+1
print(2**a)

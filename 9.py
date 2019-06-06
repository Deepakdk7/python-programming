ak=input()
ak=ak.split()
bk=int(ak[1])
ck=input()
ck=ck.split()
dk=0
ck=list(map(int,ck))
for i in range(0,bk):
    dk=dk+ck[i]
print(dk)

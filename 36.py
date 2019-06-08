sg = input()
l = 0
for i in range(len(sg)):
    if(sg[i].isalpha()!=True and sg[i].isdigit()!=True):
        l = l +1
print(l)

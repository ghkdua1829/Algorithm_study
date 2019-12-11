count = int(input())
base = []
minus = []
for i in range(count,0,-1):
    base.append((1,i))
print(base)
while(len(base) is not 0):
    a = base.pop()
    if(a[1]==1):
        minus.append((a[0]+1,a[1]+1))
        minus.append((a[0]+1,a[1]))
    elif(a[1]==len(base)):
        minus.append((a[0]+1,a[1]-1))
        minus.append((a[0]+1,a[1]))
    else:
        minus.append((a[0]+1,a[1]-1))
        minus.append((a[0]+1,a[1]))
        minus.append((a[0]+1,a[1]+1))
    
print(minus)
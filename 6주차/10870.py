def pibo(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    return pibo(n-1)+pibo(n-2)
print(pibo(int(input())))
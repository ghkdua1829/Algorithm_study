import sys
count = int(sys.stdin.readline())
lines = [] 
for _ in range(count):
    lines.append(input())
for i in range(len(lines)):
    stack_main = []
    stack_sub = []
    for j in lines[i]:
        if(j=='<'):
            if(len(stack_main)==0):
                pass
            else:
                stack_sub.append(stack_main.pop())
        elif(j=='>'):
            if(len(stack_sub)==0):
                pass
            else:
                stack_main.append(stack_sub.pop())
        elif(j=='-'):
            if(len(stack_main)==0):
                pass
            else:
                stack_main.pop()
        else:
            stack_main.append(j)
    while(len(stack_sub)!=0):
            stack_main.append(stack_sub.pop())  
        
    print("".join(stack_main))
    
        
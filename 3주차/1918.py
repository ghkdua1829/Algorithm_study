input_lines = input()
stack_main = []
stack_sub = []
for line in input_lines:
    if(line=='+' or line=='-' or line=='(' or line==')'):
        stack_sub.append(line)
        if(line==')'):
            stack_sub.pop()
            if(len(stack_sub) is not 0):
                if(stack_sub[len(stack_sub)-1]=='('):
                    stack_sub.pop()
                else:
                    stack_main.append(stack_sub.pop())
                    stack_sub.pop()
    elif(line=='*' or line=='/'):
        stack_sub.append(line)
        stack_sub.append("~")
    else:
        stack_main.append(line)
        if(len(stack_sub) is not 0):
            if(stack_sub[len(stack_sub)-1]=="~"):
                stack_sub.pop()
                stack_main.append(stack_sub.pop())
for _ in range(len(stack_sub)):
    if '~' in stack_sub:
        stack_sub.remove('~')
for _ in range(len(stack_sub)):
    stack_main.append(stack_sub.pop())
print("".join(stack_main))
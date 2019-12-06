import sys
count = int(sys.stdin.readline())
lines = [] 
result = []
for _ in range(count):
    a = sys.stdin.readline()
    lines.append(a)
for i in range(len(lines)):
    location = 0
    final_line = []
    for j in lines[i]:
        if(j=='<'):
            if(location==0):
                pass
            else:
                location = location - 1
        elif(j=='>'):
            if(location==len(final_line)):
                pass
            else:
                location = location + 1
        elif(j=="-"):
            if(location==0):
                pass
            else:
                final_line[location-1] = final_line[location-1].replace(final_line[location-1],"")
                location = location - 1
        else:
            final_line.insert(location,j)
            location = location + 1
    print("".join(final_line))
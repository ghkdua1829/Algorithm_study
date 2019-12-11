dwarf = []
height = 0
for _ in range(9):
    a = int(input())
    dwarf.append(a)
    height = height + a
correct = height - 100
for i in range(9):
    for j in range(9):
        if(i is j):
            pass
        else:
            if(correct==dwarf[i]+dwarf[j]):
                a = dwarf[i]
                b = dwarf[j]
                dwarf.remove(a)
                dwarf.remove(b)
                break
    if(len(dwarf)==7):
        break
dwarf.sort()
for i in dwarf:
    print(i)

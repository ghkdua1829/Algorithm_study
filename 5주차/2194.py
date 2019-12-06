import operator
N,M,A,B,K = input().split(" ")
N = int(N)
M = int(M)
A = int(A)
B = int(B)
K = int(K)
obstacle = []
for i in range(K):
    obstacle.append(input().split(" "))
    obstacle[i] = list(map(int,obstacle[i]))
start_unit = []
start_unit.append(input().split(" "))
start_unit[0] = list(map(int,start_unit[0]))
arrive_unit = []
arrive_unit.append(input().split(" "))
arrive_unit[0] = list(map(int,arrive_unit[0]))
for garo in range(0,A):
    for sero in range(0,B):
        start_unit.append(list(map(operator.add,start_unit[0],[garo,sero])))
        arrive_unit.append(list(map(operator.add,arrive_unit[0],[garo,sero])))
del start_unit[0]
del arrive_unit[0]
print(start_unit)
print(arrive_unit)
print(obstacle)
result = 0
while(1):
    for i in range(len(start_unit)):
        start_unit[i][0] = start_unit[i][0] + 1
    for ob in obstacle:
        if ob in start_unit:
            for i in range(len(start_unit)):
                start_unit[i][0] = start_unit[i][0] - 1
        else:
            result = result + 1    
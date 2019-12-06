def solution(priorities, location):
    answer = 1
    final = priorities[location]
    final_index = location
    i=0
    while(1):
        if(max(priorities)==priorities[i]):
            if(final==priorities[i] and final_index==i):
                return answer
            else:
                answer = answer + 1
                del priorities[i]
                final_index = final_index -1
        else:
            priorities.append(priorities[i])
            del priorities[i]
            if(final_index==i):
                final_index = len(priorities) - 1
            else:
                final_index = final_index -1

    return answer

num = int(input())
for _ in range(num):
    A = input().split(" ")
    long = A[0]
    target = A[1]
    P = input().split(" ")
    P = list(map(int, P))
    print(solution(P,int(target)))
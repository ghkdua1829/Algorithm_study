def solution(heights):
    answer = [0] * len(heights)
    while heights:
        right = heights.pop()
        for i in range(len(heights)-1,-1,-1):  #range 마지막 숫자는 포함하지 않는다.
            if(heights[i]>right):
                answer[len(heights)] = (i+1)
                break
    return answer

num = int(input())
array = input().split(" ")
for _ in range(num):
    array = list(map(int,array))
print(solution(array))
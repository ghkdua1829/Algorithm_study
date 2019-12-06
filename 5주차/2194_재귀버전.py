import sys
import math

#함수를 된다고 하고 풀어보아라
#재귀로 풀어봐라 재귀의 개념을 이해해라.

n, m, a, b, k = (map(int, sys.stdin.readline().split()))
d = [(-1,0), (1,0), (0,-1), (0,1)]
break_points = set()
visited = []
cached = {}

def in_board(p):
    x, y = p
    return 1 <= x and x <= n - a + 1 and 1 <= y and y <= m - b + 1

# s, e is a tuple
def find_min_route(s, e, history = [], depth = 0):
    if s in cached:
        # print(f'hit cache {cached[s]}')
        return cached[s]

    if s in visited or not in_board(s) or s in break_points:
        return math.inf

    history.append(s)
    depth += 1
    if s == e:
        print(f'history = {history}')
        print(f'depth = {depth}')
        return 0
    else:
        visited.append(s)
        cached[s] = min([find_min_route((s[0] +dx, s[1] + dy), e, [], depth) for dx, dy in d]) + 1
        return cached[s]


for _ in range(k):
    bx, by = map(int, sys.stdin.readline().split())
    break_points.update([(bx-dx, by-dy) for dx in range(0, a) for dy in range(0, b)])

print(break_points)

fs = tuple(map(int, sys.stdin.readline().split()))
e = tuple(map(int, sys.stdin.readline().split()))

min_route = find_min_route(fs, e)
if min_route == math.inf:
    print("-1")
else:
    print(str(min_route))
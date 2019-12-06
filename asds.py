N = int(input())
if N == 1:
    print(1)
else:
    a, b = 1, 2
    for _ in range(N-2):
        a, b = (b%157476), ((a + b)%157476)
    print(b)
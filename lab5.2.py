n = 7

a = [[(n-i+j)*(i >= j) for i in range(n)] for j in range(n)]

for r in a:
        print(*r)
        
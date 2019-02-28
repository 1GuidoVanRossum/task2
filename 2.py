n = int(input())
l = []
while n != -1:
    i = 1
    n1 = [1]
    n2 = -1
    while n2 < n:
        n2 = n1[i-1] + 6*i
        n1.append(n2)
        i += 1
    if n == 1:
        l.append('Y')
    elif n1[-1] == n:
        l.append('Y')
    else:
        l.append('N')
    n = int(input())
for i in range(len(l)):
    print(l[i])

        

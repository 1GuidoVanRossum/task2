n = int(input())
k=0
k1=0
k2=0
k3=0
k4=0
k5=0
k6=0
k7=0
k8=0
l = []
for i in range(n):
    n1 = int(input())
    s = input()
    for j in range(len(s)-2):
        s1 = s[j] + s[j+1] + s[j+2]
        if s1 == 'TTT':
            k = k + 1
        elif s1 == 'TTH':
            k1 = k1 + 1
        elif s1 == 'THT':
            k2 = k2 + 1
        elif s1 == 'THH':
            k3 = k3 + 1
        elif s1 == 'HTT':
            k4 = k4 + 1
        elif s1 == 'HTH':
            k5 = k5 + 1
        elif s1 == 'HHT':
            k6 = k6 + 1
        elif s1 == 'HHH':
            k7 = k7 + 1
    l = [n1 , k , k1, k2, k3 , k4 , k5 , k6 , k7]
    k = 0
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    k7 = 0
    print(*l , sep = ' ')
   

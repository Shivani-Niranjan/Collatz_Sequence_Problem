n = int(input())
while n!=1:
    if n%2 == 0:
        print(int(n),end = " ")
        n/=2
    else:
        print(int(n),end = " ")
        n = 3*n + 1
print(1,end=" ")
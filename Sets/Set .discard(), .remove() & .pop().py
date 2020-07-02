n = int(input())
s = set(map(int, input().split()))
nc=int(input())
for i in range(nc):
    si=input().strip().split()
    if(si[0]=='pop'):
        try:
            s.pop()
        except:
            continue
    elif(si[0]=='remove'):
        try:
            s.remove(int(si[1]))
        except:
            continue
    elif(si[0]=='discard'):
        s.discard(int(si[1]))
print(sum(s))


arr=[set(map(int,input().split())) for i in range(n)]
A=[set(map(int,input().split())) for j in range(m)]
B=[set(map(int,input().split())) for k in range(m)]
print('done')
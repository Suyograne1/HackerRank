# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = list(map(int, input().split()))
n=int(input())
c=0
d=1
for i in range(n):
    a=list(map(int,input().split()))
    if(set(a).issubset(set(arr))==True):
        c=1
    else:
        d=0
if((c*d)==0):
    print("False")
else:
    print("True")
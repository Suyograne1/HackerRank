from itertools import combinations
str1=input().strip().split()
x=1
for i in range(1,int(str1[1])+1):
    a=str(list(combinations(sorted(str1[0]),x)))[1:-1]
    a=a.replace("'","")
    a=a.replace(",","")
    a=a.replace("(","")
    a=a.replace(")","\n")
    print(a.replace(" ",""),end="")
    x=x+1
from itertools import combinations_with_replacement
str1=input().strip().split()
a=str(list(combinations_with_replacement(sorted(str1[0]),int(str1[1]))))[1:-1]
b=a.replace(","," ")
c=b.replace("'","")
d=c.replace(" ","")
e=d.replace(")","\n")
print(e.replace("(",""))
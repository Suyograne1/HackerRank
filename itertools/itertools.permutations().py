from itertools import permutations
str1=input().strip().split()
a=str(list(permutations(sorted(str1[0]),int(str1[1]))))[1:-1]
b=a.replace(","," ")
c=b.replace("'","")
d=c.replace(" ","")
e=d.replace(")","\n")
print(e.replace("(",""))
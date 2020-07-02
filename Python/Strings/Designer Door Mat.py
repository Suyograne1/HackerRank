# Enter your code here. Read input from STDIN. Print output to STDOUT
str='-'
ctr='.|.'
jtr='WELCOME'
a, b = map(int,input().split())
top=int((a-1)/2)
d=(b-3)/2
e=0
m=1

#upper part
for i in range(top):
    print(str.ljust(int(d-e),'-')+(ctr*m)+str.rjust(int(d-e),'-'))
    e=e+3
    m=m+2

#middle WELCOME part
    if(a==m):
        new=(b-7)/2
        print(str.ljust(int(new), '-') + 'WELCOME' + str.rjust(int(new), '-'))
        break

#lower part
m=m-2
ld=3
for i in range(top):

    print(str.ljust(int(ld), '-') +(ctr*m) + str.rjust(int(ld), '-'))
    ld=ld+3
    m=m-2


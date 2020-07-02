# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
X=(str(list(product(A,B)))).replace("'","")[1:-1].replace("),",")")
print(X)
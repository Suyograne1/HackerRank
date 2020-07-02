if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a=max(arr)
    arr.remove(a)
    while(max(arr)==a):
        arr.remove(max(arr))
    print(max(arr))
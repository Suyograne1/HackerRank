def average(array):
    # your code goes here
    a = set(arr)
    return (sum(a) / len(a))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
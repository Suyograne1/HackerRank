if __name__ == '__main__':
    N = int(input())
    lst = list()
    for i in range(N):
        w = input().strip().split()
        if (w[0] == 'insert'):
            lst.insert(int(w[1]), int(w[2]))
        elif (w[0] == 'print'):
            print(lst)
        elif (w[0] == 'remove'):
            lst.remove(int(w[1]))
        elif (w[0] == 'append'):
            lst.append(int(w[1]))
        elif (w[0] == 'sort'):
            lst.sort()
        elif (w[0] == 'pop'):
            lst.pop()
        elif (w[0] == 'reverse'):
            lst.reverse()





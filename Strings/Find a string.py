def count_substring(string, sub_string):
    a = 0
    count = 0
    b = len(sub_string)
    for i in range(len(string)):
        i = string[a:b]
        j = sub_string[0:]
        if (i == j):
            count = count + 1
        a = a + 1
        b = b + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
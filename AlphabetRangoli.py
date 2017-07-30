import string
def print_rangoli(size):
    for j in range(size - 1, -1, -1):
        arr = []
        mid = size - 1 - j
        for i in range(2 * (size - j) - 1):
            if i <= mid:
                arr.append(string.ascii_lowercase[j + mid - i])
            else:
                arr.append(string.ascii_lowercase[j + i - mid])
        print '-'.join(arr).center(4*size - 3, '-')
    for j in range(1, size):
        arr = []
        mid = size - 1 - j
        for i in range(2 * (size - j) - 1):
            if i <= mid:
                arr.append(string.ascii_lowercase[j + mid - i])
            else:
                arr.append(string.ascii_lowercase[j + i - mid])
        print '-'.join(arr).center(4*size - 3, '-')

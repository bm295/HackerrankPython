if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    aList = list(arr)
    maxA = max(aList)
    newList = list()
    for i in range (len(aList)):
        if aList[i] != maxA:
            newList.append(aList[i])
    secondMax = max(newList)
    print secondMax

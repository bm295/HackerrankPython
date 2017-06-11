if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(0,N):
        text = raw_input()
        text = text.split()
        if (text[0] == 'insert'):
            list.insert(int(text[1]), int(text[2]))
        elif (text[0] == 'print'):
            print list
        elif (text[0] == 'remove'):
            list.remove(int(text[1]))
        elif (text[0] == 'append'):
            list.append(int(text[1]))
        elif (text[0] == 'sort'):
            list.sort()
        elif (text[0] == 'pop'):
            list.pop()
        elif (text[0] == 'reverse'):
            list.reverse()

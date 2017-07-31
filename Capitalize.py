def capitalize(string):
    input = string.split(' ')
    output = []
    for word in input:
        if word:
            output.append(word[0].upper() + word[1:])
        else:
            output.append('')
    return ' '.join(output)

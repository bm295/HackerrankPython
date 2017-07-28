def swap(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

def swap_case(s):
    return ''.join([swap(c) for c in s])

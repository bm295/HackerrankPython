from itertools import product

arrA = map(int, input().split())
arrB = map(int, input().split())
print(*product(arrA,arrB))    

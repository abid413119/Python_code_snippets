numbers = [1, 2, 3, 4, 5, 6]

*a, = numbers
print(a)

*a, b = numbers
print(a)
print(b)

a, *b, = numbers
print(a)
print(b)

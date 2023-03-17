n, m, a = map(int, input().split())

row = n // a
col = m // a

if n % a != 0:
    row += 1

if m % a != 0:
    col += 1

print(row * col)




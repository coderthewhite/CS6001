#Sentinel Value
num = int(input())
arrs = list(map(int, input().split()))

value = arrs[0]
for index in range(1, len(arrs)):
  if value < arrs[index]:
    value = arrs[index]

print(value)
#sentinel value
def is_prime(number):
  for factor in range(2, number):
    if number % factor == 0:
      return False
  return True

def find_biggest_prime(arrs):
  pos = -1
  for index in range(len(arrs)):
    if is_prime(arrs[index]):
      pos = index
      break
  sentinel = arrs[pos]
  for index in range(pos + 1, len(arrs)):
    if is_prime(arrs[index]) and arrs[index] > sentinel:
      sentinel = arrs[index]

  return sentinel

if __name__ == '__main__':
  num = int(input())
  arrs = list(map(int, input().split()))
  result = find_biggest_prime(arrs)
  print(result)
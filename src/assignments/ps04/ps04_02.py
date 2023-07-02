#sentinel value

def find_first(arrs, candidate):
  pos = -1
  for index in range(len(arrs)):
    if arrs[index] == candidate:
      pos = index
      break
  return pos
  
def find_last(arrs, candidate):
  pos = -1
  for index in range(len(arrs)):
    if arrs[index] == candidate:
      pos = index
  return pos

def find_first_last(arrs, candidate):
  first = -1
  last = -1
  for index in range(len(arrs)):
    if arrs[index] == candidate:
      if first == -1:
        first = index
      last = index        
  return first, last
  
if __name__ == '__main__':
  num = int(input())
  candidate = int(input())
  arrs = list(map(int, input().split()))
  first = find_first(arrs, candidate)
  last = find_last(arrs, candidate)
  print(first, last)
  first, last = find_first_last(arrs, candidate)
  print(first, last)
  
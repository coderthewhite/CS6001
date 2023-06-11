embossor = "abcdefghijklmnopqrstuvwxyz"
letters = input()
 
pointer = 0
 
total = 0
for letter in letters:
    pos = embossor.index(letter)
    diff = abs(pos - pointer)
    if diff > 13:
        steps = 26 - diff
    else:
        steps = diff
    total += steps
    pointer = pos
 
print(total)

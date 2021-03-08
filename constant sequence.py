import random

counter = 0

for _ in range(5):
    prev = random.randint(0, 10)
    curr = random.randint(0, 10)
    if prev == curr:
        counter = counter + 1

print(counter)    

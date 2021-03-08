import random

for _ in range(100):
    prev = random.randint(0, 1000)
    mn = prev
    curr = random.randint(0, 1000)
    if curr < mn:
        mx = mn
        mn = curr
    else:
        mx = curr

print('Минимальное:', mn, 'Максимальное:', mx)

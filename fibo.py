n = int(input("n: "))
F1 = 1
F2 = 1
if n < 1:
    print("n больше 0")
elif n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    print(1, 1, end=" ")
    for _ in range(n):
        Fn = F1 + F2
        print(Fn, end=" ")
        F1 = F2
        F2 = Fn

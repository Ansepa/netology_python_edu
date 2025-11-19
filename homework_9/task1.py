import random

def payout(n: int) -> int:
    s = f"{n:03d}"
    if s == "777":
        return 200
    if s == "999":
        return 100
    if s == "555":
        return 50
    if s == "333":
        return 15
    if s == "111":
        return 10
    if s[1:] == "77":      # *77
        return 5
    if s[2] == "7":        # **7
        return 3
    if s[1:] == "00":      # *00
        return 2
    if s[2] == "0":        # **0
        return 1
    return 0

N = 2_000_000
total = 0

for _ in range(N):
    x = random.randint(0, 999)   
    total += payout(x) - 1       

avg = total / N
print("Средний результат:", avg)


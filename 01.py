ans = 0
cur = 50

for line in open("01.txt"):
    directions, steps = line[0], int(line[1:])
    for _ in range(steps):
        if directions == "L":
            cur = (cur - 1) % 100
        elif directions == "R":
            cur = (cur + 1) % 100
        if cur == 0:
            ans += 1

print(ans)

        
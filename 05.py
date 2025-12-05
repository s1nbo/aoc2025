def one():
    temp = False
    ans = 0
    range_ids = []
    with open("05.txt") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line is None or line == "":
            temp = True
            continue
        elif temp == False:
            parts = line.split("-")
            range_ids.append((int(parts[0]), int(parts[1])))
        elif temp == True:
            num = int(line)
            for r in range_ids:
                if num <= r[1] and num >= r[0]:
                    ans += 1
                    break
    print(ans)


def two():
    interval = []
    with open("05.txt") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line is None or line == "":
            break
        else:
            parts = line.split("-")
            interval.append((int(parts[0]), int(parts[1])))
    
    interval.sort()

    merged = []
    cur_start, cur_end = interval[0]
    for inter in interval:
        
        if inter[0] <= cur_end:
            cur_end = max(cur_end, inter[1])
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = inter
    
    
    merged.append((cur_start, cur_end))
    ans = 0
    
    for m in merged:
        ans += (m[1] - m[0] + 1)
    print(ans)

two()
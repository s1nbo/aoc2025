from collections import defaultdict

def one():
    with open("07.txt") as f:
        lines = f.readlines()
        pos = []
        count = 0
        ans = 0
        for line in lines:
            for idx, char in enumerate(line.strip()):
                if char == 'S':
                    start = [idx, count]
                elif char == '^':
                    pos.append([idx, count])
            count += 1
        
        beam_pos = set([start[0]])

        for i in range(count):
            for p in pos:
                if p[1] == i:
                    if p[0] in beam_pos:
                        beam_pos.add(p[0] - 1)
                        beam_pos.add(p[0] + 1)
                        ans += 1
                        beam_pos.remove(p[0])
    
        print(ans)


def two():
    with open("07.txt") as f:
        lines = f.readlines()
        pos = []
        count = 0
        ans = 1
        for line in lines:
            for idx, char in enumerate(line.strip()):
                if char == 'S':
                    start = [idx, count]
                elif char == '^':
                    pos.append([idx, count])  # last element is used to track how often it has been hit
            count += 1
        
        beam_pos = defaultdict(int)
        beam_pos[start[0]] = 1
        for i in range(count):
            for p in pos:
                if p[1] == i:
                    if p[0] in beam_pos:
                        beam_pos[p[0] - 1] += beam_pos[p[0]]
                        beam_pos[p[0] + 1] += beam_pos[p[0]]
                        ans += beam_pos[p[0]]
                        del beam_pos[p[0]]


    print(ans)


two()

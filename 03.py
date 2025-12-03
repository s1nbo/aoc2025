def one():
    ans = 0

    with open("03.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = [0, 0]
            line = line.strip()
            for idx, num in enumerate(line):
                num = int(num)
                if num > temp[0] and idx < len(line) - 1:
                    temp[0] = num
                    temp[1] = 0
                elif num > temp[1]:
                    temp[1] = num
            
            
            ans += temp[0]*10 + temp[1]
                
    print(ans)

def two():
    ans = 0
    
    with open("03.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = [0] * 12
            line = line.strip()
            for idx, num in enumerate(line):
                num = int(num)
                for i in range(12):
                    if num > temp[i] and idx < len(line) - 11 + i:
                        temp[i] = num
                        for j in range(i + 1, 12):
                            temp[j] = 0
                        break
        

            multiply = 1000_0000_0000
            for i in range(12):
                ans += temp[i] * multiply
                multiply //= 10
    print(ans)
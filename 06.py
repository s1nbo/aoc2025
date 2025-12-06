def one():
    ans = 0
    sol = []
    with open("06.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(" ")
            line = [x for x in line if x]
            sol.append(line)

    for col in range(len(sol[0])):
        symbol = 1 if sol[-1][col] == '+' else 0
        temp_ans = 0 if symbol else 1

        for row in range(len(sol)-1):
            if symbol:
                temp_ans += int(sol[row][col])
            else:
                temp_ans *= int(sol[row][col])

        ans += temp_ans

    print(ans)
        
def two():
    f = open("06.txt").read().split('\n')
    # find the position in the first 4 strings where there is a space at the same index
    positions = [i for i in range(len(f[0])) if all(f[j][i] == ' ' for j in range(len(f)-1))]
    ans = 0
    # add commas at those positions in all strings
    for i in range(len(f)):
        for pos in reversed(positions):
            f[i] = f[i][:pos] + ',' + f[i][pos+1:]

    # add 0 leading and trailing
    for i in range(len(f)-1):
        f[i] = f[i].replace(' ', '0')
    f[-1] = f[-1].replace(' ', '')
    
    # Matrix of correct values
    matrix = [list(row.split(',')) for row in f[:]]
    
    for col in range(len(matrix[0])):
        symbol = 1 if matrix[-1][col] == '+' else 0
        temp_ans = 0 if symbol else 1

        for i in range(len(matrix[0][col])):
            temp_num = []
            for row in range(len(matrix)-1):
                temp_num.append(matrix[row][col][i])

            combined_num = int(''.join(temp_num).replace('0', ''))
            
            if symbol:
                temp_ans += combined_num
            else:
                temp_ans *= combined_num
        
        ans += temp_ans

    print(ans)
two()
def one():
    ans = 0
    with open("04.txt", "r") as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            line.strip()
            temp = []
            for char in line:
                if char == "@":
                    temp.append(1)
                else:
                    temp.append(0)
            matrix.append(temp)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    total = 0
                
                    if i > 0:
                        total += matrix[i-1][j]
                        if j > 0:
                            total += matrix[i-1][j-1]
                        
                        if j < len(matrix[0])-1:
                            total += matrix[i-1][j+1]
                    
                    if i < len(matrix) - 1:
                        total += matrix[i+1][j]
                        if j > 0:
                            total += matrix[i+1][j-1]
                        if j < len(matrix[0])-1:
                            total += matrix[i+1][j+1]
                    
                    if j > 0:
                        total += matrix[i][j-1]
                    if j < len(matrix[0]) - 1:
                        total += matrix[i][j+1]
                    
                    if total < 4:
                        ans += 1
    
    print(ans)

one()

def two():
    ans = 0
    with open("04.txt", "r") as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            line.strip()
            temp = []
            for char in line:
                if char == "@":
                    temp.append(1)
                else:
                    temp.append(0)
            matrix.append(temp)


        flag = True
        while flag:
            flag = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        total = 0
                    
                        if i > 0:
                            total += matrix[i-1][j]
                            if j > 0:
                                total += matrix[i-1][j-1]
                            
                            if j < len(matrix[0])-1:
                                total += matrix[i-1][j+1]
                        
                        if i < len(matrix) - 1:
                            total += matrix[i+1][j]
                            if j > 0:
                                total += matrix[i+1][j-1]
                            if j < len(matrix[0])-1:
                                total += matrix[i+1][j+1]
                        
                        if j > 0:
                            total += matrix[i][j-1]
                        if j < len(matrix[0]) - 1:
                            total += matrix[i][j+1]
                        
                        if total < 4:
                            ans += 1
                            matrix[i][j] = 0
                            flag = True
    
    print(ans)

two()

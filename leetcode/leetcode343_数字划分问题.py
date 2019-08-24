a = 38
solution = [0]*(a+1)
solution[0] = 0
solution[1] = 1
solution[2] = 2
solution[3] = 3
for i in range(4,a+1):
    max_ = 0
    for j in range(1,i):
        if solution[j]*solution[i-j] > max_:
            max_ = solution[j]*solution[i-j]
    solution[i] = max_

print(solution)
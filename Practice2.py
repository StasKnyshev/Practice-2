print('Введите количество строк матрицы')
irazmer=int(input())
print('Введите количество столбцов матрицы')
jrazmer=int(input())
matrix=[]
answer=[]
for i in range(irazmer):
    matrix.append([]) # 2*irazmer
    for j in range (jrazmer):
        matrix[i].append(int(input())) #2*jrazmer*irazmer
for j in range(jrazmer):
    answer.append([]) #jrazmer*2
    for i in range (irazmer):
        answer[j].append(matrix[i][j]) #2*irazmer*jrazmer
print(matrix)
print(answer)
print(4+2*irazmer*jrazmer+2*irazmer+jrazmer)
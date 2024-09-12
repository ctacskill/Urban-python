# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу
# (вложенный список) размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.

def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
         matrix.append([])
         for k in range(m):
             matrix[i].append(value)
    print(matrix)

get_matrix(1, 0, 42)
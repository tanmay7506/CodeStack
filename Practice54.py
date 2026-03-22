m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

column_sums = [0] * n

for i in range(m):
    for j in range(n):
        column_sums[j] += matrix[i][j]

max_column_sum = max(column_sums)
max_sum_column_index = column_sums.index(max_column_sum)

print(max_sum_column_index)
print(max_column_sum)

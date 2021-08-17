triangle = int(input())
triangle_matrix = []
max_matrix = [[] for _ in range(triangle)]

for _ in range(triangle):
    triangle_matrix.append(list(map(int, input().split())))

   
for i in range(triangle - 1, -1, -1): #거꾸로 올라가면서 합이 최대인것만 더해주기
    for j in range(len(triangle_matrix[i])):
        if i == triangle - 1:
            max_matrix[i].append(triangle_matrix[i][j])
        else:
            max_matrix[i].append(triangle_matrix[i][j] + max(max_matrix[i+1][j], max_matrix[i+1][j+1]))

print(max_matrix[0][0])

#삼각형의 제일 밑에서부터 최댓값을 저장해가면서 올라가는데 대각선 왼쪽 아래와 대각선 오른쪽 아래 중 큰 수와 
#자기자신을 더한 값이 그 아래 경로의 최댓값임

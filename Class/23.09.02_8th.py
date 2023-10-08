# 가변 배열일 때 주의점이
# 계속 변한다 => len

matrix = [[1,2,3], [4], [5,6,7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

print()

# 좀 더 쉽게 변수로 지정하기
iLen = len(matrix)  # 행 길이
for i in range(iLen):   # 하나씩 끄내서 본다
    jLen = len(matrix[i])   # 2차원 리스트에 들어있는 리스트의 길이
    for j in range(jLen):   # 길이만큼 반복
        print(matrix[i][j], end=' ')
    print()
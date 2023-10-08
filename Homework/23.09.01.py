matrixs = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 1. 위와 같은 2차원 리스트를 생성하고 출력하세요.
# 2차원 리스트 생성하는 법 검색

print("Q1")
matrix = []
index = 1

for i in range(3):
    a = []
    for j in range(3):
        a.append(index)
        index += 1
    matrix.append(a)
print(matrix, end= '')


# 2. 위와 같은 2차원 리스트의 모든 원소의 합을 계산하여 출력하세요.
print()
# 리스트에서 원소 추출하는 법 검색 <- for i in matrix
# sum 함수 사용하는 법 검색

sum = 0        # <- 이 아이디어에서 착안

for i in matrixs:
    for j in i:
        sum += j
print(sum)

# 3. 위와 같은 2차원 리스트에서 짝수만 출력하세요.

for i in matrixs:
    for j in i:
        if j % 2 == 0:
            print(j, end= ' ')

# 4. 위와 같은 2차원 리스트에서 각 행의 합을 구하여 리스트로 출력하세요.

result_array = []

for matrix in matrixs:
   temp_sum = 0
   for elem in matrix:
       temp_sum += elem
   result_array.append(temp_sum)
print(sum, end= ' ')
print()

# 5. 아래와 같은 2차원 리스트에서 각 행의 평균을 계산하여 리스트로 출력하세요.

means = []

for elems in matrixs:
    temp_sum = 0
    for elem in elems:
        temp_sum += elem
        # temp_sum /= len(elems)                 나누기 변환을 할 시에 정수형이라도 실수형으로 변환된다. + 나누고 변수에 넣어주려면 /= 사용
    means.append(temp_sum / len(elems))         #가변 길이를 생각해서 숫자가 아닌 변수로 쓰자!
    # print(type(mean))
print(means)

# 문제를 해결하는 데에 있어서 주석을 열심히 달자!
# 디버그나

print()
# * 1
# ** 2
# *** 3
# **** 4
# ***** 5

# 이중 for문 - for, print만 사용해서 출력하기
for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()

# i = 1 일 때, range(0, 1) => 0 이상 1 미만, j 를 한번 출력
# i = 2 일 때, range(0, 2) => 0 이상 2 미만, j 를 두번 출력

# for [변수] in [range, 순회가 가능한 것들 (ex, list, tuple, str)]:
# [변수] => 보통은 for문 안에서만 사용한다 -> 외우자 (이 방식대로 하지 않으면 헷갈리게 됨)
# for문은 아래에 있는 코드를 n번 수행한다 => 이것이 이해가 필요함 *에 집중할게 아니라 그만큼 for문이 n번 돌아가는 것에 집중!

# end='' => 파이썬에서 print() 함수는 기본적으로 줄 바꿈이 된다. 근데, end=''를 사용하게 되면 줄바꿈이 삭제
# print() => end='\n'가 default이다.
# 임의로 지정하게 되면 바뀌게 된다.

# Homework
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# if ~ elif ~ else 구문임. -> 무조건 맨 앞에서는 if로 시작해야함

# 주제 : 학생들의 점수에 따라 학생들의 학점을 계산하시오
# 1번 학생 ~ N번 학생의 점수를 리스트로 표현
score = [90, 70, 60, 50, 100, 92, 84, 45, 2]

# 조건
# 90점 이상은 A 학점
# 80점 이상은 B+ 학점
# 70점 이상은 B 학점
# 60점 이상은 C+ 학점
# 50점 이상은 C 학점
# 그 아래는 F

# for value in score:
#     if value >= 90:
#         print("A", end=' ')
#     elif value >= 80:
#         print("B+", end=' ')
#     elif value >= 70:
#         print("B")
#     elif value >= 60:
#         print("C+")
#     elif value >= 50:
#         print("C")
#     else:
#         print("F")

# 함수 => 공통적인거 묶어서 사용한다
def func1(value):
    print(value, end=', ')


for value in score:
    if value >= 90:
        func1("A")
    elif value >= 80:
        func1("B+")
    elif value >= 70:
        func1("B")
    elif value >= 60:
        func1("C+")
    elif value >= 50:
        func1("C")
    else:
        func1("F")

# if ~ else if ~ else
# 파이썬에서는 함축해서 elif
# if ~ elif ~ else 구문

# 12345
# 1, 2, 3, 4, 5

# 줄 바 꿈
print()
numberList = [1, 2, 3, 4, 5]

# 인덱스
index = 0

# 리스트의 길이
length = len(numberList)

for num in numberList:
    if index != len(numberList) - 1:
        print(num, end=', ')
    else:
        print(num, end='')
    index += 1

# index : 0, 1, 2, 3, 4
# len(numberList) = 5, 배열에서는 0부터 시작하기 때문에

# PPH [숫자 6자리] -200
# 반복적인 작업에서 규칙을 찾아서 단순화 시켜라

# 몇개 지정하면 좋겠지만? 몇 개를 모를 때

print()
print()

print("작업 시작!")
cat_list = []

while True:
    # 숫자 6자리를 입력을 받습니다.
    # 만약 z를 입력을 받았을 때 종료시킵니다.
    value = input('숫자 6자리를 입력하세요 (종료 조건은 z입력) >> ')
    if value == 'z':
        break

    # 6자리가 아니야
    if len(value) != 6:
        print("6자리 입력해 이자식아")
        continue

    temp = "PPH " + value + "-200"

    cat_list.append(temp)

print(cat_list)

# 중복제거 해줘
# 그룹화해서 갯수세기
#

# 문제 도출
# 나 600개 QR 만들어야해 => for(1~600)
# 근데 이거 프린트할거라 이미지로 만들어줘야해 => 검색 => img 저장하는 방법
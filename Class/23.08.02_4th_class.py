# 조건문과 반복문
# if (true or false) -> 항상 True 일때만 실행 됨.
# =는 대입연산자 / ==은 비교 연산자

value = 10
if value == 10:
    print(True)

# 비교 연산자 ==, not은 ! (!=)
if value != 10:
    print("aa")

# a라는 변수에 1부터 10까지 포함하고 있는 List를 만들고 싶습니다.
a = list(range(1, 11))

# a라는 list 안에 n이라는 숫자가 있으면 n을 출력하라.
# a라는 list 안에 8이라는 숫자가 있으면 8을 출력하라.
# in 연산자 (이거 안에 포함되어 있는지를 확인하거나 for문에서 list에서 꺼내오는 용도로 사용하기도 함)
if 8 in a:
    print(8)

# for문을 이용하여 반복문을 만든다. 어떤 구간을 선정해서 돌리는 것
# while문도 사용함 (minor)   --> True/False와 연관이 있다. 결국 조건이 참인지 거짓인지에 따라 문법 실행
# while default is 무한 반복
# break - 반복을 탈출할 때 사용

# [1부터 10까지 탐색하면서] [5가 나오면 출력하고 종료해라] -> 문제를 뜯어보면 들여쓰기가 보이겠구만.
for value in range(1, 10):
    if value == 5:
        print(5)
        break

index = 0

while index != 10:
    index += 1
    print(index)


# range (start, end, ..)
# start -> end 미만이다.

# if for in range 를 숙지하자.

a = list(range(1, 5))
print(a)

for value in a:
    print("*")
    if value == 4:
        break

# 삼각형 별찍기 (기본형)
# for문과 print만을 이용하여 출력하시오
# hint : 이중 for 문

a = ""
for i in range(1,6):
   for j in range(0, i):
       a += "*"
   a += "\n"
   print(a)

for i in range(1,6):
    for j in range(0,i):
        print('*', end = '')
    print()

for i in range(-4,0):
    for j in range(i,0):
        print('*', end = '')
    print()

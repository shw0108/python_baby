a = 10
b = 20
c = 30
d = 40

print(a, b, c, d)

# list = 배열 (행렬)

# 배열 선언
a = []

# 배열에 추가하는 것
a.append(1)
a.append(2)
a.append(3)

# 배열에서 빼는 것 (뒤에서 부터)
a.pop()

# 변수 초기화 = 초기에 값을 넣어둔다.
a = [1, 2, 3, 4, 5]

# 자료형에 의존적이지 않다. int, str 다 들어갈 수 있다.
a = [1, 'str', 3, 3.9]

# 새로운 배열,리스트 => 자료 구조
# []

# 새로운 리스트 선언
a = []

# 1-100까지 중에 짝수 인 것만 출력하시오 => 배열에 저장하여 출력하라!
for i in range(1, 10):
    if i % 2 == 0:
        a.append(i)

print(a)

# 배열, index 인덱스 ==> 위치

# 위에서 구한 것 중에 작은 것부터 10번째 있는 값을 출력하시오
print(a[10])

#  리스트에 i (index) 번째 값을 출력
# a[index] ==> a 라는 리스트의 10번째에 있는 값을 출력하시오

# 키 리스트 선언
height = [190, 180, 210, 160]

# 키 순서대로 해서 앞에서 2번 사람을 구하라
# 정렬 - default 오름차순
height.sort()

# 코딩은 index 무조건 0부터 시작
print("len : ", len(height))
print(height[0])
print(height[1])

# range를 사용해서 리스트 만들기? => 잘 안씀 => for 문 돌림
a = list(range(10))

# range(start, end, 증감폭) -> start 부터 end-1까지 증감폭에 따라.
a = list(range(5, 12, 2))

# 튜플 => 리스트에서 변경, 추가 삭제 불가 => 한번 선언되면 그걸로 끝
# 튜플 선언 ==> (), 절대 참조
a = (1, 2, 3, 4)

# 논리 연산자
# True False
# 1     0


# 많이 해봐야 는다.
a = list(range(0, 100, 10))
a = []

for i in range(0, 100):
    if i % 10 == 0:
        a.append(i)
print(a)

print(30 in a)

if a.__contains__(30):
    print(True)

print(100 not in a)

# 조건문 -> True, False 가 매우 중요하다.

# 시퀀스 => 리스트(행렬), 튜플, range, 문자열
a = "Hello World"
# 문자열 => 문자들의 집합이다!
print(a[1])

# 시퀀스의 특 => 순서가 중요함. index로 접근이 가능하다!
print(a[6])

# 두개를 합칠 수 있다.
a = [10, 20, 30, 40]
b = [50, 60, 70, 80]

print(a + b)

# a의 index 0, 1, 2, 3
# index -1 => 3 (음수 index는 뒤에서 부터 나오는 것)

# 슬라이스
# 반복문 조건문
a = list(range(0, 100, 10))
print(a)

b = []
i = 0
for value in a:
    b.append(value)
    i+=1
    if i == 1:
        break
print(b)

b= a[1:2]
print(b)


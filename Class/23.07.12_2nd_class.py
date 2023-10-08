a = 10
if a == 10:
    print(a)

# 함수, 반복문, 조건문에 해당하는 것들은 항상 끝에 :을 붙인다.
# 들여쓰기는 무조건 4칸 (보통 탭 한번 누르면 됨) / 들여쓰기를 없앨 때는 shift+tab

if a== 10:
  print(a)

print ('Hello world')

# Unit 5 숫자 계산하기

a = 10
b = 5

# a + b 의 값을 result라는 변수에 담고 싶다
result = a + b

print (result)

# 자료형에 상관없이 변수 자료형이 알아서 변환된다.
result = b / a

print (result)
# 스펠링만 틀려도 다 틀리니까 주의해서 해야함.

# 내장함수 : 별도의 설치가 필요없이 Python이 가지고 있는 함수
# 예를 들어 : print, type, input
# 이 변수의 자료형은 ??
print(type(a))
print(type(result))

# >>> 여기다 입력하세요 (무시하고 print 찍으면 됨)
# / 는 나누기 연산입니다

# % 는 나머지 연산입니다
print(3 % 2)

# ** 는 거듭제곱 연산입니다
print(2 ** 10)

# * 은 곱하기 연산이다
print(2 * 10)

# 타입 변환
a = 5
b = 10
result = a / b
print(result)

print(int(result))
print(type(result))

# int(), float(), str()
# 형(자료형) 변환할 때는 값에 주의
a = 10

# 정수 -> 실수
print(float(a))

# 정수 -> 문자열
print(str(a), type(str(a)))

# 문자열 -> 정수
# 문자열 '', "" 둘 중 하나 사용
# 둘 다 되는 이유는? (''나 ""를 변수에 넣고 싶어서)
a = "10"

print(a)
print(type(a))

string = "'string'"
print(string)

# 숫자 -> 문자열 다 됨.
# 문자열 -> 숫자는 안 됨.

# csv 파일 => 엑셀
# Comma separate Value

# 문자열을 자르기 하면 됨
# 문자열 자르기 할 때 구분자를 사용할 수 있음
# 구분자 : 원하는 문자 예를 들어 CSV 에서는 ,(comma)

value = "a,b,c,d,10"
print(value.split(','))

value = "BaBaBaBa"
print(value.split('a'))

value = "2002 09 01"
print(value.replace(" ", ""))

# 자기 자신과 연산, 노란 줄로 틀린거 힌트 줌.
a = 10
a = a + 10

a += 10

print(a)

a -= 10
a *= 10
a /= 10

print (a)

a %= 10

print(a)

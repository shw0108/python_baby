
# for i in range(1, 6):
#     for j in range(0, i):
#         print('*', end='')
#     print()

# i = 1일 때, range(0,1) => 0이상 1미만, j를 1 번 출력
# i = 2일 때, range(0,2) => 0이상 2미만, j를 2 번 출력
# i = 3일 때, range(0,3) => 0이상 3미만, j를 3 번 출력
# i = 4일 때, range(0,4) => 0이상 4미만, j를 4 번 출력
# i = 5일 때, range(0,5) => 0이상 5미만, j를 5 번 출력

# for i in range(1,6):
#     for j in range(0,6-i):
#         print('*', end='')
#     print()

for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()                 # i == 5 까지 위쪽 이중 for문을 돈다.
    if i == 5:              # 5까지 다 돌고 나서, k 있는 이중 for문 돈다.
        for k in range(0,i):
            for l in range(0,4-k):
                print('*', end='')
            print()
        i -= 1
    elif i == 0:
        print()

for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(4, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()

# k = 0 일 때, (0,5) -> l (0,4), l을 4번 출력 -> i == 4
# k = 1 일 때, (0,4) -> l (0,3), l을 3번 출력 -> i == 3
# k = 2 일 때, (0,3) -> l (0,2), l을 2번 출력 -> i == 2
# k = 3 일 때, (0,2) -> l (0,1), l을 1번 출력 -> i == 1
# k = 4 일 때, (0,1) -> l (0,0), l을 0번 출력 -> i == 0 -> print()

print("Homework 1")

# 1. 1부터 50까지의 숫자 중에서 3의 배수를 출력하는 프로그램을 작성하세요. ==> 이런 문제에서 마지막은 항상 제외하는데, 그럼 1 더해줘서 마지막 숫자도 포함되게 해야함?

a = list(range(1, 50))
b = []

for i in a:
    if i%3 == 0:
        b.append(i)
    elif i == 50:
        break
print(b)

# 최대한 짧게

for S in range(1, 51):
    if S % 3 == 0:
        print(S, end=' ')
print()

# for문 안쓰고? (하는 방법은 없을까?) ==============================================
# a = list(range(1, 50))
#
# if a%3 == 0:
#     print(a, end=' ')



print()
print()
print()

print("Homework 2")

# 2. 사용자로부터 숫자를 입력받아, 입력한 숫자가 짝수인지 홀수인지 출력하는 프로그램을 작성하세요. (input 사용)

# while True:
#     # 안되니까 일단 int 넣어서 숫자로 인식시키긴 함... / a에다가 대입을 해야하니 대입연산자인 '='를 사용하자
#     a = input('숫자를 입력하시오(정수만 써라 이기야, 000 쓰면 끝남) >> ')
#     a = int(a)

#     a = int(input('숫자를 입력하시오(정수만 써라 이기야, 000 쓰면 끝남) >> '))   # 문자랑 숫자 혼용해서는 못 쓰는건가?
#                                                                      # 차라리 변수 2개로 써서 문자 숫자 나눠서도 안되던데?
#     # 얘가 멈춰주는거고
#     if a == 000:
#         break
#
#     if a % 2 == 0:
#         print('짝수')
#         continue
#     elif a % 2 == 1:
#         print('홀수')
#         continue
#     else:
#         print('숫자 써라 게이야')
#         continue
#     break
# 이제 끝임

print()
print()
print()

# (str)000 => 숫자로 변환 => 0

print("Homework 3")

# 3. 1부터 10까지의 숫자의 합을 계산하여 출력하는 프로그램을 작성하세요.

DongDong = []

for i in range(1,11):
   if i != 11:
       DongDong.append(i)
       i += 1
   elif i == 11:
       break
print(sum(DongDong))

sum = 0
for i in range(1, 11):
    sum += i

print(sum)


print()
print()
print()

print("Homework 4")
# 4. 1부터 100까지의 숫자 중에서 7의 배수이면서 5의 배수는 아닌 숫자를 출력하세요.

Big_Dong = []

for sex in range(1, 101):
    if sex%7 == 0 and sex%5 != 0:
        Big_Dong.append(sex)

print(list(Big_Dong))

# 여기에서 ',' 이걸 넣어서 쓰고 싶은데? 마지막꺼는 ',' 빼려면 내가 일일히 계산해야 하는데 그거 없이 하는 방법은?
for sex in range(1, 101):
    if sex%7 == 0 and sex%5 != 0:
        print(sex, end=' ')

print()
print()
print()

print("Homework 5")
# 5. 사용자로부터 단을 입력받아 구구단을 출력하는 프로그램을 작성하세요. (힌트는 value = int(input()))

value = int(input("알고 싶은 구구단의 단을 입력하시오 (근데 암산 못함?) >>> "))

for i in range(1,10):
    print(str(value) + " * " + str(i) + " =", value*i)

    if value == 0:
        break

print()
print()
print()

print("Homework 6")
# 6. 1부터 20까지의 숫자 중에서 2의 거듭제곱인 숫자만 출력하는 프로그램을 작성하세요.

for i in range(1,21):                   # 이건 1 ~ 20까지 숫자라고 할 때,
    if pow(2, i) < 21:                  # 이건 숫자가 작으니까 대충 이렇게 쓴 건데 맞나..?
        print(pow(2,i), end= ' ')

print()
print()
print()

print("Homework 7")
# 7. 100 이하의 소수를 출력하는 프로그램을 작성하세요.

# for i in range(1, 101):


print()
print()
print()

print("Homework 8")
# 8. 사용자로부터 숫자를 계속 입력받다가 0을 입력하면 그동안 입력된 숫자들의 합을 출력하는 프로그램을 작성하세요.


bigtit = []         # 꼭 바깥쪽에 넣어야 되는 이유는? (while 문 안에 넣으니까 안되네..)

# while True:
#     a = int(input("숫자 입력해라 게이야 >>> "))
#     bigtit.append(a) and sum(bigtit)
#     if a == 0:
#         print(sum(bigtit))
#         break

# 7. 100 이하의 소수를 출력하는 프로그램을 작성하세요.
# 알고리즘 문제
# 1. N까지 다 나눠본다. 1~N까지 다 돔        알고리즘 => 극단적인 예 1억건
# 2. N/2까지 다 나눠본다.  1 ~ N/2 까지 다 돔      5000만건
# 3. 루트N까지 다 나눠본다.      1억의 루트 만큼
# 1은 소수가 아니겠죠?
# 2는 소수인가요? O
# 3은 소수인가요? 0
def isPrime(value):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

for i in range(1, 101):
    if i == 1:
        continue    # 밑에 로직을 수행하지 않음. => 다음 루프 수행 i => 2
    if i == 2:
        print(i)
        continue
    #cnt = 0     # 나누어 떨어지는 갯수를 파악해보자
    if isPrime(i) :
        print(i)


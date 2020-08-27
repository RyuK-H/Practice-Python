print(True)
print(not True)

animal = "인간"
name = "류기혁"
age = 27
hobby = "망상"
is_adult = age > 20

print("우리집" + animal + "의 이름은 " + name + "에여")
print("정수형은 str로 감싸야한데 ㄷㄷ" + str(age))
print("bool은?" + str(is_adult))

# 연산자
print(1 != 3)
print((3 > 0) & (3 < 5))
print(5 > 4 > 3)
print((3 > 0) | (3 > 4))

# 숫자처리함수
print(abs(-4))
print(pow(4,2))
print(max(5, 10))
print(min(3,-22))
print(round(3.14))
print(round(4.56))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(15))
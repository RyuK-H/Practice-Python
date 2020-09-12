# print(True)
# print(not True)

# animal = "인간"
# name = "류기혁"
# age = 27
# hobby = "망상"
# is_adult = age > 20

# print("우리집" + animal + "의 이름은 " + name + "에여")
# print("정수형은 str로 감싸야한데 ㄷㄷ" + str(age))
# print("bool은?" + str(is_adult))

# # 연산자
# print(1 != 3)
# print((3 > 0) & (3 < 5))
# print(5 > 4 > 3)
# print((3 > 0) | (3 > 4))

# # 숫자처리함수
# print(abs(-4))
# print(pow(4,2))
# print(max(5, 10))
# print(min(3,-22))
# print(round(3.14))
# print(round(4.56))

# from math import *

# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(15))

# from random import *

# print(random())
# print(int(random() * 10))
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randint(1,45))

# sentence = '기혁기혁'
# print(sentence)
# sentence2 = "기혁기혁"
# print(sentence2)
# sentence3 = """
# 기혁기혁
# 와. 이건 뭐여
# """
# print(sentence3)

# gh = "991206-1234567"
# print("성별 : " + gh[7])
# print("연 : " + gh[0:2])
# print("월 : " + gh[2:4])
# print("일 : " + gh[4:6])
# print("생년월일 : " + gh[:6])
# print("뒤 7자리 : " + gh[7:])
# print("뒤 7자리(뒤에서) : " + gh[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(len(python))
# print(python.replace("Python", "JavaScript"))
# print(python.index("n")) 

# print(python.find("JAVA"))
# print(python.count("n"))

# print("이건 또 C네 %d" % 20)
# print("이건 또 C네 %s" % "zz")
# print("이건 또 C네 %c" % "A")
# print("이건 또 C네 %s" % 20)
# print("이건 또 C네 %s zzz %s" % (20, 50))

# print("나는 {}살 입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아해요".format("검정", "노랑"))

# print("나는 {age}살 {color}색을 좋아합니다.".format(age = 20, color ="빨간"))

# a = 30
# b = "노랑"
# print(f"나는 {a} {b}")

# print("백문이 불여일견\n백견이 불여일타")
# print("케켘\"후\"후")
# print("케켘\\\"후\"후")
# print("케켘\t\"후\"후")

# subway = ["홍대역", "광교역", "판교역"]
# print(subway)
# subway.append("세류역")
# subway.insert(2, "강남역")
# print(subway)

# cabinet = {3: "류기혁", 100: "하이"}
# print(cabinet.get(3, "사용가능"))
# print(3 in cabinet)

# menu = ("돈까스", "치즈까스")
# print(menu[0])

# (name, age, hobby) = ("류기혁", "29", "음악")
# print(name, age, hobby)

# my_set = {1,2,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java & python)
# print(java.intersection(python))

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))


# weather = input("오늘 날씨는 어때요? : ")

# if weather == "비" or weather == "눈" :
#   print("우산을 챙기세요.")
# elif weather == "미세먼지" :
#   print("마스크 끼세여")
# else :
#   print("그냥 가세여")

# temp = int(input("기온 : "))

# if 30 <= temp:
#   print("너무 더워요. 나가지 마셈")
# elif 10 <= temp and temp < 30:
#   print("굳굳")
# else:
#   print("추워여")
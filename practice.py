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

# for waiting_no in range(1,6):
#   print("대기번호 : {0}".format(waiting_no))

# customer = "류기혁"
# index = 5

# while index >= 1:
#   print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#   index -= 1
#   if index == 0:
#     print("커피 폐기처분")

# absent = [2, 5]
# no = [7]

# for student in range(1, 11):
#   if student in absent:
#     continue
#   elif student in no:
#     break

#   print("{0}".format(student))

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# def plus(a, b = 10):
#   print(a + b)

# plus(4)

# def profile(name, age, lang1, lang2):
#   print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#   print(lang1, lang2)

# def profile2(name, age, *langs):
#   print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#   for lang in langs:
#     print(lang, end=" ")

# profile("류기혁", "29", "한글", "ㅋㅋ")
# profile2("류기혁", "29", "한글", "ㅋㅋ", "꽥", "끽")

# import sys

# print("a", "b", sep=",", end="?")
# print("a", "b", file=sys.stderr)

# scores = {"수학": 0, "영어": 50, "코딩": 100}

# for subject, score in scores.items():
#   # print(subject, score)
#   print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1,21):
#   print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))

# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >-10}".format(-500))
# print("{0:_<+10}".format(500))
# print("{0:+,}".format(10000000000000))
# print("{0:+,}".format(-10000000000000))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미":["축구", "농구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#   print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#   study_file.write("파이썬 공부 중")

# with open("study.txt", "r", encoding="utf8") as study_file:
#   print(study_file.read())

# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#   print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

class Unit:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

class AttackUnit(Unit):
  def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp)
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}].".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__ (self, flying_speed)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
import random

number = random.randint(1, 99)
chance = 10
count = 0

def input_check(msg, casting=int):
    while True:
        try:
            user_input = int(input("몇 일까요? "))
            return user_input
        except:
            continue

while count < chance:
    count += 1
    user_input = input_check("몇 일까요? ")
    if number == user_input:
        break
    elif user_input < number:
        print("{} 보다 큰 숫자입니다 ".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자입니다 ".format(user_input))

if number == user_input:
    print("정답 {}".format(number))
else:
    print("실패. 정답은 {}".format(number))

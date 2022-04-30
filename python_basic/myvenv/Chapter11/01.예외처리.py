won = input("원화금액을 입력하세요 >>>")
dollar = input("환율을 입력하세요 >>>")

try:
    print(int(won) / int(dollar))
except ValueError as e:
    print("예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("항상 실행되는 코드")


class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가!!!")

try:
    num = int(input("음수를 입력해 주세요 >>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생!", e)
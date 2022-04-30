version = 2.0

def printAuthor():
    print("스타트코딩")

class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"

if __name__ == "__main__":
    print("pay module 실행")

print(__name__)
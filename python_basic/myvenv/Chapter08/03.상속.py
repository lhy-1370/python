# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 날기")

Wolf = Wolf("울프", 1500, 200)
Wolf.move()

Shark = Shark("사크", 3000, 400)
Shark.move()

Dragon = Dragon("드래곤", 8000, 800)
Dragon.move()
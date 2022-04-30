class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self, num):
        self.health += num

goblin = Monster(800,120,300)
print(goblin.health, goblin.attack, goblin.speed)

goblin.decrease_health(100)
print(goblin.health, goblin.attack, goblin.speed)

goblin.get_health(30)
print(goblin.health, goblin.attack, goblin.speed)
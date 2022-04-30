class Unit:
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f"{self.name}(이)가 생성 되었습니다.")
        Unit.count += 1

    def __str__(self):
        return f"[{self.name} 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}"

    def hit(self, demage):
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0

        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0

    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]개")

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)



print(probe)
print(zealot)
print(dragoon)
print(Unit.count)


zealot.demage += 2
print(zealot)

probe.hit(16)
print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)


Unit.print_count()
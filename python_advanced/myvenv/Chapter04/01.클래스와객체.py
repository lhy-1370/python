class Unit:
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f"{self.name}(이)가 생성 되었습니다.")

    def __str__(self):
        return f"[{self.name} 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}"


probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)


print(probe)
print(zealot)
print(dragoon)

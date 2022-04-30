class item:
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을 주었습니다.")

    def discard(self):
        print(f"[{self.name}]을 버렸습니다.")

class weapon(item):
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage
    
    def attack(self):
        print(f"[{self.name}]을 이용해 {self.demage}로 공격합니다.")

class healingitem(item):
    def __init__(self, name, hill):
        super().__init__(name)
        self.hill = hill
    
    def use(self):
        print(f"[{self.name}]을 이용해 {self.hill}로 회복합니다.")        

m16 = weapon("m16", 110)
bungdae = healingitem("붕대", 20)

m16.attack()
bungdae.use()
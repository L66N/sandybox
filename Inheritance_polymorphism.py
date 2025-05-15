#Inheritance

class HanterXHanter:
    name = None
    age = None
    height = None
    hp = None
    hair_style = None

    def __init__(self, name, age, height, hp, hair_style):
        self.name = name
        self.age = age
        self.height = height
        self.hp = hp
        self.hair_style = hair_style

    def get_power(self):
        print("This person has uniq power: ")

class Hisoka(HanterXHanter):
    power = 0
    haunted = 0

    def __init__(self, power, haunted, name, age, height, hp, hair_style):
        super(Hisoka, self).__init__(name, age, height, hp, hair_style)
        self.power = power
        self.haunted = haunted

    def get_power(self):

        print("Name: ", self.name,"\nAge: ", self.age, "\nHeight: ", self.height,"\nHp person: ", self.hp,
              "\nHair style: ", self.hair_style, "\nKilled persons: ", self.haunted)
        super().get_power()
        print(self.power)

class Gon(HanterXHanter):

    best_friends = 0
    hanter = 0

    def __init__(self, power, best_friends, name, age, height, hp, hair_style):
        super(Gon, self).__init__(name, age, height, hp, hair_style)
        self.best_friends = best_friends
        self.power = power

    def get_power(self):
        print("Name: ", self.name,"\nAge: ", self.age, "\nHeight: ", self.height,"\nHp person: ", self.hp, "\nHair style: ", self.hair_style,
              "\nBest friends: ", self.best_friends)
        super().get_power()
        print(self.power)

class Killua(HanterXHanter):

    power = 0
    killer = 0

    def __init__(self, power, killer, name, age, height, hp, hair_style):
        super(Killua, self).__init__(name, age, height, hp, hair_style)
        self.power = power
        self.killer = killer

    def get_power(self):
        print("Name: ", self.name, "\nAge: ", self.age, "\nHeight: ", self.height, "\nHp person: ", self.hp,
              "\nHair style: ", self.hair_style, "\nA killer?: ", self.killer)
        super().get_power()
        print(self.power)

Hisoka = Hisoka("Very strong and fearless person, have some tricks to confuse you.",2000, 'Hisoka', 22, 180, 200, "pink hairstyle")
Gon = Gon("The person has huge aura fireballs, very fast and intiutive.", "Yes. Killua Zoldic", 'Gon Frix', 12, 160, 120, "Black haircut")
Killua = Killua("Very smart and fearless guy, has siblings and powerful skills. The family are the killers, he has a dark side he hide", "Yes", "Killua Zoldic",
                12, 158, 180, "Shiny blond haircut and blue eyes")

Hisoka.get_power()
Gon.get_power()
Killua.get_power()
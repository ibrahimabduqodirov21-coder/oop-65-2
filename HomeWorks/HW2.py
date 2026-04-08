# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье. Здоровье: {self.health}")


# Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


# Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


# Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


# Создаем объекты
warrior = Warrior("Артур", 5, 100, 20, 50)
mage = Mage("Мерлин", 5, 80, 25, 100)
assassin = Assassin("Шэдоу", 5, 70, 30, 90)


# Выбор игрока
choice = input("Выберите героя: Warrior / Mage / Assassin: ")

if choice == "Warrior":
    player = warrior
    enemy = mage
elif choice == "Mage":
    player = mage
    enemy = assassin
elif choice == "Assassin":
    player = assassin
    enemy = warrior
else:
    print("Неверный выбор!")
    exit()


print("\nВы выбрали:", player.__class__.__name__)
print("Противник:", enemy.__class__.__name__)


# Логика игры
if isinstance(player, Warrior) and isinstance(enemy, Assassin):
    print("Warrior победил!")
elif isinstance(player, Assassin) and isinstance(enemy, Mage):
    print("Assassin победил!")
elif isinstance(player, Mage) and isinstance(enemy, Warrior):
    print("Mage победил!")
else:
    print("Противник победил!")

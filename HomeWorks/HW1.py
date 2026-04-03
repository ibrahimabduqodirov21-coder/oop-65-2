class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength


    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


kirito = Hero('Kirito', 1, 100, 10)
asuna = Hero('Asuna', 2, 90, 12)

print(kirito.greet())
kirito.attack()
print(kirito.strength)
kirito.rest()
print(kirito.health)

print()

print(asuna.greet())
asuna.attack()
print(asuna.strength)
asuna.rest()
print(asuna.health)


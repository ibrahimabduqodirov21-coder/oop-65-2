# class Hero:
#
#     # Конструктор класса
#     def __init__(self, name, hp, lvl):
#         # Атрибуты класса
#         self.name_hero = name
#         self.hp_hero = hp
#         self.lvl_hero = lvl
#
#     # Метод класса
#     def action(self):
#         return f"{self.name_hero} hero base action!!"
#
#
# # Обьект|Экземпляр на основе класса
# kirito = Hero("Kirito", 1000, 100)
# asuna = Hero("Asuna", 10000, 1000)
#
# print(kirito.action())
# print(asuna.action())
#
# HeroMage - just for class
# hero_mage - ...


class Hero:

    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты класса
        self.name_hero = name
        self.hp_hero = hp
        self.lvl_hero = lvl

    # Метод класса
    def action(self):
        return f"{self.name_hero} hero base action!!"


# Обьект|Экземпляр на основе класса
kirito = Hero("Kirito", 1000, 100)
asuna = Hero("Asuna", 10000, 1000)
my_str = "just text"






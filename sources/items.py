""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer"


class Weapon:
    def __init__(self):
        raise NotImplementedError("Dop not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "돌맹이"
        self.damage = 4
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "대거"
        self.damage = 5
        self.value = 15


class RustyPick(Weapon):
    def __init__(self):
        self.name = "곡괭이(녹슨)"
        self.damage = 20
        self.value = 50

class SilverPick(Weapon):
    def __init__(self):
        self.name = "곡괭이(은)"
        self.damage = 70
        self.value = 400

class GoldPick(Weapon):
    def __init__(self):
        self.name = "곡괭이(금)"
        self.damage = 100
        self.value = 750

class DiaPick(Weapon):
    def __init__(self):
        self.name = "곡괭이(다이아)"
        self.damage = 250
        self.value = 1850

class MasterPick(Weapon):
    def __init__(self):
        self.name = "곡괭이(전설)"
        self.damage = 450
        self.value = 9999

class Food:
    def __init__(self):
        raise NotImplementedError("Do not create raw Eatable objects.")

    def __str__(self):
        return "{} (+{} Hungry)".format(self.name, self.healing_value)

class CrustyBread(Food):
    def __init__(self):
        self.name = "구운 빵(음식)"
        self.healing_value = 10
        self.value = 20

class burger(Food):
    def __init__(self):
        self.name = "햄버거(음식)"
        self.healing_value = 50
        self.value = 60

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Bandage(Consumable):
    def __init__(self):
        self.name = "붕대"
        self.healing_value = 10
        self.value = 20


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "회복 물약"
        self.healing_value = 50
        self.value = 60


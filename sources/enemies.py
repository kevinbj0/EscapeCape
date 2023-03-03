""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer"


class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

##Low_level_monster
class Sand(Enemy):
    def __init__(self):
        self.name = "Sand"
        self.hp = 10
        self.damage = 2
        self.value = 10

##Level1_monster
class Steel(Enemy):
    def __init__(self):
        self.name = "Steel"
        self.hp = 20
        self.damage = 2
        self.value = 20

##Level1_Boss
class gatekeeper(Enemy):
    def __init__(self):
        self.name = "gatekeeper"
        self.hp = 100
        self.damage = 10
        self.value = 100

##Level2_monster
class Silver(Enemy):
    def __init__(self):
        self.name = "Silver"
        self.hp = 30
        self.damage = 10
        self.value = 50

##Level2_Boss
class Unknown(Enemy):
    def __init__(self):
        self.name = "Unknown"
        self.hp = 200
        self.damage = 15
        self.value = 450

##Level3_monster
class Dia(Enemy):
    def __init__(self):
        self.name = "Diamond"
        self.hp = 100
        self.damage = 15
        self.value = 150

##Boss_monster
class Unknown_Stone(Enemy):
    def __init__(self):
        self.name = "미지의 돌"
        self.hp = 350
        self.damage = 20
        self.value = 9999

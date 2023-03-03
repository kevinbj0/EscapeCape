""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer"

import items
import world
import os
import enemies
import random
import Characters

class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.CrustyBread()]
        self.hp = 90
        self.hungry = 90
        self.gold = 50
        self.victory = False

        self.Floor = 0
        self.Turn = 0
        self.Monster = 0
        self.Boss = 0
        self.ON_Enemies = 0
        self.trader = Characters.Trader()

    ###생존 확인
    def is_alive(self):
        return self.hp > 0

    ###인벤토리
    def print_inventory(self):
        print('')
        print('┏━━━━━━━━┓')
        print('┣━━━ㅁ━━━┫')
        print('┃        ┃')
        print('┗━━━━━━━━┛')
        print()
        print("Inventory:")
        for item in self.inventory:
            print("*" + str(item))
        print("*Gem : {}".format(self.gold))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon : {} (공격력 : {})\n".format(best_weapon, best_weapon.damage))

        input("Press Enter Key to Continue . . .")
        os.system('cls')

    def most_powerful_weapon(self): 
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    ###공격
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        enemy = self.ON_Enemies
        os.system('cls')
        print('          :$# ')
        print('         #@@ #')
        print('        @@@ @$')
        print('      .@@# @@:')
        print('     ,@@# #@# ')
        print('    @.$@ #@@  ')
        print('    @@  @@@   ')
        print('    .@@ $@.   ')
        print('   .$.@@.,    ')
        print('  .*,$.@@     ')
        print(' *.,*.        ')
        print(' :@..         ')
        print('  ~*          \n')
        print("You can use {} 공격!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        self.hp -= enemy.damage
        print("몬스터에 {} 의 데미지".format(best_weapon.damage))
        print("{} 의 피해 입음\n".format(enemy.damage))
        print("enemy Hp : {}".format(enemy.hp))

        if not enemy.is_alive():
            print("{} 을(를) 처치하였습니다!\n".format(enemy.name))
            self.Monster = 0
            self.Boss = 0
            self.gold += enemy.value
            print("{} Gem 채굴 (현재 Gem : {})".format(enemy.value,self.gold))
            if self.Floor == 30:
                self.victory = True

        input("\nPress Enter Key to Continue . . .")
        os.system('cls')
        

    ###회복
    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return
        print('    .@@@@@.    ')
        print('    :@   @:    ')
        print('    *#   #=    ')
        print('    *#   #=    ')
        print('.:**##   ##**:.')
        print('@@###;   ;###@@')
        print('@             @')
        print('@             @')
        print('@             @')
        print('@@###;   :###@@')
        print('.:==##   ##==:.')
        print('    *#   #=    ')
        print('    *#   #=    ')
        print('    :@   @:    ')
        print('    .@@@@@.   \n')  
        print("Choose an item to use to heal: ")  
        for i, item in enumerate(consumables,1):
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("\n아이템 선택 : ")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}\n".format(self.hp))
                input("Press Enter Key to Continue . . .")
                os.system('cls')
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice, try again.")

    ###먹기
    def Eat(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Food)]
        if not consumables:
            print("You don't have any items to Eat!")
            return
        print("Choose an item to use to heal: ")
        for i, item in enumerate(consumables,1):
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("\n아이템 선택 : ")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hungry = min(100, self.hungry + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current Hungry: {}\n".format(self.hungry))
                input("Press Enter Key to Continue . . .")
                os.system('cls')
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice, try again.")

    ###전진
    def Advance(self):
        self.Monster += 1
        self.Floor += 5
        self.Turn += 1
        self.hungry -= 4

        if self.hungry < 0:
            self.Turn += 1
            self.hp -= 4

        r = random.randrange(1,4)
        if self.Floor < 10:
            self.enemy = enemies.Steel()
            if r == 3:
                self.enemy = enemies.Sand()

        elif self.Floor == 10:
            self.Boss = 1
            self.enemy = enemies.gatekeeper()
            os.system('cls')
            print("\n\n 땅이 울리며 주변의 돌들이 모인다 . . . ")
            input("\t\n\n Press Enter Key to Continue . . .")
            os.system('cls')

        elif self.Floor < 20:
            self.enemy = enemies.Silver()
            if r == 3:
                self.enemy = enemies.Steel()

        elif self.Floor == 20:
            self.Boss = 1
            self.enemy = enemies.Unknown()
            os.system('cls')
            print("\n\n 포효가 들리며 화염이 주변을 두른다 . . . ")
            input("\t\n\n Press Enter Key to Continue . . .")
            os.system('cls')

        elif self.Floor < 30:
            self.enemy = enemies.Dia()
            if r == 3:
                self.enemy = enemies.Silver()

        elif self.Floor == 30:
            self.Boss = 1
            self.enemy = enemies.Unknown_Stone()
            os.system('cls')
            print("\n\n 끝이 보이지 않을 정도로 거대한 바위가 보인다 . . . ")
            input("\t\n\n Press Enter Key to Continue . . .")
            os.system('cls')
        
        self.ON_Enemies = self.enemy
        os.system('cls')
        print("\n몬스터 등장 !\n")
        print("Name : {}".format(self.ON_Enemies.name))
        print("Hp : {} \nDamage : {}".format(self.ON_Enemies.hp,self.ON_Enemies.damage))
        input("\nPress Enter Key to Continue . . .")
        os.system('cls')

    ###탐색
    def Search(self):
        r = random.randrange(3,9)
        if r < 8: 
            self.Turn += 1
            self.hungry -= 4
            if self.hungry < 0:
                self.Turn += 1
                self.hp -= 4
                
            self.gold += 50*r
            print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣬⣍⠻⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⠀⠀⡰⠻⢿⣿⣿⣷⠘⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⠰⣿⣷⣄⠈⢿⣿⣿⡇⠙⠋⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⢢⠀⠛⠿⡇⠘⠟⠋⠀⠀⢰⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⢼⣿⣷⣄⡐⠀⢀⣴⣦⠀⡎⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⠼⣿⣿⣿⡇⠀⣿⣿⡿⠐⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print('⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⡏⠀⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print("\n\n{}Gem 을 발견하였다.\n\nGem : {}\n".format(50*r,self.gold))
            input("Press Enter Key to Continue . . .")
            os.system('cls')

        else:
            self.Floor -= 5
            Player.Advance(self)


    ###도망
    def escape(self):
        os.system('cls')
        enemy = self.ON_Enemies
        r = random.randrange(1,3)  
        if r==2:
            print('      :      ')
            print(' ~#@:--=!    ')
            print(' @@@@  *,    ')
            print(' @@@@.       ')
            print(' =@@@@.@@@.  ')
            print('  !=-@@  ,@, ')
            print('=, ~@ !=  ,$ ')
            print('-$=@   @     ')
            print('  ,    @     ')
            print('   $#@@@;    ')
            print('   @    @    ')
            print('  =,    .$:@;')
            print('  @      $=  ')
            print(' !~      \n')
            print(" 도망 성공!")
            self.Monster = 0
            self.Turn += 2
        else:
            self.Turn += 2
            self.hp = self.hp - enemy.damage
            print(" 도망 실패\n")
            print(" enemy Attack! \n -{} Damage\n Trun 2 증가\n\n Player HP : {}".format(enemy.damage,self.hp))

        input("\n Press Enter Key to Continue . . .")
        os.system('cls')

    ##신비의돌(상점)
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gem".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                os.system('cls')
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

    def swap(self, seller, buyer, item):
            if item.value > buyer.gold:
                print("not enough Gem")
                return
            buyer.inventory.append(item)
            buyer.gold = buyer.gold - item.value
            print("Trade Complete!")

    def check_if_trade(self):
            while True:
                os.system('cls')
                print()
                print('          ..........           ')
                print('        !@@@@@@@@@@@@!       ')  
                print('      =@@@          @@@=       ')
                print('     $@@;            ;@@$      ')
                print('     @*#@#=********=#@@*@      ')
                print('    @@  -#@@@@@@@@@@#-  @@     ')
                print('   *@,   $$        $$   ,@*    ')
                print('  -@*    @!        !@    *@-   ')
                print(' .@@     @!        !@     @@.  ')
                print(' -@@!,  ,@:        :@-  ,!@@-  ')
                print('  *@@@@,!@.        .@!,@@@@=   ')
                print('   @@@@@@@::::::::::@@@@@@@    ')
                print('    @@,,@@@@@@@@@@@@@@,,@@     ')
                print('     @@, @*        *@.,@@      ')
                print('      @@,*@.      .@*.@@       ')
                print('      ,@#,@=      =@,$@,       ')
                print('       ~@$!@,    ,@!=@~        ')
                print('        ~@$@$    $@$@~         ')
                print('         ;@@@,  ,@@@;          ')
                print('          *@@#  #@@*           ')
                print('           #@@..@@#            ')
                print('            @@@@@@             ')
                print('             @@@@              ')
                print('              @@.              ')
                print('              ..  ')
                print()
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("돌이 은은한 빛을 냅니다 . . . (B)빌기\n넣어두기 - Enter\n")
                user_input = input()

                if user_input in ['B', 'b']:
                    os.system('cls')
                    print("Here's whats available to buy: ")
                    self.trade(buyer = self, seller = self.trader)
                else:
                    os.system('cls')
                    return
    
    def trading(self):
        Player.check_if_trade(self) 
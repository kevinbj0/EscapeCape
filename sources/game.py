""" Text adventure game
    @insta = @lakshaytalkstocomputer
    @year  = 2018
"""
__author__ = "lakshaytalkstocomputer"

import os
import world
from player import Player
from collections import OrderedDict
import random
import enemies

file = open('Winner_Name.txt','r',encoding='cp949')
Winner_Name = file.read()
file.close()

file = open('Winner_Turn.txt','r')
Winner_Turn = file.read()
file.close()

def play():
        os.system('cls')
        print()
        print()
        print()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃                       Escape UnderWorld                          ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━  게임설명 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃                                                                  ┃")
        print("┃     지하에 갇힌 주인공이 지하 30m에서 지상으로 탈출하는          ┃")
        print("┃     체력 + 피로도 기반 턴제 생존 RPG                             ┃")
        print("┃                                                                  ┃")
        print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        print("┃                         -조작법-                                 ┃")
        print("┃                                                                  ┃")
        print("┃    S: 신비의돌-상점     W: 전진     E: 탐색     i:인벤토리       ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print("\n\tBest Player -> {}, {} Turn Clear! \n".format(Winner_Name,Winner_Turn))
        input("\tPress Enter Key to Continue . . .")
        os.system('cls')
        input(world.Start_tile.intro_text())
        os.system('cls')
        input(world.Start_tile.intro_text2())
        os.system('cls')
        input(world.Start_tile.intro_text3())
        os.system('cls')
        input(world.Start_tile.intro_text4())
        os.system('cls')
        player = Player()
        while player.is_alive() and not player.victory:
            if player.is_alive() and not player.victory:
                choose_action(player)
            elif not player.is_alive():
                print("Your journey has come to an early end! ")
        
        if player.is_alive() == False:
            os.system('cls')
            print("\n\nGAME OVER . . . ")
            input("\t\n\nPress Enter Key to Continue . . .")
            os.system('cls')  
        
        if player.victory == True:
            os.system('cls')
            print("\n\n 부서진 돌을 해치고 나가니 한 줄기 빛이 보인다 . . . ")
            input("\t\n\n Press Enter Key to Continue . . .")
            os.system('cls')
            input(world.VictoryTile.intro_text())

            if(int(Winner_Turn) > player.Turn):
                os.system('cls')
                print('      .~#@@@~.       ')
                print('     ~$@:~~:@#~      ')
                print('     @#   .  #@     ')
                print('    !=   ,#   =*     ')
                print('    @;  $@@   ;@     ')
                print('   ;@,  #*@   .@!    ')
                print('   !@    -@    @!    ')
                print('   :@-   -@   ,@:    ')
                print('    @;   -@   ;@     ')
                print('    =@-  ,=  -@=     ')
                print('    :@@:    :@@:     ')
                print('    @;=@@##@@=;@     ')
                print('   ~@~ ~~@@~~ -@~    ')
                print('   !@    @@    @!    ')
                print('  .#;   $##$   ;#.   ')
                print('  .@    #==#    @.   ')
                print('  @@@@;~@  @~;@@@@   ')
                print(' ,,..!@#$  $#@!..,,  ')
                print('      *@,  ,@*      ')
                print('\n최고기록 경신!\n')
                Name_input = input("Winner_Name: ")
                file = open('Winner_Name.txt','w',encoding='cp949')
                file.write(Name_input)
                file.close()

                file = open('Winner_Turn.txt','w')
                file.write(str(player.Turn))
                file.close()

                print('\n이름을 새겼습니다.\n')
                input("\t\nPress Enter Key to Exit . . .") 

def get_available_actions(player):
    actions = OrderedDict()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("┃ Floor : {} \t   Turn : {}".format(player.Floor,player.Turn))
    print("┃")
    print("┃ Hungry : {}".format(player.hungry))
    print("┃ HP : {}  \t    Gem : {}".format(player.hp,player.gold))
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if player.Monster == 1:
        best_weapon = player.most_powerful_weapon()
        print("Your best weapon : {} (공격력 : {})".format(best_weapon, best_weapon.damage))
        print("Name : {}".format(player.ON_Enemies))
        if player.Floor == 10:
            print('                 ~@@@@@@                ')
            print('                 ,#@@@@@                ')
            print('              .:;$@@@@@;                ')
            print('           ~~=#@@@@@@@@@=.              ')
            print('        ,$@@@@@@@@@@@@@@@#:~-           ')
            print('        *@@@@@@@@@@@@@@@@##@#*          ')
            print('       ,@@@@@@@@@@@@@@@@@#####$         ')
            print('       ,@@@@@@@@@@@@@@@@#@@@@@@         ')
            print('       ,@@@@@@@@@@@@@@@@@@@@@@@;        ')
            print('       !@@@@@@@@@@@@@@@@@@@@@@@~        ')
            print('      ,@@@@@$*@@@@@@@@@@@@@@@@@!        ')
            print('      =@@@@@; #@@@@@@@@@@@$@@@@=.       ')
            print('     ,#@@@@@  -@@@@@@@@@@*-@@@@@,       ')
            print('     !@@@@@,  .$@@@@@@@@@,.$@@@@=       ')
            print('     @@@@@=   ,@@@@@@@@@@~ -@@@@#;      ')
            print('    :#@#@@#.  ,@@@@@@@@@@#  @@@@##-     ')
            print('    !##@@@=   :@@@@@@@@@@@  @@@@##-     ')
            print('    :#@@@@!   =@@@@@@@@@@@  =@@@##,     ')
            print()
        elif player.Floor == 20:
            print('  ~,                                     ')
            print('  ,@            .                        ')
            print('  ,@@,          #@@:                     ')
            print('  ,@@:         -@@@@-                    ')
            print('  ,@@@:         #@@=                     ')
            print('  @@@@@:       -@@@#.                    ')
            print(' -*@@@@$         !@@-                    ')
            print('   =@@@@#        ~@@-                    ')
            print('   :@@@@@!       ~@@-                    ')
            print('    @@@@@@.      :@@-                 ,  ')
            print('    @@@@@@@-     #@@-            -~:@,   ')
            print('   !~;@@@@@@=   ,@@@-       :$$$$@@@@$!  ')
            print('      .@@@@@@*#@@@@$.       :@@@@@@@#-   ')
            print('       *@*-!@@@@@@@$.       #@@@@@@@,    ')
            print('       -  ,@@@@@@@@@:     .@@@@@@@@.     ')
            print('         ~@@*@@@@@@@@    .#@@@@@@@=      ')
            print('       .,@#  @@@@@@@@@~.*@@@@@@@@@!      ')
            print('      .#@,   @@@@@@@@@@@@@@@@@@@;:.      ')
            print('      .~    ,@@@@@@@@@@@@@@@@@#          ')
            print('      ..-. ~@@@@@@**@@@@@@@@@#- ..       ')
            print('      , - #@@@@@@= ,=@@@@@@@@@. -        ')
            print()
        elif player.Floor == 30:
            print('                        @@@       @@@  ')
            print('@@@          @@@@@     @@@       :@@@@  ')
            print('@@@@,       ..~@@@@@@@@@!        @@#@@* ')
            print('@@#@@    .;!#@@@@@!;#@@@$       !@@ !@$.')
            print('@@.@@* !@@@@@@@*   -@@#@@,     .#@~ .@@,')
            print('@@ !@@@@@@#*!,    -@@*.@@,     :@#,  #@#')
            print('@@ .@@@@!,.       $@@  @@-     @@=   #@;')
            print('@@  ;@@-         !@@,  @@*    :@@   :@@,')
            print('@@   !@#.       ,@@*   !@@   .@@:   $@* ')
            print('@@   -@@;       @@#     @@   !@@,  ,@@- ')
            print('@@;   *@@.     *@@.     @@,  $@!   @@=  ')
            print('@@@@.  @@@    ,@@!      @@! -@@   *@@.  ')
            print('.!@@@=,,@@~  ,@@$       *@= @@* ~=@@*   ')
            print('  ,=@@#=*@#. *@@.       :@=!@@ ;@@@;.   ')
            print('    *$@@@@@::@@~        :@##@*@@@$-     ')
            print('     .:@@@@@@@$         ~@@@@@@@;.      ')
            print('       .$@@@@@$;-.......,#@@@@#~        ')
            print('         ;=@@@@@@@@@@@@@@@@@@*          ') 
            print('           :*#@@@@@@@@@@@@@@.           ')
            print()
        else:
            print()
            print('     $@@@@@$@@$     ')
            print('    -@@@@@@@@@@-    ')
            print('    !@@@@@@@@@@!    ')
            print('    !@@@@@@@@@@*    ')
            print('    !@@ ;@@! @@*    ')
            print('    !@@,=@@=,@@*    ')
            print('    !@@@@@@@@@@*    ')
            print('    ~;;;;;;;;;;~    ')
            print(' #@              @# ')
            print('*@@ @@@@@@@@@@@@ @@*')
            print('@@@ @@@@@@@@@@@@ @@@')
            print('@@@ =@@@@@@@@@@= @@@')
            print('@@@!            !@@@')
            print('#@@@~,@@@@@@@@,-@@@#')
            print('@@@@~,@@@@@@@@,-@@@@')
            print()    
        print("HP : {}  \nDamage : {}\n".format(player.ON_Enemies.hp,player.ON_Enemies.damage))
        print("Choose an action: ")
    if player.Monster == 0:
        action_adder(actions, 'w', player.Advance, "전진") 
        action_adder(actions, 'e', player.Search, "탐색") 
        action_adder(actions, 's', player.trading, "신비의돌(상점)") 
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
    if player.hungry < 100:
        action_adder(actions, 'q', player.Eat, "Eat")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if player.Monster == 1:
        action_adder(actions, 'a', player.attack, "공격") 
        if player.Boss != 1:
            action_adder(actions, 'd', player.escape, "도망") 

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(player):
    action = None
    while not action:
        available_actions = get_available_actions(player)
        
        ##설명추가
        action_input = input("Action: ") ##행동을 입력받음
        action_input = action_input.lower() ##대문자 입력 시 소문자로 변경

        if action_input == 'money': 
            player.gold += 999000
            os.system('cls')
            break
        action = available_actions.get(action_input)
        os.system('cls')
        if action:
            action()
        else:
            os.system('cls')
            print("Invalid action!")
            input("\t\n\nPress Enter Key to Continue . . .")
            os.system('cls')

play()

#Andrew Hilton 4th pd
#Concrete jungle - dungeon crawler set in urban city BETA BUILD 1.0.0
import math
import random
import os
### Misc Classes ###
user=0
class Item:
    def __init__(self, initname, initdesc, initDPS, initdura, initvalue):
        self.name=initname
        self.desc=initdesc
        self.DPS=initDPS
        self.dura=initdura
        self.value=initvalue
        
    def __str__(self):
        return str(self.name) + str(self.desc) + str(self.DPS) + str(self.dura) + str(self.value)
class Inventory:
    def __init__(self):
        self.items = {}
        global inventory
        global user
    def new_item(self, item):
        self.items[item.name] = item
        
    def del_item(self, item):
        del self.items[item.name]
    def consume(self):
            if user.pos.actions == "food":
                if user.money >= 5:
                    user.money = user.money - 5
                    user.energy = user.energy + 30
                    print("You get 30 energy from food upon spending $5.")
                    user.player_menu()
            print("You may not eat here, or you don't have enough money!")
            user.player_menu()
    def __str__(self):
        output = '\t'.join([" ", " ", " ", " ", " "])
        for item in self.items.values():
            output += '\n' + '\t'.join([str(x) for x in ['\n', item.name, '\n', item.desc, '\n', "DPS ;        ", item.DPS, '\n', "Durability ; ", item.dura, '\n', "Value ; ", item.value]])
        return output
class Room:
    def __init__(self, name, desc, actions, x, y):
        global rlist
        self.name = name
        self.desc = desc
        self.actions = actions
        self.x = x
        self.y = y
    def getpos(self):
        pos=[self.x, self.y]
        return pos
    def getlinks(self):
        global user
        index = 0
        ava_list = []
        choice = 0
        newpos=user.pos
        print("You are at", user.getroom())
        print("You can move to:")
        for i in rlist:
            if i.x == self.x:
                if i.y == (self.y - 1) or i.y == (self.y + 1):
                    index = index+1
                    print(str(index)+". "+i.name)
                    ava_list.append(i)
            if i.y == self.y:
                if i.x == (self.x - 1) or i.x == (self.x + 1):
                    index = index+1
                    print(str(index)+". "+i.name)
                    ava_list.append(i)
        #print(ava_list)
        choice = input("Enter which room/street number you wish to move to (Uses 5 energy)")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "1":
            newroom1=ava_list[0]
            user.setposxy(newroom1.x, newroom1.y)
            user.setpos(ava_list[0])
        elif choice == "2":
            try:
                newroom2=ava_list[1]
                user.setposxy(newroom2.x, newroom2.y)
                user.setpos(ava_list[1])
            except:
                print("Improper input")
                user.player_menu()
        elif choice == "3":
            try:
                newroom3=ava_list[2]
                user.setposxy(newroom3.x, newroom3.y)
                user.setpos(ava_list[2])
            except:
                print("Improper input")
                user.player_menu()
        elif choice == "4":
            try:
                newroom4=ava_list[3]
                user.setposxy(newroom4.x, newroom4.y)
                user.setpos(ava_list[3])
            except:
                print("Improper input")
                user.player_menu()
        else:
            print("Improper input")
            user.player_menu()
        user.setpos(newpos)
        user.player_menu()
    def enterroom(self):
        if self.actions == None:
            print("You may not enter, or there is nothing to enter!")
            user.player_menu()
        else:
            if self.actions == "guitarstore":
                guitarstore()
            elif self.actions == "gasstation":
                gasstation()
            elif self.actions == "airport":
                airport()
        
    def __str__(self):
        return(str(self.name))
class Enemy:
    def __init__(self, initname, initDPS, initHP):
        self.name=initname
        self.DPS=initDPS
        self.HP=initHP
    def atk_player(self, name, DPS, HP):
        pass
###PLAYER CLASS - WIP###
class Player:
    global user
    global rlist
    global inventory
    def __init__(self, initHP, initenergy, initx, inity, initinv, initpos, initmoney):
        position = []
        self.HP=initHP
        self.energy=initenergy
        self.x=initx
        self.y=inity
        self.inv=initinv
        self.pos=initpos
        self.money =initmoney
    def getpos(self):
        global position
        position =[self.x, self.y]
        return position
    def getroom(self):
        room=self.pos
        return room
    def player_menu(self):
        if user.energy <= 0:
            print('''
You've run entirely out of energy, you passed out and were taken into a hospital.
Due to your homelessness, you are unable to pay the medical bills, and sent further into debt.
You have lost the game.''')
            lose_game("Energy = 0")
        elif user.HP <= 0:
            print('''You've run entirely out of health, you passed out and were taken into a hospital.
Due to your homelessness, you are unable to pay the medical bills, and sent further into debt.
You have lost the game.''')
            lose_game("Health = 0")
        randnum = random.randint(0, 12)
        randnum2 = random.randint(0, 16)
        randnum3 = random.randint(0, 10)
        randnum4 = random.randint(0, 9)
        randnum5 = random.randint(0, 20)
        randnum6 = random.randint(0, 30)
        if randnum3 == 1:
            print("You stumble upon a trashcan with a mostly uneaten meal inside. Would you like to eat it for 15 energy?")
            trashchoice = input("y/n")
            if trashchoice == "y":
                user.energy = user.energy + 15
                user.HP = user.HP - 5
            elif trashchoice == "n":
                print("You pass up the garbage, what a waste")
        elif randnum2 == 1:
            print("You find a $5 bill on the ground.")
            user.money = user.money + 5
        elif randnum == 1:
                print("A group of onlookers will pay you to be entertained by guitar playing. This will take 10 energy.")
                choiceguitar = input("Do you wish to accept? y/n")
                if user.energy < 10:
                    print("You do not have enough energy")
                    user.player_menu()
                if choiceguitar == "y":
                    user.energy = user.energy - 10
                    randmoney = random.randint(25, 100)
                    user.money = user.money + randmoney
                    print("You play, expending 10 energy for", randmoney, "dollars")
                elif choiceguitar == "n":
                    pass
        elif randnum4 == 1:
            print("You pass by some kind and wealthy looking people. Would you like to beg for some change?")
            abciwa=input("y/n")
            if abciwa == "y":
                howmuchmoney = random.randint(5, 125)
                print("You beg for money, getting", str(howmuchmoney), "dollars in exchange for 10 hp.")
                user.money = user.money + howmuchmoney
                user.HP = user.HP - 10
        elif randnum5 == 1:
            print("A violent gang beats you up and mugs you, you lose half of your money and 30 HP")
            user.HP = user.HP - 30
            user.money = (user.money // 2)
        elif randnum6 == 1:
            print("A caring philanthropist feels bad for your condition, and gives you $500! Your HP goes up by 20 aswell.")
            user.HP = user.HP + 20
            user.money = user.money + 500
        print('''
 1. Move
 2. Inventory
 3. Enter/Open
 4. Menu
 5. Buy Food
''')
        print('''ENERGY = ''', str(self.energy))
        print('''MONEY = ''', str(self.money))
        print('''HP = ''', str(user.HP))
        print("   You are at", str(user.pos), "; ")
        print(user.pos.desc)
        x=input("Input 1-5; ")
        if x == "1":
            if self.energy > 0:
                self.energy = self.energy - 5
                os.system('cls' if os.name == 'nt' else 'clear')
                user.move()
            else:
                print("You do not have enough energy to do that!")
                user.player_menu()
        elif x == "2":
            inv()
        elif x == "3":
            user.pos.enterroom()
        elif x == "4":
            menu()
        elif x == "9":
            user.attack()
        elif x == "a":
            cheat_inv()
        elif x == "5":
            inventory.consume()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid inputs, try again")
            user.player_menu()
    def move(self):
        self.pos.getlinks()
        
    def attack(self):
        pass
    def getpos(self):
        pass
    def setpos(self, newpos):
        self.pos = newpos
        user.player_menu()
    def setposxy(self, newposx, newposy):
        self.x = newposx
        self.y = newposy
        return True

###Streets###
r1 = Room("Martin Luther King Upper End", "A bustling street, with two more sections down the road, connected to a guitar store and a burger king.", None, 0, 2)
r2 = Room("Martin Luther King Middle", "A bustling street, with two more sections on either side.", None, 0, 1)
r3 = Room("Martin Luther King Lower End", "A bustling sreet with two more sections up the road.", None, 0, 0)
r4 = Room("1st Street Middle Right Side", "A very long street running through the center of the city.", None, 1, 1)
r5 = Room("1st Street Left Side", "A very long street running through the center of the city.", None, -1, 1)
r6 = Room("1st Street Right Side", "A very long street running through the center of the city.", None, 2, 1)
r7 = Room("1st Street Far Right Side", "A very long street running through the center of the city.", None, 3, 1)
r8 = Room("1st Street Far Left Side", "A very long street running through the center of the city, this side is connected to a convenience store", "gasstation", -2, 1)
r9 = Room("Greg Street Lower", "Gregorious Streetorious, a small, mostly uninhabited street, with one more section above.", None, 0, 3)
r10 = Room("Greg Street Middle/Top", "Gregorious Streetorious, a small, mostly uninhabited street, with one more section below.", None, 0, 4)
r11 = Room("2nd Street Middle", "A somewhat busy street, with two more sections on either side.", None, 0, 5)
r12 = Room("3rd Street Right Side", "A somewhat busy street, with two more sections to the left.", None, 1, 5)
r13 = Room("2nd Street Left Side", "A somewhat busy street, with two more sections to the right.", None, -1, 5)
r14 = Room("Citytropolis National Airport", "An enormous airport on the upper end of the city.", "airport", 0, 6)
r15 = Room("Burger King", "A fast-food chain.", "food", 1, 2)
r16 = Room("Shell Gas Station", "A convenience store.", "gasstation", -2, 1)
r17 = Room("Guitar center", "A musical store.", "guitarstore", -1, 2)
rlist=[]
rlist += [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17]
### Functions ###
def inv():
    global inventory
    print(inventory)
    user.player_menu()

        
inventory = Inventory()
user=Player(100, 50, 0, 0, inventory, r1, 99999)
inventory.new_item(Item("Lighter ", "A Bic lighter, still has juice. ", 1, 30, 5))

def change_inv(item, add_or_del):
    global user
    global inventory
    if add_or_del == "add":
        if item == "guitar":
            inventory.new_item(Item("Guitar ", "A wooden instrument, can you play? ", 9, 50, 100))
        elif item == "knife":
            inventory.new_item(Item("Knife ", "A metal blade, be careful. ", 20, 15, 30))
        elif item == "lighter":
            inventory.new_item(Item("Lighter ", "A Bic lighter, still has juice. ", 1, 30, 5))
        if item == "brokenguitar":
            inventory.new_item(Item("Broken Guitar ", "A barely stringed wooden instrument, tough to play. ",  9, 20, 50))
    elif add_or_del == "del":
        if item == "guitar":
            inventory.del_item(Item("Guitar", "A wooden instrument, can you play? ", 9, 50, 120))
        elif item == "knife":
            inventory.del_item(Item("Knife ", "A metal blade, be careful. ", 20, 15, 30))
        elif item == "lighter":
            inventory.del_item(Item("Lighter ", "A Bic lighter, still has juice. ", 1, 30, 5))
        elif item == "brokenguitar":
            inventory.del_item(Item("Broken Guitar ", "A barely stringed wooden instrument, tough to play. ",  9, 20, 50))
    user.player_menu()
def cheat_inv():
    item=input("what item")
    choice=input("what choice")
    change_inv(item, choice)
def guitarstore():
    global user
    global inventory
    print('''
1. New guitar - $130
2. Repair a broken guitar - $75
3. Sell a new guitar - $100
4. Leave - Free!''')
    x=input("Input 1-4; ")
    if x == "1":
        if user.money >= 130:
            user.money = user.money - 130
            change_inv("guitar", "add")
        else:
            print("You don't even have the money for that!")
            user.player_menu()
    elif x == "2":
        if user.money >= 75:
            user.money = user.money - 75
            inventory.del_item(Item("Broken Guitar ", "A barely stringed wooden instrument, tough to play. ",  9, 20, 50))
            change_inv("guitar", "add")
    elif x == "3":
        try:
            inventory.del_item(Item("Guitar ", "A wooden instrument, can you play? ", 9, 50, 100))
            user.money = user.money + 100
            print("You sell the guitar for $100")
            user.player_menu()
        except:
            print("You do not have this to sell!")
            user.player_menu()
    elif x == "4":
        user.player_menu()
    else:
        print("Improper inputs!")
        user.player_menu()
def gasstation():
    global user
    global inventory
    print('''
1. Snack - $3
2. Leave - Free!''')
    x=input("Input 1-2; ")
    if x == "1":
        if user.money >= 3:
            user.money = user.money - 3
            user.energy = user.energy + 20
            print("You spend $3 on a light snack and get 20 energy, and 10 HP")
            user.HP = user.HP + 10
            user.player_menu()
    elif x == "2":
        user.player_menu()
    else:
        print("Invalid input!")
        user.player_menu()
    print("You don't have enough money!")
    user.player_menu()
def airport():
    global user
    global inventory
    print('''
1. Standard Air Ticket - $450
2. Snacks - $15
3. Leave - Free!''')
    choice=input("Input 1-3; ")
    if choice == "1":
        if user.money >= 450:
            print("You buy a ticket and escape the city. You win!")
            win_game("You bought a plane ticket and escape to a country more friendly to the homeless!")
        else:
            print("You don't have enough money.")
            user.player_menu()
    elif choice == "2":
        if user.money >= 15:
            print("You waste $15 on airport food, gaining 45 energy, and 10 HP")
            user.energy = user.energy + 45
            user.HP = user.HP + 10
            user.money = user.money - 15
            user.player_menu()
        else:
            print("You don't have enough money.")
            user.player_menu()
        user.player_menu()
    user.player_menu()
        
### Menu ###
def menu():
    print('''------------------
| 1. New Game    |
------------------''')
    x=input("Input ; ")
    if x == "1":
        new_game()
    elif x == "2":
        load_game()
    elif x =="3":
        admin()
    elif x =="4":
        debug()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid inputs, try again")
        menu()
def new_game():
    print("DISCLAIMER ; THIS IS A BETA BUILD, Things yet to be added include more streets/buildings and more functionality for items, aswell as possibly balance issues as they arise.")
    print('''
You find yourself in the midsts of a sprawling city. Skyscrapers tower over you, creating a sense
of insignificance as hundreds of pedestrians pass you in your daze. Upon coming to your senses,
you decide you must survive on the streets atleast long enough to build up a hefty enough income
to escape the concrete jungle.
''')
    user.player_menu()
def lose_game(reason):
    for i in range(30):
        print("YOU LOSE DUE TO; ", str(reason))
        lose_game(reason)
def win_game(reason):
    for i in range(30):
        print("YOU WIN DUE TO; ", str(reason))
        win_game(reason)
        break
def admin():
    print("NOTHING TO SEE HERE")
    menu()
def debug():
    print("NOTHING TO SEE HERE")
    menu()
def load_game():
    print("Loading games is tough work! Check back here later :)")
    menu()
randpos = random.choice(rlist)
inventory.new_item(Item("Broken Guitar ", "A barely stringed wooden instrument, tough to play. ",  9, 20, 50))
user=Player(100, 50, 0, 0, inventory, randpos, 30)
menu()

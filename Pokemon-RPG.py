import random
from Items import Item, Crit_Potion, Pokeball, Master_Pokeball, Health
from random import randint
from pokemon_art import bulbasaur_art, charmander_art, squirtle_art, logo, pokeball_art, goodbye_message, professor_oak, nurse_joy
import os
import time
from pygame_tester import nineties_intro, battle_song
from sys import exit

# POKEMON CLASSES


class Pokemon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.bounty = 50
        self.items = []
        self.attack = attack
        # self.secondary_attack = secondary_attack
        # self.special_attack = special_attack
        

class Charmander(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))


class Squirtle(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))

class Bulbasaur(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))
        

class Gyarados(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))
        
class Mewtwo(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))



def menu_launch():
    os.system("clear")
    logo()
    starter_pokemon = {
    1: Charmander("Charmander", 100, 50),
    2: Squirtle("Squirtle", 100, 40),
    3: Bulbasaur("Bulbasaur", 100, 45),
    }
    
    user_name = input("What is your name young trainer? ")
    time.sleep(2)
    os.system("clear")
    professor_oak()
    print("")
    print("Nice to meet you %s. I'm Professor Oak. I'll be helping you on your quest to become a pokemon trainer. Let's get you set up with a pokemon. Choose wisely, this pokemon will become your best friend and trusted ally." % (user_name))
    print("")
    print("====================================================================================")
    print("")
    print("Choose your pokemon:")
    print("""
    1. Charmander
    2. Squirtle
    3. Bulbasaur
              """)
    # user_input = int(input(""))
    # print(user_input)
    
    player = None
    running = True
    while running:
        pokemon_choice = int(input("Who do you choose? "))
        time.sleep(1)
        os.system("clear")
        if pokemon_choice == 1:
            player = starter_pokemon[1]
            charmander_art()
        elif pokemon_choice == 2:
            player = starter_pokemon[2]
            squirtle_art()
        elif pokemon_choice == 3:
            player = starter_pokemon[3]
            bulbasaur_art()
    
        else:
            print("Please choose a number 1 - 3.")
    
        print("What an excellent choice!! Take care of %s for us!" % (player.name))
        #Tests the selection above - delete later
        #print(player.__dict__)
        play_song = False
        running = False
        main(player)



def main(player):
    print("""
          1. Find wild pokemon
          2. Visit Nurse Joy
          3. Visit the Store
          4. Quit 
    
          """)
    main_input = int(input("What do you and %s want to do? " % (player.name)))
    main_running = True
    while main_running == True:
        if main_input == 1:  
            battle(player)
        elif main_input == 2:
            medic(player)
        elif main_input == 3:
            shop(player)
        elif main_input == 4:
            time.sleep(1)
            os.system("clear")
            goodbye_message()
            pokeball_art()
            time.sleep(3)
            main_running = False
            exit()
        else:
            print("Please type a number 1 - 4. ")
            time.sleep(2)
            os.system("clear")
            logo()
            main(player)
            


def battle(player):

    charizard = Pokemon("Charizard", 100, 20)
    blastoise = Pokemon("Blastoise",100, 20)
    mewtwo = Pokemon('Mewtwo', 100, 25)
    squirtle = Pokemon('Squirtle', 100, 25)

    # characters = [" ", charizard, blastoise, mewtwo, squirtle]

    opponent_list = [charizard, blastoise, mewtwo, squirtle]
    opponent = random.choice(opponent_list)
    battle = True
    print("A wild %s appears!" % (opponent.name)) 
    while battle:
        # random_number = randint(1, 5)
        # opponent = opponent_list[random_number]

        time.sleep(2)
        #Launch into battle sequence here
        os.system('clear')
        # print(logo)
        logo()
        action = input("""What would you like to do?
            1.Attack
            2.Defend
            3.Use an item
            4.Flee
            """)
        if action == '1' and player.health > 0:
            time.sleep(1)
            print("%s attacked %s." % (player.name, opponent.name))
            time.sleep(3)
            print(' ')
            opponent.health -= player.attack 
            print("%s's health has decreased to %d." % (opponent.name, opponent.health))
            time.sleep(2)
            #Add statement to make value 0 to avoid negative health
            if opponent.health <= 0:
                #add delay print later
                print("%s has fainted!" % opponent.name)
                # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                break
            else:
                pass
            
            if opponent.health > 0:
                print("""============================================================""")
                print("It's your enemy's turn to attack.")
                time.sleep(1)
                player.health -= opponent.attack
                print("""%s's health is now %d""" % (player.name, player.health))
                time.sleep(4)
            
            else:
                print("Please enter a valid option.")
        
        elif action == '2':
            random.randrange(1, 4)
            if random.random() <= 0.5:
                print("%s defended itself and took no damage." % (player.name))
                time.sleep(3)

            else:
                player.health -= opponent.attack
                print("%s defended itself, but it failed." % (player.name)) 
                print("%s health is: %d" % (player.name, player.health))
                time.sleep(3)
        elif action == '4':
            print("You have fled the battle!")
            time.sleep(2)
            main(player)
        
        else:
            print("Please type in a number 1 -4")

    

def medic(player):
    os.system("clear")
    nurse_joy()
    print("Hello, and welcome to the Pokemon Center. We restore your tired Pokemon to full health. Do you want to heal %s? " % (player.name))
    print("")
    # print("%s's health is %s" % (player.name, player.health))
    medic_input = input("")
    lower_medic_input = medic_input.lower()
    if lower_medic_input == "yes":
        player.health = 100
        print("%s is at full health." % (player.name))
        time.sleep(2)
        os.system("clear")
        logo()
        main(player)
    elif lower_medic_input == "no":
        print("%s looks tired. :( Are you sure? " % (player.name))
        second_chance = input("")
        if second_chance == "yes":
            main(player)
        else:
            player.health = 100
            print("%s is at full health." % (player.name))
    else:
        print("Please type yes or no.")
        
    


def shop(player):
    print("Welcome to the shop! What can we help you with today?")
    print("""
          1. Purchase Potions 
          2. Purchase attack items
          3. Purchase Pokeballs
          4. View Inventory
          5. Exit the shop
          """)
    shop_input = int(input(""))
    if shop_input == 1:
        print("Which potion would you like to purchase?")
        print("""
              1. Health Potion (25 coins)
              2. Attack Potion (30 coins)
              3. Defense Potion (25 coins)
              4. View inventory
              5. Return to shop menu
              """)
        potion_input = int(input(""))
        if potion_input == 1:
            #Future: subtract from bounty/coins
            player.items.append("Health Potion")
            #check to delete later:
            print(player.items)
            print("Thanks for the purchase!")
        elif potion_input == 2:
            player.items.append("Attack Potion")
            print("Thanks for the purchase!")
        elif potion_input == 3:
            player.items.append("Defense Potion")
            print("Thanks for the purchase!")      
        elif potion_input == 4:
            print(player.items)
        elif potion_input == 5:
            shop(player)
        else:
            print("Please type a number 1 - 5")
    
    #Still need to input options for 2 and 3 
    
    elif shop_input == 4:
        print(player.items)
    
    elif shop_input == 5:
        main(player)

    else:
        print("Please type a number 1-5. ")

    # main(player)



menu_launch()



    



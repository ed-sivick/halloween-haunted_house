import random
import time


def print_sleep(start_message):
    print(start_message)
    time.sleep(2)


def visit_character(pouch):
    print_sleep("Please enter the character that might help you exit"
                " the Haunted House:\n")
    character = input("Witch\n"
                      "Pirate\n"
                      "Troll\n\n")
    if character.lower() == "witch":
        witch(pouch)
    elif character.lower() == "pirate":
        pirate(pouch)
    elif character.lower() == "troll":
        troll(pouch)
    else:
        print_sleep("Sorry, but that is not a valid option.")
        visit_character(pouch)


def start():
    print_sleep("\nIt's Halloween night, and you're trapped in a"
                " Haunted House with only a small empty pouch in hand.")
    print_sleep("There is an angry Troll guarding the Exit door in"
                " front of you.")
    print_sleep("To your left is a greedy Pirate in a room counting his"
                " gold coins.")
    print_sleep("To your right is a horrid Witch stirring a smoky cauldron"
                " in the kitchen.\n")


def witch(pouch):
    print_sleep("You choose to visit the horrid Witch.\n")
    if "door_key" in pouch:
        print_sleep("'You again?!  You already tasted my brew for a gold"
                    " coin'")
        print_sleep("'Now leave my kitchen at once!'\n")
        visit_character(pouch)
    elif "gold_coin" in pouch:
        print_sleep("'Double, double toil and trouble!  You already have"
                    " a gold coin!'")
        print_sleep("'Now leave this room before I turn you into a Newt!'\n")
        visit_character(pouch)
    else:
        print_sleep("She invites you into her kitchen, and you notice the"
                    " treasure chest of gold coins sitting on a table"
                    " behind her.")
        print_sleep("She says; 'You must taste a sample of my brew for one"
                    " of those gold coins', and watches as you taste the"
                    " brew from her ladle.")
        print_sleep("She gives you a coin, and you leave the room feeling a"
                    " bit dizzy.\n")
        pouch.append("gold_coin")
        visit_character(pouch)


def pirate(pouch):
    print_sleep("You choose to visit the greedy Pirate.")
    print_sleep("He meets you at the entrance of the room, and grabs the"
                " pouch from your hand, opens it, and peers inside.\n")
    if "door_key" in pouch:
        print_sleep("'Arrr!  I already gave you a door key!'")
        print_sleep("'Now leave this room before I make you walk the"
                    " plank!'\n")
        visit_character(pouch)
    elif "gold_coin" in pouch:
        print_sleep("'Shiver Me Timbers!  You have one of my gold coins!'")
        print_sleep("'I will give you a door key for the Troll if you can win"
                    " a coin flip'")
        print_sleep("'Heads- I WIN, or Tails- YOU WIN.'\n")
        flip = random.choice(["Heads.", "Tails."])
        print("The Pirate flips the coin and the result is", flip)
        if flip == "Heads.":
            print("'Aye aye!  I WIN, and no key for you unless you bring me"
                  " another coin from the Witch!'")
            pouch.remove("gold_coin")
            visit_character(pouch)
        else:
            print_sleep("'Arrr!  YOU WIN, now take this key before I change"
                        " my mind!'")
            pouch.append("door_key")
            visit_character(pouch)
    else:
        print_sleep("He says; 'What, no treasure?! I can help you, but you"
                    " must wager one gold coin for a door key.'")
        print_sleep("'However, the witch has stolen my treasure chest of"
                    " gold coins.'")
        print_sleep("'Now leave this room before I make you walk the"
                    " plank!'\n")
        visit_character(pouch)


def troll(pouch):
    print_sleep("You choose to visit the angry Troll.\n")
    if "door_key" in pouch:
        print_sleep("You remove the door key from the pouch and give it"
                    " to the troll.")
        print_sleep("The troll says; 'Ooooh!  I see you visited the Witch"
                    " and Pirate.'")
        print_sleep("'YOU WIN!  You may leave this house, but you'll be"
                    " back!'\n")
        print_sleep("'...you see that witches brew turns people into trolls!'")
        print_sleep("'I too was just like you, but now I'm trapped in this"
                    " house!'\n\n")
        print_sleep("GAME OVER\n")
        play_again()
    else:
        print_sleep("The angry Troll says; 'You have no door key to exit"
                    " this house!'")
        print_sleep("'Now Go Back until you find a key!'\n")
        visit_character(pouch)


def again_input(prompt, yes, no):
    while True:
        response = input(prompt).lower()
        if yes in response:
            break
        elif no in response:
            break
        else:
            print_sleep("Sorry, but that is not a valid option.\n")
    return response


def play_again():
    response = again_input("Would You Like To Play Again?\n"
                           "Please enter 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_sleep("OK, Have A Nice Day!")
        exit()
    elif "yes" in response:
        play_game()


def play_game():
    pouch = []
    start()
    visit_character(pouch)
    witch(pouch)
    pirate(pouch)
    troll(pouch)


play_game()

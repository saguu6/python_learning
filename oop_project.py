#war game
from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#mycards = [(s,r) for s in SUITE for in RANKS]

"""
#ONE MORE way
mycards=[]
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))
"""

class Deck():

    def __init__(self):
        print("creating ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS] #getting all the crds in the deck i.e is all 52 cards

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:]) #spliting the the cards into half Tuple unpacking

class Hand():

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards)) #number of the crads in hands

    def add(self,added_cards):
        self.cards.extend(added_cards) #adding crads in to hands

    def remove_card(self):
        return self.cards.pop() #removing the cards

class Player():

    def __init__(self,name,hand):  #player has name and hand obhect
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card() #play a card AND REMOVE IT
        print("{} has placed : {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_card(self): #REMOVING THE WAR CARDS
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3): #3 CRADS ARE BEING REMOVED
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return true if player has cards
        """

        return len(self.hand.cards) != 0

print("WELCOME TO WAR")

#CRAETE NEW DECK AND SPLIT IT IN half
d = Deck()

d.shuffle()

half1,half2 = d.split_in_half()

#create both Player
comp  = Player("computer",Hand(half1))

# name = input("what is your name?")
user = Player("sagar",Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("time for a new round")
    print(user.name+" has the count :"+str(len(user.hand.cards)))
    print(comp.name+" has the count :"+str(len(comp.hand.cards)))
    print("play card")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(comp.remove_war_card())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over, number of rounds :",str(total_rounds))

print("a war happend "+str(war_count)+"times")

print("computer cards")
print(str(comp.still_has_cards()))

print("player cards")
print(str(user.still_has_cards()))

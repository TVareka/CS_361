from tkinter import *
import random
from PIL import ImageTk, Image
import time

##PLAN
# Dealer Cards and Player Cards
# Be able to deal the cards
# Display the cards (w/ GUI)
# Sum of Player/Dealers cards
# Compare sums of player/dealer
# If players sum > 21, then bust
# if players sum < 21, option to hit or stay
# if player chooses to stay, compare sum of dealer vs player
# if players sum <= 21 AND > Dealers sum, then player wins
# if players sum < dealers sum, player loses

total_wins = 0
total_losses = 0
SUITS = ['C', 'S', 'H', 'D']
# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
CARDS = []


"""
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)


CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)

"""


class Card:
    def __init__(self, suit, val, image):
        self.suit = suit
        self.val = val
        self.image = image

    # Simple way of showing current card
    def show(self):
        print("{} of {}".format(self.val, self.suit))


    def get_val(self):
        return self.val

    def get_suit(self):
        return self.suit

    def draw(self, pos, frame):
        # self.card = ImageTk.PhotoImage(Image.open("card_back.png"))
        Label(frame, image=self.image).place(x=0 + (80 * pos), y=0)


class Deck:
    def __init__(self):
        self.cards = []
        # self.build_deck()

    # Building deck numbers 1-13 and suits as 'C', 'S', etc.
    def build_deck(self):
        img = Image.open('CARDS.png').convert('RGBA')
        for i in range(0, 4):
            for j in range(1, 14):
                crop = img.crop([(j-1)*73, i*98, j*73, (i+1)*98])
                crop_img = ImageTk.PhotoImage(crop)
                self.cards.append(Card(SUITS[i], j, crop_img))

    # Way to shuffle the deck which will be needed at the start of any game
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    # Way to make sure deck is truly shuffled (not for game use)
    def show_deck(self):
        for i in self.cards:
            i.show()

    # Allows a card to be drawn during game of Blackjack
    def draw_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = "Cards in hand: "

        for i in self.cards:
            s = s + str(i)
        return s

    def add_card(self, card):
        self.cards.append(card)

    def show_hand(self, frame, player):
        pos = 0

        for i in self.cards:
            i.draw(pos, frame)
            pos += 1

        Label(frame, bg='green', font='Helvetica 20 bold', text='Total: ' + str(player.get_value())).place(
            x=700, y=240)

    def get_value(self):
        value = 0
        ace = False

        for i in self.cards:
            value = value + min(i.get_val(), 10)
            if i.get_val() == 1:
                ace = True
        if ace and (value + 10) <= 21:
            value = value + 10
        return value

# Dont need this
    def draw(self, canvas, pos):
        j = 0
        for i in self.cards:
            i.draw(canvas, [(pos[0] + (j * 80)), pos[1]])
            j = j + 1


def hit(frame):
    global deck, hand, dealer, total_losses, total_wins

    card = deck.draw_card()
    hand.add_card(card)

    hand.show_hand(frame, hand)
    Label(frame, bg='green', font='Helvetica 20 bold', text='Total: ' + str(hand.get_value())).place(
        x=700, y=240)
    # if hand.get_value() > 21:
    #    total_losses = (total_losses + 1)


def stay(frame):
    global deck, hand, dealer, total_losses, total_wins

    while dealer.get_value() < 17:
        card = deck.draw_card()
        dealer.add_card(card)
        dealer.show_hand(frame, dealer)
        time.sleep(1)
    #if dealer.get_value() > 21:
    #    total_wins = (total_wins + 1)


def deal():
    global deck, hand, dealer, total_losses, total_wins

    deck = Deck()
    deck.build_deck()
    hand = Hand()
    dealer = Hand()
    deck.shuffle()
    hand.add_card(deck.draw_card())
    hand.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())



deck = Deck()
hand = Hand()
dealer = Hand()

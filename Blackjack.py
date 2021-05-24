from tkinter import *
import random
from PIL import ImageTk, Image
import time

in_game = True
hidden = True
total_wins = 0
total_losses = 0
SUITS = ['C', 'S', 'H', 'D']


# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    global hidden

    def __init__(self, suit, val, image):
        self.suit = suit
        self.val = val
        self.image = image
        self.blank = ImageTk.PhotoImage(Image.open('card_back.png').convert('RGBA'))

    # Simple way of showing current card
    def show(self):
        print("{} of {}".format(self.val, self.suit))

    def get_val(self):
        return self.val

    def get_suit(self):
        return self.suit

    def draw(self, pos, frame, player):
        Label(frame, image=self.image).place(x=0 + (80 * pos), y=0)
        if hidden and player == dealer:
            Label(frame, image=self.blank).place(x=0, y=0)


class Deck:
    def __init__(self):
        self.cards = []

    # Building deck numbers 1-13 and suits as 'C', 'S', etc.
    def build_deck(self):
        img = Image.open('CARDS.png').convert('RGBA')
        for i in range(0, 4):
            for j in range(1, 14):
                crop = img.crop([(j - 1) * 73, i * 98, j * 73, (i + 1) * 98])
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
            i.draw(pos, frame, player)
            pos += 1

        if player == dealer and hidden:
            pass
        else:
            Label(frame, bg='green', font='Perpetua 25 bold', text='Total: ' + str(player.get_value())).place(
                x=500, y=240)

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


def hit(frame, d_frame, button, lang):
    global deck, hand, dealer, total_losses, total_wins, in_game, hidden
    bust_lang = 'Bust! You Lose'

    if not lang:
        bust_lang = 'Fracasso! Você Perdeu'

    if in_game:
        card = deck.draw_card()
        hand.add_card(card)

        hand.show_hand(frame, hand)
        Label(frame, bg='green', font='Perpetua 25 bold', text='Total: ' + str(hand.get_value())).place(
            x=500, y=240)

        if hand.get_value() == 21:
            Label(frame, bg='green', font='Perpetua 25 bold', text='Blackjack!').place(x=750, y=240)
            stay(d_frame, button, lang)
            return

        if hand.get_value() > 21:
            total_losses += 1
            hidden = False
            dealer.show_hand(d_frame, dealer)
            in_game = False
            Label(frame, bg='green', font='Perpetua 25 bold', text=bust_lang).place(x=750, y=240)

        if in_game is False:
            show_button(button)


def stay(frame, button, lang):
    global deck, hand, dealer, total_losses, total_wins, in_game, hidden
    bust_lang = 'Dealer Busts! You Win!'
    lose_lang = 'Dealer Wins! You Lose'
    tie_lang = 'It\'s a tie!'
    win_lang = 'You Win!'

    if not lang:
        bust_lang = 'Busto de Negociante! Você Ganha!'
        lose_lang = 'Revendedor Ganha! Você perdeu'
        tie_lang = 'É um Empate!'
        win_lang = 'Você Ganha!'

    if in_game:
        hidden = False
        dealer.show_hand(frame, dealer)
        frame.master.update()
        in_game = False
        while dealer.get_value() < 17:
            time.sleep(1)
            card = deck.draw_card()
            dealer.add_card(card)
            dealer.show_hand(frame, dealer)
            frame.master.update()

        if dealer.get_value() > 21:
            total_wins += 1
            dealer.show_hand(frame, dealer)
            Label(frame, bg='green', font='Perpetua 25 bold', text=bust_lang).place(x=750, y=240)
        else:
            if dealer.get_value() > hand.get_value():
                Label(frame, bg='green', font='Perpetua 25 bold', text=lose_lang).place(x=750, y=240)
                dealer.show_hand(frame, dealer)
                total_losses += 1
            elif dealer.get_value() == hand.get_value():
                Label(frame, bg='green', font='Perpetua 25 bold', text=tie_lang).place(x=750, y=240)
                dealer.show_hand(frame, dealer)

            else:
                Label(frame, bg='green', font='Perpetua 25 bold', text=win_lang).place(x=750, y=240)
                dealer.show_hand(frame, dealer)
                total_wins += 1

        if in_game is False:
            show_button(button)


def show_button(button):
    button.place(x=525, y=120)


def deal():
    global deck, hand, dealer, total_losses, total_wins, in_game, hidden

    deck = Deck()
    deck.build_deck()
    hidden = True
    in_game = True
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

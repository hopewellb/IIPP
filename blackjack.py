# Baby's First Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
result = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class       
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        self.hand = "Hand is: "
        for i in range(len(self.cards)):
             self.hand += (str(self.cards[i]) + " ")
        return self.hand                     

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        self.value = 0
        self.total_aces = 0
        for card in self.cards:
            if card.get_rank() == 'A':
                self.total_aces += 1
            self.value += VALUES[card.get_rank()]
        if self.value <= 11 and self.total_aces > 0:
            self.value += 10
            return self.value
        else:
            return self.value
               
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            card = self.cards[i]
            card_pos = [pos[0] * i + 60, pos[1]]
            card.draw(canvas, card_pos)
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [96, 198], CARD_BACK_SIZE)
    
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))           

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(-1)
    
    def __str__(self):
        self.deck_content = "Deck contains "
        for i in range(len(self.deck)):
            self.deck_content += (str(self.deck[i]) + " ")
        return self.deck_content

#define event handlers for buttons
def deal():
    global score, outcome, result, in_play, deck, player_hand, dealer_hand
    if in_play:
        score -= 1
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    deck.shuffle()
    outcome = "Hit or stand?"
    result = ""
    for i in range(2):
        player_hand.add_card(deck.deal_card())    
        dealer_hand.add_card(deck.deal_card())         
    in_play = True

def hit():
    global score, result, outcome, player_hand, dealer_hand, deck, in_play
    if in_play == True and player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "New deal?"
            result = "You bust!"
            score -= 1
            in_play = False
    else:
        return       
       
def stand():
    global score,player_hand, dealer_hand, deck, in_play, result, outcome
    if not in_play:
        return
    if player_hand.get_value() > 21:
            in_play = False
            result = "You bust!"
            outcome = "New deal?"
            score -= 1
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
                        
        if dealer_hand.get_value() > 21:
            in_play = False
            outcome = "New deal?"
            result = "Dealer busts. You win!"
            score += 1            
        elif dealer_hand.get_value() >= player_hand.get_value():
            in_play = False
            outcome = "New deal?"
            result = "Dealer wins!"
            score -= 1
        else:
            in_play = False
            outcome = "New deal?"
            result = "You win!"
            score += 1

# draw handler    
def draw(canvas):
    global score, player_hand, dealer_hand, outcome, result
    player_hand.draw(canvas, [100, 400]) 
    dealer_hand.draw(canvas, [100, 150])
    canvas.draw_text('Blackjack', [210, 40], 40, 'Black')
    canvas.draw_text('Dealer', [60, 130], 35, 'Black')
    canvas.draw_text('Player', [60, 380], 35, 'Black')
    canvas.draw_text(outcome, [200, 380], 35, 'Black')
    canvas.draw_text("Score: " + str(score), [445, 100], 35, 'Black')
    if result == "You win!":
        canvas.draw_text(result, [210, 310], 45, 'Blue')
    elif result == "Dealer busts. You win!":
        canvas.draw_text(result, [100, 310], 45, 'Blue')
    else:
        canvas.draw_text(result, [210, 310], 45, 'Red')
       
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 530)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deck = Deck()
deal()
frame.start()

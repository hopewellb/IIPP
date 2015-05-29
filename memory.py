# Baby's first implementation of card game - Memory

import simplegui
import random

# global variables
CARD_WIDTH = 50
CARD_HEIGHT = 100
cards_list1 = range(8)
cards_list2 = range(8) 
card_deck = cards_list1 + cards_list2
flipped_card1 = None
flipped_card2 = None

def new_game():
    """Starts new game and resets global variables."""
    global cards, turns, exposed, state, flipped_card1, flipped_card2
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    exposed = [False] * 16
    flipped_card1 = None
    flipped_card2 = None
    random.shuffle(card_deck)    
     
def mouseclick(pos):
    """Handler for mouse clicks that also controls Memory's logic. 
    The handler will assign clicked cards a position in the card
    index, determine which cards are exposed,
    check if the last 2 cards match, keep track of turns
    and control the flow of the game.
    """
    global turns, CARD_WIDTH, card_deck, exposed, state, flipped_card1, flipped_card2
    click = list(pos)
    card_pos = click[0] // 50    
    if exposed[card_pos]:
        return
    for card_index in range(16):         
        if click[0] > (card_index * CARD_WIDTH) and click[0] < ((card_index * CARD_WIDTH) + CARD_WIDTH):           
            if state == 0:
                exposed[card_index] = True      
                flipped_card1 = card_index   
                print "Flipped card #1 is: " + str(card_deck[card_index])
                state = 1
                print "state 1"
            elif state == 1:
                exposed[card_index] = True
                flipped_card2 = card_index
                print "Flipped card #2 is: " + str(card_deck[card_index]) 
                state = 2
                print "state 2"
                turns += 1
                label.set_text("Turns = " + str(turns))
                print "turn is " + str(turns)
            else:               
                if card_deck[flipped_card1] != card_deck[flipped_card2]:
                    exposed[flipped_card1] = False
                    exposed[flipped_card2] = False
                    exposed[card_index] = True
                    flipped_card1 = card_index
                    state = 1
                else:
                    flipped_card1 = card_index
                    exposed[card_index] = True
                    state = 1
                print "Flipped card #1 is: " + str(card_deck[card_index])
                print "state 1"               
                                       
def draw(canvas):
    """This draw handler will draw numbers and cards on the
    canvas. Cards are 50x100 pixels."""
    global card_deck, CARD_WIDTH, CARD_HEIGHT, exposed, card_pos
    for card_index in range(16):   
        card_pos = [(CARD_WIDTH * card_index), 67] 
        text_pos = [(card_pos[0] + 10), card_pos[1]] 
        point_a = [card_pos[0], 0]
        point_b = [card_pos[0] + CARD_WIDTH, 0]
        point_c = [card_pos[0], 100]
        point_d = [card_pos[0] + CARD_WIDTH , 100]
        if exposed[card_index] == True:
            canvas.draw_text(str(card_deck[card_index]), text_pos, 55, "White")
        elif exposed[card_index] == False:
            canvas.draw_polygon([(point_a), (point_b),
            (point_d), (point_c)], 1, "Yellow", "Green")
                     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

###########
# Imports #
###########

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleplot
import random

##############
# Initialize #
##############

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# global variables
in_play = False
outcome = ""
current = ""
score = 0
dealer = []
player = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

###########
# Classes #
###########

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

    def draw(self, canvas, x, y, faceDown):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [x + CARD_CENTER[0], y + CARD_CENTER[1]], CARD_SIZE)
        if faceDown == True:
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [x + CARD_BACK_CENTER[0], y + CARD_BACK_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return ','.join([card.get_suit()+card.get_rank() for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        sum = 0
        ace = False
        for card in self.hand:
            sum += VALUES.get(card.get_rank())
            if card.get_rank() == 'A':
                ace = True
        if ace and sum <= 10:
            return sum+10
        else:
            return sum

    def hit(self, deck):
        self.add_card(deck.deal_card())

    def busted(self):
        global busted
        sum = self.get_value()
        if sum > 21:
            return True

    def draw(self, canvas, y):
        for card in self.hand:
            card.draw(canvas, 50+80*self.hand.index(card), y, False)


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        self.shuffle()

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


############
# Handlers #
############

#define event handlers for buttons
def deal():
    global outcome, current, in_play, dealer, player, deck, score
    if in_play:
        score -= 1
    deck = Deck()
    dealer = Hand()
    player = Hand()
    outcome = ""
    current = "Hit or Stand?"
    in_play = True
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)

def hit():
    global in_play, outcome, score, current
    if in_play == True:
        player.hit(deck)
        #print "Player has " +str(player)+" with the value of "+str(player.get_value())
    # if the hand is in play, hit the player
        if player.busted():
            outcome = 'You went bust!'
            current = 'New deal?'
            in_play = False
            #print outcome
            score -= 1
        if player.get_value() == 21:
            in_play = False
            outcome = 'You got BLACKJACK!'
            current = 'New deal?'
            #print outcome
            score += 1

def stand():
    global outcome, in_play, score, current
    if in_play == True:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer.get_value() < 17:
            dealer.hit(deck)
            #print "Dealer has " +str(dealer)+" with the value of "+str(dealer.get_value())
            if dealer.busted():
                outcome = "Dealer went bust!"
                #print outcome
                score += 1
        # assign a message to outcome, update in_play and score
        if not dealer.busted() and dealer.get_value() > player.get_value():
            outcome = "Dealer won."
            #print outcome
            score -= 1

        if not dealer.busted() and dealer.get_value() == player.get_value():
            outcome = "It's a tie."
            #print outcome
        if not dealer.busted() and dealer.get_value() < player.get_value():
            outcome = "You won."
            #print outcome
            score += 1
    in_play = False
    current = "New deal?"

# draw handler
def draw(canvas):
    global in_play
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Score: "+str(score), (400, 100), 26, "Black")
    canvas.draw_text("Blackjack", (70,100), 38, "Blue")
    canvas.draw_text("Dealer", (70, 180), 26, "Black")
    canvas.draw_text(outcome, (220, 180), 26, "Black")
    canvas.draw_text("Player", (70, 380), 26, "Black")
    canvas.draw_text(current, (220, 380), 26, "Black")
    dealer.draw(canvas, 200)
    player.draw(canvas, 400)
    card = Card("S", "A")
    if in_play:
        card.draw(canvas, 50, 200, faceDown = True)

######
# UI #
######

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

########
# Main #
########

# deal an initial hand
deal()

# get things rolling
frame.start()

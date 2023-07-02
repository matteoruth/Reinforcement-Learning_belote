import deck

class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.belote = False
        self.rebelote = False
        self.score = 0
        self.take = None
    
    def __str__(self) -> str:
        # a string format as follows: Romain has taken the atout or Romain has not taken the atout
        take_string = "has taken the atout" if self.take else "has not taken the atout"
        return self.name + " " + take_string
    
    def get_name(self):
        return self.name
    
    def get_hand(self):
        return self.hand
    
    def get_score(self):
        return self.score
    
    def get_take(self):
        return self.take
    
    def get_belote(self):
        return self.belote and self.rebelote
    
    def set_take(self, take):
        assert isinstance(take, str) and take in ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.take = take

    def add_score(self, score):
        assert isinstance(score, int)
        self.score += score
        
    def add_card(self, card: deck.card):
        assert isinstance(card, deck.card)
        self.hand.append(card)
        
    def add_cart_list(self, card_list: list):
        assert isinstance(card_list, list)
        self.hand += card_list
        
    def play_card(self, card: deck.card):
        assert isinstance(card, deck.card) and card in self.hand
        self.hand.remove(card)
        return card

    def print_hand(self):
        #   __ __ ___
        #  /7 /8 /9  \
        #  |♠ |♥ |♦  |
        
        # use the card format to print the hand
        # print the hand in a nice format
        for i in range(len(self.hand)):
            print(" __", end = "")
        print("")
        for i in range(len(self.hand)):
            print("/" + str(self.hand[i].get_rank(symbol=True)).ljust(2), end = "")
        print("\\")
        for i in range(len(self.hand)):
            print("|" + self.hand[i].get_suit(symbol=True), end = " ")
        print(" |")
        
player1 = player("Romain")
deck = deck.cardDeck()
deck.shuffle(times=100)

# distribute 3 cards to player1
player1.add_cart_list(deck.distribute(8))
player1.print_hand()
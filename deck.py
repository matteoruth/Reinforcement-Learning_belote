import random

class card():
    def __init__(self, suit , rank, non_atout, atout):
        assert isinstance(suit, str) and isinstance(rank, int) and (rank in range(7, 14) or rank == 1)
        self.suit = suit
        self.rank = rank
        self.non_atout_value = non_atout
        self.atout_value = atout
        self.atout = None
        
    def set_atout(self, atout):
        assert isinstance(atout, str) and atout in ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.atout = True if self.suit == atout else False
        
    def reset_atout(self):
        self.atout = None
        
    def get_atout_value(self):
        return self.atout_value

    def get_non_atout_value(self):
        return self.non_atout_value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def __str__(self) -> str:
        atout_string = "is atout" if self.atout else "is not atout"
        return self.suit + " " + str(self.rank) + " " + atout_string

class cardDeck():
    def __init__(self):
        self.deck = []
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            self.deck.append(card(suit, 7,0,0))
            self.deck.append(card(suit, 8,0,0))
            self.deck.append(card(suit, 9,0,14))
            self.deck.append(card(suit, 10,10,10))
            self.deck.append(card(suit, 11,2,20))
            self.deck.append(card(suit, 12,3,3))
            self.deck.append(card(suit, 13,4,4))
            self.deck.append(card(suit, 1,11,11))
        self.distributed = []
        self.played = []
        
    def __len__(self):
        return len(self.deck)
    
    def shuffle(self, times = 3):
        for i in range(times):
            cut = random.randint(0, len(self) - 1)
            first = self.deck[:cut]
            second = self.deck[cut:]
            self.deck = second + first
        print("Shuffled")
        
    def cut(self, cut=0):
        first = self.deck[:cut]
        second = self.deck[cut:]
        self.deck = second + first
        print("Cut")
        
    def set_atout(self, atout):
        for card in self.deck:
            card.set_atout(atout)
        
        for card in self.played:
            card.set_atout(atout)
        
        for cards in self.distributed:
            cards.set_atout(atout)
            
    def reset_atout(self):
        for card in self.deck:
            card.reset_atout()
            
    def new_game(self, shuffle = True):
        assert len(self.played) == 32
        
        self.deck = self.played
        self.played = []
        self.distributed = []
        self.reset_atout()
    
    
    def printDeck(self):
        for card in self.deck:
            print(str(card))

    def distribute(self, nb_cards):
        cards = []
        for i in range(nb_cards):
            temp = self.deck.pop()
            cards.append(temp)
            self.distributed.append(temp)
        return cards




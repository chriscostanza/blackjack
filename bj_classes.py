import random

class Card():
    
    def __init__(self,suite,name,value):
        self.suite = suite
        self.value = value
        self.name = name
    
    def __str__(self):
        return f"{self.name} of {self.suite}"

class Deck():
    
    def __init__(self,cards=[]):
        self.cards = cards
        
    def replenish_cards(self):
        
        '''
        clears deck and then 
        fills deck up with all 52 cards
        '''
        self.cards = []
        card_suites = ['Spades','Hearts','Clubs','Diamonds']
        card_names = [('Two',2),('Three',3),('Four',4),('Five',5),('Six',6),('Seven',7),('Eight',8),('Nine',9),('Ten',10),('Jack',10),('Queen',10),('King',10),('Ace',11)]
        for suite in card_suites:
            for name,value in card_names:
                cardname = name+suite
                cardname = Card(suite,name,value)
                self.cards.append(cardname)
        
        
    def shuffle(self):
        
        '''
        Shuffles deck list
        '''
        
        random.shuffle(self.cards)
        
    def deal_card(self):
        
        '''
        pops card off of deck list
        meant to be used after shuffle
        '''
        
        return self.cards.pop()


class Player():
    
    def __init__(self,name="",bank=0,hand=[]):
        
        # name expect string, bank expect int, hand is empty list
        self.name = name
        self.bank = bank
        self.hand = hand
        
    def withdraw(self,amount):
        if amount <= self.bank:
            self.bank -= amount
        else:
            print("INSUFFICIENT FUNDS")
        
        
    def deposit(self,amount):
        self.bank += amount
        
    def draw_card(self,card):
        self.hand.append(card)
        
    def hand_value(self):
        
        '''
        takes in player.hand and 
        converts raw cards into value
        '''

        total_value = 0

        for card in self.hand:
            total_value += card.value

        if total_value > 21 and 11 in list(card.value for card in self.hand):
            total_value -= 10

        return total_value
    
    def new_hand(self):
        
        '''
        Empties player hand list
        '''
        self.hand = []
    
    def player_hand_display(self):
        
        '''
        displays cards in player's hand
        '''
    
        # takes in player hand and displays cards
        print(f"---{self.name}'s Hand---")
        for card in self.hand:
            print(card)
            
    def computer_hand_display(self):
        
        '''
        displays one card for computer hand, 
        rest of cards are displayed as 'FACE DOWN CARD'
        '''
        
        print("---Computer's Hand---")
        print(self.hand[0]) 
        for card in self.hand[1:]:
            print("FACE DOWN CARD")



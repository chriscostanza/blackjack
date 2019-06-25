from random import randint
from Classes import Hand
from Classes import Card
from Functions import deal
from Functions import bust_check
from Functions import table
from Functions import table_win


# FUNCTIONS #




# CARDS # 

twospades = Card("Two of Spades",2)
twohearts = Card("Two of Hearts",2)
twodiamonds = Card("Two of Diamonds",2)
twoclubs = Card("Two of Clubs",2)

threespades = Card("Three of Spades",3)
threehearts = Card("Three of Hearts",3)
threediamonds = Card("Three of Diamonds",3)
threeclubs = Card("Three of Clubs",3)

fourspades = Card("Four of Spades",4)
fourhearts = Card("Four of Hearts",4)
fourdiamonds = Card("Four of Diamonds",4)
fourclubs = Card("Four of Clubs",4)

fivespades = Card("Five of Spades",5)
fivehearts = Card("Five of Hearts",5)
fivediamonds = Card("Five of Diamonds",5)
fiveclubs = Card("Five of Clubs",5)

sixspades = Card("Six of Spades",6)
sixhearts = Card("Six of Hearts",6)
sixdiamonds = Card("Six of Diamonds",6)
sixclubs = Card("Six of Clubs",6)

sevenspades = Card("Seven of Spades",7)
sevenhearts = Card("Seven of Hearts",7)
sevendiamonds = Card("Seven of Diamonds",7)
sevenclubs = Card("Seven of Clubs",7)

eightspades = Card("Eight of Spades",8)
eighthearts = Card("Eight of Hearts",8)
eightdiamonds = Card("Eight of Diamonds",8)
eightclubs = Card("Eight of Clubs",8)

ninespades = Card("Nine of Spades",9)
ninehearts = Card("Nine of Hearts",9)
ninediamonds = Card("Nine of Diamonds",9)
nineclubs = Card("Nine of Clubs",9)

tenspades = Card("Ten of Spades",10)
tenhearts = Card("Ten of Hearts",10)
tendiamonds = Card("Ten of Diamonds",10)
tenclubs = Card("Ten of Clubs",10)

jackspades = Card("Jack of Spades",10)
jackhearts = Card("Jack of Hearts",10)
jackdiamonds = Card("Jack of Diamonds",10)
jackclubs = Card("Jack of Clubs",10)

queenspades = Card("Queen of Spades",10)
queenhearts = Card("Queen of Hearts",10)
queendiamonds = Card("Queen of Diamonds",10)
queenclubs = Card("Queen of Clubs",10)

kingspades = Card("King of Spades",10)
kinghearts = Card("King of Hearts",10)
kingdiamonds = Card("King of Diamonds",10)
kingclubs = Card("King of Clubs",10)

acespades = Card("Ace of Spades",11)
acehearts = Card("Ace of Hearts",11)
acediamonds = Card("Ace of Diamonds",11)
aceclubs = Card("Ace of Clubs",11)


# THE GAME #

while True:
    
    # Define new hands / name input / welcome #
    
    print('Welcome to black jack!')
    name = input("Please enter your name!: ")
    player1 = Hand(name,[],0,800)
    dealer = Hand('Dealer',[],0,800)
    pot = Hand('Pot',[],0,0)
    
    # ready prompt #
    
    play = input('Are you ready to play? Y/N: ')
    
    if play[0].upper() == 'Y':
        game_on = True
    else:
        game_on = False
        

    # GAME PLAY # 
    
    while game_on:
        
        # DEFINE THE DECK EVERY START OF GAME, CLEAR HANDS/VALUE #
        
        deck = [twoclubs,twodiamonds,twohearts,twospades,
        threeclubs,threediamonds,threehearts,threespades,
        fourclubs,fourdiamonds,fourhearts,fourspades,
        fivespades,fivehearts,fivediamonds,fiveclubs,
        sixspades,sixhearts,sixdiamonds,sixclubs,
        sevenspades,sevenhearts,sevendiamonds,sevenclubs,
        eightspades,eighthearts,eightdiamonds,eightclubs,
        ninespades,ninehearts,ninediamonds,nineclubs,
        tenspades,tenhearts,tendiamonds,tenclubs,
        jackspades,jackhearts,jackdiamonds,jackclubs,
        queenspades,queenhearts,queendiamonds,queenclubs,
        kingspades,kinghearts,kingdiamonds,kingclubs,
        acespades,acehearts,acediamonds,aceclubs]
        
        player1.value = 0
        player1.cards = []
        dealer.value = 0
        dealer.cards = []
        
        # BETTING PHASE #
        
        print(f'Current Holdings: {player1.money}')
        
        # Bankrupt Check #
        if player1.money == 0:
            game_on = False
            print("You've run out of money! Game Over!!")
            break
        elif dealer.money == 0:
            game_on = False
            print("Dealer is bankrupt! You've Won!!")
            break
        else:
            pass
        # Place bet #
        betting = True
        
        while betting == True:
            try:
                bet = int(input('How much would you like to bet?: '))
                if bet > player1.money:
                    print("You don't have enough money")
                    continue
                elif bet > dealer.money:
                    print(f"Dealer only has ${dealer.money}. Place a lower bet!")
                    continue
                else:
                    player1.transfer(bet,pot)
                    dealer.transfer(bet,pot)
                    deal(player1)
                    deal(player1)
                    deal(dealer)
                    deal(dealer)
                    table()
                    betting = False
                    turn = 'Player 1'
            except:
                print("Please select a valid amount of money!")
                continue
        
        # PLAYER 1 TURN #
        
        while turn == 'Player 1':

            choice = input("Hit or Stand?")
            
            if choice[0].upper() == 'H':
                deal(player1)
                table()
                if bust_check(player1.value,player1.name) == True:
                    table_win()
                    print(f"{player1.name} bust!")
                    pot.payout(dealer)
                    break
                else:
                    continue
            elif choice[0].upper() == 'S':
                turn = "Dealer"
                break
                    
        # DEALER TURN / WIN CHECK #

        while turn == "Dealer":
            
            while dealer.value < 17:
                deal(dealer)
                table()

            else:
                
                if bust_check(dealer.value,dealer.name) == True:
                    table_win()
                    print(f"{dealer.name} bust!")
                    pot.payout(player1)
                    turn = "Player 1"
                    break
                
                elif dealer.value > player1.value:
                    table_win()
                    print("Dealer wins!")
                    pot.payout(dealer)
                    turn = "Player 1"
                    break
                        
                elif dealer.value == player1.value:
                    table_win()
                    print("Draw!")
                    pot.draw_payout(dealer,player1)
                    turn = "Player 1"
                    break                        
                    
                else:
                    table_win()
                    print(f"{player1.name} wins!")
                    pot.payout(player1)
                    turn = "Player 1"
                    break
                    
                    

                
                
            
                
                
            
        
            
        
            

        


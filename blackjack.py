## WELCOME MESSAGE/PLAYER NAME INPUT

print("Welcome to BlackJack!")

#global variables
bankrupt = False
the_deck = Deck()

#player assignment
player1 = Player(player_name_input(),200,[])
computer = Player('Computer',200,[])

# Overall Game loop (continues while both players have money)
while not bankrupt:

    #betting phase (abnkrupt check, take in bet, set current bet, withdraw bet from players banks)
    bankrupt_check(player1,computer)
    current_bet = betting(player1,computer)
    player1.withdraw(current_bet)
    computer.withdraw(current_bet)
    
    # replenish and shuffle deck, clear hands
    the_deck.replenish_cards()
    the_deck.shuffle()
    player1.new_hand()
    computer.new_hand()
    
    #p1 draw
    player1.draw_card(the_deck.deal_card())
    player1.draw_card(the_deck.deal_card())
    
    #computer draw
    computer.draw_card(the_deck.deal_card())
    computer.draw_card(the_deck.deal_card())
    
    
    # Player 1 turn
    #loop for asking to hit or stand breaks on busy
    while not bust_check(player1):
        display_table(player1,computer)
        hit = input('Hit or Stand?: ')
        if hit[0].lower() == 'h':
            player1.draw_card(the_deck.deal_card())
        else:
            break
    
    #if p1 busts this happens else computer phase starts  
    if bust_check(player1) == True:
        computer.deposit(current_bet*2)
        display_table(player1,computer)
        print("BUST!")
        
    else:
        while not bust_check(computer):

        #Computer draw loop

            if computer.hand_value() < player1.hand_value() and computer.hand_value() != 21:
                computer.draw_card(the_deck.deal_card())
                print("I am drawing a card because my hand is less than yours and 21")
            elif computer.hand_value() == player1.hand_value() and computer.hand_value() not in range(18,22):
                computer.draw_card(the_deck.deal_card())
                print("I am drawing a card because our hands are even and it is worth the risk")
            else:
                break

        #different win conditions
        if bust_check(computer) == True:
            display_table_end(player1,computer)
            print(f"{computer.name} busts! {player1.name} wins!")
            player1.deposit(current_bet*2)
        elif computer.hand_value() == player1.hand_value():
            display_table_end(player1,computer)
            print("DRAW!")
            player1.deposit(current_bet)
            computer.deposit(current_bet)
        elif computer.hand_value() > player1.hand_value():
            display_table_end(player1,computer)
            print("Computer wins!")
            computer.deposit(current_bet*2)
        else:
            display_table_end(player1,computer)
            print(f"{player1.name} wins!")
            player1.deposit(current_bet*2)











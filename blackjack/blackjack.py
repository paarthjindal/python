# blackjack rules

# the deck is unlimited in size
# there are no jokers
# jack/queen /king all count as 10
# the ace can count as 1 or 11
# we use following deck [11,2,3,4,5,6,7,8,9,10,10,10,10]
# cards in list have equal probability to being picked
# cards are not removed from deck after they have been drawn

#  https://replit.com/@appbrewery/blackjack-start#main.py

# FUNCTION TO GENERATE A RANDOM NUMBER FROM DECK
import random
def deal_card() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    temp = random.choice(cards)
    return temp

# TAKE A LIST OF CARDS FROM THE USER AND RETURN THE SUM OF THEM
def calculate_sum(user_cards):
    sum = 0
    for i in range(len(user_cards)):
        sum += user_cards[i]
    if sum == 21 and len(user_cards) == 2:
      return 0

    if 11 in user_cards and sum > 21:
        user_cards.remove(11)
        user_cards.append(1)

    return sum

# after the end of the game it will just compare all things and return the result
def compare(user_cards,computer_cards):
    if user_cards == computer_cards:
        return "Draw"
    elif user_cards ==0:
        return "Congrats win ! you have a blackjack "
    elif computer_cards ==0:
        return "Oops you loose! Opponent has  a blackjack "
    elif user_cards > 21:
        return "You are too high! You loose!"
    elif computer_cards > 21:
        return "You win computer gone out of bound!"
    elif user_cards > computer_cards:
        return " you win"
    else:
        return " you lose"
def main():
    is_game_over = False

    user_cards = []
    computer_cards = []
    a = 2
    while a > 0:
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        a = a - 1

    while not is_game_over:

        user_score=calculate_sum(user_cards)
        computer_score=calculate_sum(computer_cards)
        print(f"  Your cards: {user_cards},current_score:{user_score}")
        print(f"  Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            print("Do you want to pick one more card? type 1 for yes or 0 for no")
            a = int(input())
            if a == 0:
                is_game_over = True
            else:
                user_cards.append(deal_card())



     # now its time for computer to play its game

    while (computer_score!=0 and computer_score<17):
         computer_cards.append(deal_card())
         computer_score = calculate_sum(computer_cards)
    print(compare(user_score,computer_score))

    paarth=int(input("Do you want to play a new game type 1 for yes or 0 for no"))
    if paarth == 1:
        main()
    else:
       return

    return

if __name__ == '__main__':
    main()


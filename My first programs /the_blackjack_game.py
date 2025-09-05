import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculating_score(cards):
    if sum(cards) == 22 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer wins!"
    elif user_score == 0:
        return "You have a BlackJack! You win!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > 21:
        return "You went over. Computer wins!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"


users_cards = []
computers_cards = []
computers_score = -1
users_score = -1
is_game_over = False
for _ in range(2):
    users_cards.append(deal_card())
    computers_cards.append(deal_card())
while not is_game_over:
    users_score = calculating_score(users_cards)
    computers_score = calculating_score(computers_cards)
    print(f"Your cards are {users_cards} and your score is {users_score}.")
    print(f"Computer's first card is {computers_cards[0]}")

    if users_score == 0 or computers_score == 0 or users_score > 21:
        is_game_over = True
    else:
        add_card = input("Do ypu want to add a card? Type 'y' if you do, type 'n' if you don't: ").lower()
        if add_card == "y":
            users_cards.append(deal_card())
        else:
            is_game_over = True
while computers_score != 0 and computers_score < 17:
    computers_cards.append(deal_card())
    computers_score = calculating_score(computers_cards)

print(f"So here are your cards: {users_cards} and your final score if: {users_score}!")
print(f"And here are the computer's cards: {computers_cards}, computer's score is: {computers_score}!")
print(compare(users_score, computers_score))










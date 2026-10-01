# بهبود پروژه سنگ، کاغذ و قیچی

import random

print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print("------------------")

player1_wins = 0
player2_wins = 0
winning_score = 4

while player1_wins < winning_score and player2_wins < winning_score:
    randomNumber = random.randint(0, 2)
    computerMove = None

    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    print(f"Player 1: {player1_wins} | Player 2: {player2_wins}")
    Player_1 = input("player_1 , Make your move : ").lower()
    print(f"player_2 , Make your move : {computerMove}")
    Player_2 = computerMove

    if Player_1 == "q" or Player_1 == "quit":
        break

    if Player_1 == Player_2:
        print("thats a tie ...")
    elif Player_1 == "rock":
        if Player_2 == "scissors":
            print("player_1 wins!....")
            player1_wins += 1
        elif Player_2 == "paper":
            print("player_2 wins!...")
            player2_wins += 1
    elif Player_1 == "paper":
        if Player_2 == "rock":
            print("player_1 wins!...")
            player1_wins += 1
        elif Player_2 == "scissors":
            print("player_2 wins!...")
            player2_wins += 1
    elif Player_1 == "scissors":
        if Player_2 == "paper":
            print("player_1 wins!...")
            player1_wins += 1
        elif Player_2 == "rock":
            print("player_2 wins!...")
            player2_wins += 1
    else:
        print("something went wrong ....")

print(f"Final Scores: Player 1: {player1_wins} | Player 2: {player2_wins}")


# --------------------------------------------------------------------------------------------------
# نسخه بهبود یافته توسط هوش مصنوعی:

# import random

# print("Rock...")
# print("Paper...")
# print("Scissors...")
# print("------------------")

# player1_wins = 0
# player2_wins = 0
# winning_score = 4

# moves = ["rock", "paper", "scissors"]

# while player1_wins < winning_score and player2_wins < winning_score:

#     print(f"Player 1: {player1_wins} | Player 2: {player2_wins}")

#     player_1 = input("Player 1, make your move: ").lower()

#     if player_1 == "q" or player_1 == "quit":
#         break

#     if player_1 not in moves:
#         print("Invalid move! Please choose rock, paper, or scissors.")
#         continue

#     player_2 = random.choice(moves)

#     print(f"Player 2, make your move: {player_2}")

#     if player_1 == player_2:
#         print("That's a tie!")

#     elif (
#         (player_1 == "rock" and player_2 == "scissors")
#         or
#         (player_1 == "paper" and player_2 == "rock")
#         or
#         (player_1 == "scissors" and player_2 == "paper")
#     ):
#         print("Player 1 wins!")
#         player1_wins += 1

#     else:
#         print("Player 2 wins!")
#         player2_wins += 1

# print(
#     f"Final Scores: Player 1: {player1_wins} | "
#     f"Player 2: {player2_wins}"
# )

import random

print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print("------------------")

randomNumber = random.randint(0, 2)
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"


Player_1 = input("player_1 , Make your move : ").lower()
print(f"player_2 , Make your move : {computerMove}")
Player_2 = computerMove

if Player_1 == Player_2:
    print("thats a tie ...")
elif Player_1 == "rock":
    if Player_2 == "scissors":
        print("player_1 wins!....")
    elif Player_2 == "paper":
        print("player_2 wins!...")
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("player_1 wins!...")
    elif Player_2 == "scissors":
        print("player_2 wins!...")
elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("player_1 wins!...")
    elif Player_2 == "rock":
        print("player_2 wins!...")
else:
    print("something went wrong ....")


# --------------------------------------------------------------------------------------------------
# توضیحات:

# پیاده سازی مثال، به روش ایف های تودرتو یا نستدایف است
# random: یک ماژول یا کتابخانه پایتونی هست که میتونیم داخل پروژه خودمون ایمپورت کرده و ازش استفاده کنیم
# randint(): یکی از فانکشن های کتابخانه که برای ما بین دو عددی که بهش میدیم، یکی رو بصورت رندم انتخاب میکند
# .lower(): یک فانکشن که میاد تمامی حروف را بصورت حروف کوچک تبدیل میکند و در اختیار ما قرار میدهد

# --------------------------------------------------------------------------------------------------
# پیاده سازی به روش دیگر

# if Player_1 == "rock" and Player_2 == "scissors":
#     print("player_1 wins!....")
# elif Player_1 == "rock" and Player_2 == "paper":
#     print("player_2 wins!...")
# elif Player_1 == "paper" and Player_2 == "rock":
#     print("player_1 wins!...")
# elif Player_1 == "paper" and Player_2 == "scissors":
#     print("player_2 wins!...")
# elif Player_1 == "scissors" and Player_2 == "paper":
#     print("player_1 wins!...")
# elif Player_1 == "scissors" and Player_2 == "rock":
#     print("player_2 wins!...")
# elif Player_1 == Player_2:
#     print("thats a tie ...")
# else:
#     print("something went wrong ....")

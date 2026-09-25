# دستورات شرطی

# --------------------------------------------------------------------------------------------------
# مثال:

userRank = 2

if userRank == 1:
    print("you got GOLD medal")
    print("you are the best!")
elif userRank == 2:
    print("you got SILVER medal")
elif userRank == 3:
    print("you got BRONZE medal")
else:
    print("you got no medal")

# --------------------------------------------------------------------------------------------------
# دستورات شرطی تک خطی:

print("you got GOLD medal") if userRank == 1 else print("no medal")

# عملگر های منطقی

# --------------------------------------------------------------------------------------------------
# and: باید همه شرط های بین آن ترو باشد تا گزاره ترو شود در غیر این صورت فالس میشود

print(f"True and True: {True and True}")  # True and True: True
print(f"True and False: {True and False}")  # True and False: False
print(f"False and True: {False and True}")  # False and True: False
print(f"False and False: {False and False}")  # False and False: False

userAge = 19
userGender = "male"

if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")


# --------------------------------------------------------------------------------------------------
# or: اگر یکی از شرط ها هم درست باشد، ترو برگردانده میشود

print(f"True or True: {True or True}")  # True or True: True
print(f"True or False: {True or False}")  # True or False: True
print(f"False or True: {False or True}")  # False or True: True
print(f"False or False: {False or False}")  # False or False: False

weather = "sunnny"

if weather == "sunnny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")


# --------------------------------------------------------------------------------------------------
# not: دستور را برعکس میکند یعنی اگر عبارتی فالس باشد، ترو میکند و بالعکس

print(f"not True: {not True}")  # not True: False
print(f"not False: {not False}")  # not False: True

isBorotherComing = False

if not isBorotherComing:
    print("my sister said: i wont come")


# --------------------------------------------------------------------------------------------------
# Example: هر فرد باتوجه به سنی که دارد باید مبلغ خاصی رو پرداخت کند

# 2 < age < 8 => 2 dollars
# age >= 65 => 5 dollars
# rest => 10 dollars

age = 50

# روش اول:
if (age >= 0 and age <= 2) or (age >= 8 and age < 65):
    print("you should pay 10 dollars")


# روش دوم:
if not ((age > 2 and age < 8) or age >= 65):
    print("you should pay 10 dollars")

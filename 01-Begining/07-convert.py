# Convert : عملیات تبدیل انواع داده ها به یکدیگر

# --------------------------------------------------------------------------------------------------
# convert in interpolation:
# :در عبارت زیر، در اینترپولیشن بصورت درونی هسته ی پایتون میاد خودش عبارت داخل آکولات رو تبدیل به استرینگ میکند
print(f"multiply of 2 and 6 is: {2 * 6}")  # multiply of 2 and 6 is: 12

# --------------------------------------------------------------------------------------------------
# تبدیل عدد صحیح به عدد اعشاری:

myWeight = 80
print(type(myWeight))  # <class 'int'>
print(myWeight)  # 80

# تبدیل خود متغییر به نوع اعشار:
myWeight = float(myWeight)
print(type(myWeight))  # <class 'float'>
print(myWeight)  # 80.0

# ریختن تبدیل شده متغییر عدد صحیح داخل یک متغییر جدید
# myWeightFloat = float(myWeight)
# print(type(myWeightFloat))  # <class 'float'>

# --------------------------------------------------------------------------------------------------
# تبدیل عدد اعشاری به عدد صحیح:

myNumber = 14.612
print(type(myNumber))  # <class 'float'>
print(myNumber)  # 14.612

# myNumber = int(myNumber)
# print(type(myNumber)) # <class 'int'>
# print(myNumber) # 14

# اگر خواستیم اعشار را به سمت بالا گرد کند کافیست عبارت را بعلاوه یک کنیم:
myNumber = int(myNumber) + 1
print(myNumber)  # 15


# --------------------------------------------------------------------------------------------------
# تبدیل عدد به رشته:

myHeight = 170
myHeight = str(myHeight)
print(type(myHeight))  # <class 'str'>
print(myHeight)  # 170


# --------------------------------------------------------------------------------------------------
# تبدیل رشته به عدد:

# تبدیل یک رشته ای که داخلش عدد نیست منجربه ارور میشود:

# testNumber = "MyTestNumber"
# testNumber = int(testNumber) # ValueError: invalid literal for int() with base 10: 'MyTestNumber'

# ولی در مثال زیر چون عدد داخل رشته هست به درستی تبدیل میشود:
testNumber2 = "2026"
print(type(testNumber2))  # <class 'str'>
testNumber2 = int(testNumber2)
print(type(testNumber2))  # <class 'int'>

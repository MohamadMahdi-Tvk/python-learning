# String Interpolation => Formatting Strings

# مربوط به فرمت دهی نوع داده ای رشته میباشد

firstName = "Sara"
lastName = "Moradi"
result = "Username is " + firstName + " and UserFamily is " + lastName

print(result)  # Username is Sara and UserFamily is Moradi

# f => Formatting: روش بهتر کد بالایی
# {} => داخل آکولات ما به متغییر های خود نیاز داریم؛ حتی با زدن کنترل و اسپیس میتونیم در کادر باز شده آن را پیدا کنیم
result2 = f"Username is {firstName} and UserFamily is {lastName}"
print(result2)  # Username is Sara and UserFamily is Moradi


# مثال عددی:
number1 = 3
number2 = 5
print(f"Sum is: {number1 + number2}")  # Sum is: 8

# --------------------------------------------------------------------------------------------------
# String Indexes:

# نوع داده ای رشته ای، میاد تک به تک کارکتر هایش را ایندکس گذاری میکند
# هرکدام از کارکتر ها یا حرف ها، دارای یک شناسه یا عدد هستند که از صفر شروع میشوند و به آن ایندکس میگویند
# با استفاده از اعداد ایندکس میتونیم به حروف دسترسی داشته باشیم

print(firstName)  # چاپ کل رشته
print(firstName[2])  # r => چاپ حرف سوم رشته

# اگر ایندکسی را خارج از بازه رشته قرار بدیم، چه اتفاقی میفتد؟
print(firstName[4])  # IndexError: string index out of range

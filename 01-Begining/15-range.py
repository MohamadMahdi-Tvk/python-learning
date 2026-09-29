# range(start, stop, step) => to create a list of numbers

# تعریف یک رنج یا بازه عددی
myNumbers = range(1, 10)


# اگر به همین صورت خروجی رو چاپ کنیم برای ما همان رنج رو میاورد
print(myNumbers)  # range(1, 10)


# برای اینکه اعداد درون رنج را مشاهده کنیم میتونیم متغییری ایجاد کرده و مقدارش رو لیستی از رنج درنظر بگیریم:
result = list(myNumbers)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# میتونیم در یک خط عملیات مربوط به چاپ یک بازه را انجام دهیم:
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# اگر بخواهیم بازه عددی تعریف کنیم که از صفر شروع میشود، نیازی نیست صفر را بنویسیم:
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# step: تعیین گام بازه عددی

print(list(range(1, 20, 2)))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# تعریف بازه عددی بصورت نزولی:
print(list(range(10, 1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]


# Example 1:

# for num in range(1, 10):
#     print("*" * num)


# Example 2:

for num in range(1, 10):
    if num % 2 == 1:
        for star in range(1, 6):  # [1, 2, 3, 4, 5]
            print("*" * star)
    else:
        for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
            print("*" * star)

# filter(functionorNone, iterable)

# برای فیلتر کردن آیتم ها برای یک ایتربیل استفاده می شود

numbers = [1, 2, 3, 4, 5, 6]

# فقط اعدادی که زوج هستند رو واکشی کن:
evens = filter(lambda num: num % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6]

# --------------------------------------------------------------------------------------------------
# مثال: لیستی از افراد داریم که میخوایم سبد خرید آن ها را چک کنیم، که اگر خالی بود آنها را فیلتر کنیم
users = [
    {'name': 'mohamamd', 'shop_cart': []},
    {'name': 'sara', 'shop_cart': ['kotlin', 'vue']},
    {'name': 'iman', 'shop_cart': []},
]

# حالا میخوایم اون سبد خرید هایی که خالی هستند را حذف کنیم:
result = filter(lambda user: len(user['shop_cart']) == 0, users)
print(list(result)) # [{'name': 'mohamamd', 'shop_cart': []}, {'name': 'iman', 'shop_cart': []}]

# یادآوری در مورد تروسینس و فالسینس: لیست یا رشته خالی نمایانگر فالسینس هستند
# پس در لامبدای خود نیازی نیست از لن استفاده کنیم:
result_1 = filter(lambda user: user['shop_cart'], users)
# اما این عبارتی که قرار دادیم در خروجی آن را میاورد که سبد خرید او دارای آیتم هست:
print(list(result_1)) # [{'name': 'sara', 'shop_cart': ['kotlin', 'vue']}]

# برای اینکه مشکل برطرف شود، یک نات قبل از دستور قرار میدهیم تا آنهایی که سبد خرید خالی دارند را بیاورد
result_2 = filter(lambda user: not user['shop_cart'], users)
print(list(result_2)) # [{'name': 'mohamamd', 'shop_cart': []}, {'name': 'iman', 'shop_cart': []}] 

# ترکیب استفاده از مپ و فیلتر در کنار همدیگر:
# در مثال بالا، تمام آبجکت ها بصورت کامل برگردانده شده است، اما مثلا ما لیستی از اسم ها را فقط میخوایم داشته باشیم:
result_3 = map(lambda user: user['name'], 
               filter(lambda user: not user['shop_cart'], users))
print(list(result_3)) # ['mohamamd', 'iman']

# با استفاده از لیست کامپرهنشن هم میتوانیم همچین چیزی ایجاد کنیم:
result_4 = [user['name'] for user in users if len(user['shop_cart']) == 0]
print(result_4) # ['mohamamd', 'iman']
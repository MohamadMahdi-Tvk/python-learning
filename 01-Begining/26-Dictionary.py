# Dictionary

# بطور معمول، در لیست ها از عناصر یکسان استفاده می کنیم، یعنی لیستی از اعداد اگر داریم، نمیایم داخلش رشته هم قرار بدهیم
# اما یک ساختار دیگری داریم تحت عنوان دیکشنری، که میاد یک کلید اصلی می گیرد و یک مقدار:

# dictionary = {
#     key: value
# }

# بطور مثال:
my_dictionary = {
    "name": "Item 1",
    "count": 3,
    "price": 2500
}
print(my_dictionary)  # {'name': 'Item 1', 'count': 3, 'price': 2500}

# میتوانیم لیستی از دیکشنری ها ایجاد کنیم:
my_shopping = [
    {"name": "Python", "price": "free"},
    {"name": "Kotlin", "price": 2500},
]
print(my_shopping)
# [{'name': 'Python', 'price': 'free'}, {'name': 'Kotlin', 'price': 2500}]

# روش دیگر برای ایجاد یک دیکشنری؛ ورودی کلید اصلی و مقدار میگیرد
my_dictionary_2 = dict(name="new dictionary", age=30)
print(my_dictionary_2)  # {'name': 'new dictionary', 'age': 30}

# --------------------------------------------------------------------------------------------------
# نحوه دسترسی به آیتم های درونی دیکشنری ها:

# شناسه مقادیر ما همان کلید اصلی دیکشنری است، بنابراین می توان با کلید اصلی به مقدار دسترسی داشت:

my_info = {
    "first_name": "mohamadmahdi",
    "last_name": "Tavakoli",
    "age": 30
}
print(my_info["first_name"])  # mohamadmahdi
print(my_info["last_name"])  # Tavakoli
print(my_info["age"])  # 30

# اگر کلیدی رو قرار بدهیم که در دیکشنری ما وجود ندارد، ارور میدهد؛ مثلا:
# print(my_dictionary_3["city"]) # KeyError: 'city'

# برای بدست آوردن تمامی آیتم های یک دیکشنری، روش بهتر استفاده از حلقه فور است
# keys(): این متد برای دیکشنری ها است، که یک لیستی از کلید های اصلی آن دیکشنری را ایجاد می کند
# values(): یک لیستی از مقادیری که داخل دیکشنری وجود دارد را ایجاد می کند؛ این متد بطور پیش فرض در زبان پایتون برای دیکشنری ها ایجاد شده است

print(my_info.keys())  # dict_keys(['first_name', 'last_name', 'age'])
print(my_info.values())  # dict_values(['mohamadmahdi', 'Tavakoli', 30])

# چاپ کلید های اصلی
for key in my_info.keys():
    print(key)

# چاپ مقادیر
for value in my_info.values():
    print(value)

# چاپ مقادیر با استفاده از کلید های اصلی
for key in my_info.keys():
    print(my_info[key])

# items: با استفاده از این متد، کلید اصلی و مقدار را در قالب توپل، با هم میاورد
for item in my_info.items():
    print(item)
# خروجی:
# ('first_name', 'mohamadmahdi')
# ('last_name', 'Tavakoli')
# ('age', 30)

# چاپ کلید و مقدار با همدیگر:
for key, value in my_info.items():
    print(key, value)
# خروجی:
# first_name mohamadmahdi
# last_name Tavakoli
# age 30

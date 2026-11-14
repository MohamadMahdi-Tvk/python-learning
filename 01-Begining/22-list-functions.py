# List Functions - part 3

my_courses = ["Python", "Kotlin", "Ionic", "Python", "JQuery", "Vuejs", "Python"]
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# index(value, start, stop): برای اینکه شماره ایندکس یک آیتم رو بدست بیاوریم
# value: مقداری که در لیست است
# start: نقطه شروع جستجو در لیست
# stop: نقطه پایان جستجو در لیست

index_kotlin = my_courses.index("Kotlin")

# index_python = my_courses.index("python")

index_python_with_start = my_courses.index("Python", 1)

index_python_with_start_stop = my_courses.index("Python", 1, 5)

print(index_kotlin)  # 1

# print(index_python)
# ValueError: list.index(x): x not in list
# به این دلیل که پایتون را با پی کوچک نوشته ایم و فانکشن به حروف کوچک و بزرگ حساس است

# 3 => در لیست، از کاتلین به بعد شروع به جستجو میکند
print(index_python_with_start)

print(index_python_with_start_stop)  # 3

# --------------------------------------------------------------------------------------------------
# count(): بدست آوردن آن آیتمی که درون لیست تکرار شده

number_of_python = my_courses.count("Python")
number_of_django = my_courses.count("Django")

print(number_of_python) # 3
print(number_of_django) # 0

# --------------------------------------------------------------------------------------------------
# reverse(): وارونه کردن لیست، کپی ایجاد نمیکند، بلکه همان لیست را وارونه می کند

print(my_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_numbers.reverse() # اینجا وارنه اش کردیم، و روی خود لیست تغییر ایجاد می کند و آن را آپدیت می کند
print(my_numbers) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# --------------------------------------------------------------------------------------------------
# sort(): مرتب کردن آیتم های درون لیست، همان لیست را آپدیت می کند

unordered_numbers = [5, 9, 6, 3, 18, 75, 1]
print(unordered_numbers) # [5, 9, 6, 3, 18, 75, 1]
unordered_numbers.sort() # اینجا روی همان لیست، عملیات مرتب سازی را انجام دادیم
print(unordered_numbers) # [1, 3, 5, 6, 9, 18, 75]

# اگر آیتم های لیست رشته باشند، براساس حروف الفبا مرتب می کند:
my_courses.sort()
print(my_courses) # ['Ionic', 'JQuery', 'Kotlin', 'Python', 'Python', 'Python', 'Vuejs']

# --------------------------------------------------------------------------------------------------
# join(): متصل کردن آیتم های لیست بوسیله جداکننده ای که بهش میدیم و خروجی رشته
# خروجی بصورت یک رشته به همراه جداکننده ای هست که برای جداسازی آیتم ها برایش درنظر گرفته ایم
# لزوما این فانکشن برای آرایه یا لیست نیست؛ یعنی همراه با لیست استفاده میشود اما برای لیست نیست

second_courses = " - ".join(my_courses)
print(second_courses) # Ionic - JQuery - Kotlin - Python - Python - Python - Vuejs

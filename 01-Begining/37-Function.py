# Function - part 5

# *args :
# برای اینکه تعداد پارامتر های ورودی یک فانکشن داینامیک باشد، و بتوانیم بی نهایت ورودی دریافت کنیم
# طبق قاعده، باید در ورودی یک ستاره قرار داده و یک اسم دلخواه برایش درنظر بگیریم، ولی معمولا به عنوان آرگز میشناسند
def sum_all_numbers(*args):
    print(args)

sum_all_numbers(4, 6, 8, 5)  # (4, 6, 8, 5)

# می بینیم که یک توپل برای ما بر میگرداند، بنابراین می تونیم با حلقه فور به تک تک المان های آن دسترسی داشته باشیم:
def sum_all_numbers_2(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_numbers_2(4))  # 4
print(sum_all_numbers_2(1, 5, 6, 9))  # 21

# میتوان پارامتر های دیگری هم در ورودی برای فانکشن درنظر گرفت:
def sum_all_numbers_3(name, *args):
    print(name)
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_numbers_3('first', 1, 2, 3, 4, 5))
print(sum_all_numbers_3('second', 2, 3, 4, 5, 6))
print(sum_all_numbers_3('third', 3, 4, 5, 6, 7))

# --------------------------------------------------------------------------------------------------
# **kwargs:
# اگر خواسته باشیم ورودی های فانکشن ما بصورت دیکشنری دریافت شوند از دابل استار استفاده میکنیم؛ بنابراین
# میاد بصورت دیکشنری، کلید اصلی و مقدار را دریافت می کند
# kwargs => keyword arguments

def show_user_info(**kwargs):
    print(kwargs)

show_user_info(name="mohamadmahdi", family="tavakoli", age=30)
# {'name': 'mohamadmahdi', 'family': 'tavakoli', 'age': 30}

show_user_info(name="alireza", family="karimi", age=6, email="alireza@gmail.com")
# {'name': 'alireza', 'family': 'karimi', 'age': 6, 'email': 'alireza@gmail.com'}

# دسترسی به آیتم های درون دیکشنری با حلقه فور:
def show_user_info_2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_user_info_2(name="mohamadmahdi", family="tavakoli", age=30)

# در سینگل استار میتوانیم لیستی از پارامتر ها را دریافت کنیم
# اما دابل استار کلید اصلی و مقدارش رو در یک دیکشنری قرار میدهد و میتوانیم از آن استفاده کنیم

# --------------------------------------------------------------------------------------------------
# ما 4 مورد زیر را بررسی کردیم:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs
# اگر بخواهیم در فانکشنی از همه ی این 4 مورد استفاده کنیم، باید به همین ترتیبی که قرار داده ایم استفاده کنیم؛ مثلا:

def display_inf(a, b, *args, def_param="default", **kwargs):
    return [a, b, args, def_param, kwargs]

print(display_inf(1, 2, 6, first_name="mohammad", last_name="ordookhani"))
# [1, 2, (6,), 'default', {'first_name': 'mohammad', 'last_name': 'ordookhani'}]

# --------------------------------------------------------------------------------------------------
# فانکشن زیر را درنظر بگیرید:
def sum_all_numbers_4(*args):
    print(args) # (1, 2, 3, 4, 5, 6)
    total = 0
    for num in args:
        total += num
    return total

# یک لیستی هم داریم:
numbers = [1, 2, 3, 4, 5, 6]

# حالا میخواهیم این لیست رو بدیم به فانکشنمون تا آن ها را جمع کند:
# sum_all_numbers_4(numbers) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# میبینیم که وقتی خود لیست رو در ورودی به فانکشن ارسال می کنیم ارور می دهد؛ چون عملیات += روی یک لیست
# اتفاق افتاده است؛ برای رفع این مشکل باید بیایم و آیتم های درون لیست را آنپک کنیم و آن ها را بکشیم بیرون
# کافیه برای این کار قبل از لیست، یک ستاره قرار دهیم:
print(sum_all_numbers_4(*numbers)) # 21

# پس در حالت عادی اگر لیست را پاس بدیم یک توپل ایجاد میکند که درونش یک لیست دارد، پس خروجی آن به این شکل در میاد:
# ([1, 2, 3, 4, 5, 6],)
# اما وقتی ستاره را قرار می دهیم، یک توپل درست می کند و آیتم ها را بصورت کامل جدا می کند، یعنی اینجوری:
# (1, 2, 3, 4, 5, 6)

# --------------------------------------------------------------------------------------------------
# فانکشن زیر را درنظر بگیرید:
def display_names(name, family):
    print(f"name is: {name} and family is: {family}")

# یک دیکشنری هم داریم:
person = {"name": "Ali", "family": "Moradi"}

# اگر خواسته باشیم این دیکشنری را به فانکشن پاس بدیم، باید کلید های اصلی را واکشی کنیم 
# پس برای این کار از دابل استار باید استفاده کنیم:
display_names(**person) # name is: Ali and family is: Moradi

# پس بطور کلی، اگر از سینگل استار استفاده کنیم، میره و آیتم ها را بیرون می کشد
# ولی اگر از دابل استار استفاده کنیم، میره کلید های اصلی موجود در یک دیکشنری را واکشی میکند و مقادیر آنها را ارسال میکند
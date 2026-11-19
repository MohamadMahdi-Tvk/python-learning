# Function - part 1

# مهم ترین کاری که فانکشن انجام می دهد، جلوگیری از تکرار کد ها هست؛ بطور کلی، فانکشن ها ساختاری هستند
# که یک بار کدنویسی می شوند، و تنها با صدا زدن نام آنها در جاهای مختلف می توان از آنها استفاده کرد

# تعریف کلی یک فانکشن :
# def name_of_function():
#     command

# def : define (تعریف کردن)

# مثال: تعریف یک فانکشن که یک متن رو در خروجی پرینت می کند:
def say_hello():
    print("Hello, Python!")


# فقط تعریف فانکشن کافی نیست، بلکه با استفاده از نام آن، باید در جایی از کدمان که میخواهیم، فراخوانی شود:
say_hello()  # Hello, Python!


# فانکشن می تواند شامل مجموعه ای از دستورات هم باشد:
def my_function():
    print("This is First Command!")
    print("This is Second Command!")


# فراخوانی فانکشن:
my_function()
# This is First Command!
# This is Second Command!

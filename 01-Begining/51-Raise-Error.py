# Raise Error

# خودمان میتوانیم ارور های شخصی ایجاد یا ریز کنیم، مثلا ایندکس ارور ایجاد میکنیم:
# raise IndexError => IndexError

# میتوانیم متن ارور هم برای آن قرار بدیم:
# raise IndexError("you have entered invalid value!") => IndexError: you have entered invalid value!

# برای هر نوع اروری میتوانیم این کار را انجام دهیم:
# raise ValueError("Invalid Value!") => ValueError: Invalid Value!

# مثال: یک فانکشنی داریم، که دو تا رشته دریافت میکند، و اگر کاربر رشته وارد نکرد، ارور دریافت می کند
# همینطور یک توپلی هم از رنگ ها داریم که اگر رنگی که کاربر وارد کرد داخل آن نبود، یک نوع دیگری از ارور را برگرداند:
def colorize(text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"Printed {text} in {color}")

colorize("Hello, World", "blue") # Printed Hello, World in blue
colorize(30, "blue") # TypeError: text must be a string
colorize("Hello, World", "yellow") # ValueError: yellow is not in colors


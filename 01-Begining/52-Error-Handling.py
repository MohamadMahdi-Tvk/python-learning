# Error Handling

# برای مدیریت خطاهای برنامه از ترای اکسپت استفاده می کنیم

# try:
#     print(my_name)
# except:
#     print("an error occured!")

# مثال: مدیریت خطا برای استفاده از کلید اصلی که دیکشنری وجود ندارد
# داخل این فانکشنی که نوشتیم، ارور عدم وجود کلید را مدیریت میکنیم
def get(d, key):
    try:
        return d[key]
    except:
        # return None => میتونیم نان برگردانیم
        return "no key found"


person = {
    'name': 'mohammad',
    'family': 'tavakoli'
}
print(get(person, 'name'))
print(get(person, 'family'))
print(get(person, 'age'))  # no key found

# میتوان برای ارور های مختلف اکسپت های مختلفی قرار بدهیم:


def get_2(d, key):
    try:
        return d[key]
    except KeyError:  # اگر خطای کی ارور رخ داد، دستورات زیر را ریترن کند
        return "no key found"
    except IndexError:  # اگر ایندکس ارور رخ داد، دستورات زیر را ریترن کند
        return "index error"

# --------------------------------------------------------------------------------------------------
# مثال: گرفتن عدد از کاربر، که اگر عدد وارد نشد، ارور بدهد


# در این مثال، کاربر مقداری را وارد میکند، بلاک ترای آن را به اینت تبدیل میکند، اگر نتواند این کار را کند
# یعنی کاربر یک رشته وارد کرده، پس وارد بلاک اکسپت می شود:
try:
    num = int(input("please enter a number: "))
except:
    print("thats not a number!")
else:
    print("this is else section")
finally:
    print("this is finally section")

# کار دستور الس و فاینالی بعد از بلاک اکسپت چیه؟
# دستور ترای اول اجرا میشود، چک میکند که دستور بدون مشکل اجرا میشه، یعنی مقداری که وارد شده به اینت
# تبدیل می شود و مشکلی ندارد؛ اگر مشکلی داشت میره سراغ بلاک اکسپت، و دستورات داخل
# اکسپت اجرا می شود؛ اما اگر هیچ اروری وجود نداشته باشد و دستور ترای با موفقیت انجام بشه، دستور الس اجرا میشود
# اما دستور فاینالی، برایش مهم نیست خطایی رخ داده یا خیر، در هرصورت این فاینالی اجرا می شود

# همین مثال را میتوانیم با حلقه وایل تکمیل ترش کنیم، یعنی تا زمانی که عدد وارد نشده در حلقه بماند:
while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("thats not a number, please enter another one!")
    else:
        print("you have entered a number")
        break
    finally:
        print("this is finally section")

# --------------------------------------------------------------------------------------------------
# مثال: فانکشنی برای تقسیم داریم، که باید خطاهایی که کاربر هنگام ورود اعداد تولید میکند را مدیریت کنیم
# یعنی وقتی رشته وارد کرد یا وقتی که عددی بر 0 تقسیم کرد، ارور دریافت کند:


def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:  # این اکسپت برای زمانی که کاربر می خواست عددی را بر 0 تقسیم کند
        return "Dont Divide By Zero Please!"
    except TypeError:  # این اکسپت برای زمانی که کاربر بجای عدد، یک رشته وارد کرد:
        return "first and second must be numbers!"


print(divide(1, 0))  # Dont Divide By Zero Please!
print(divide(1, "Hello"))  # first and second must be numbers!

# as:
# اگر بخواهیم در خروجی، اروری که خود سیستم برای ما برمیگرداند را ببینیم باید از از استفاده کنیم
# برای اکسپت تایپ ارور انجام میدهیم و کلمه ی ارور بعد از از، میتواند هرچیزی باشد و به عنوان متغییر درنظر گرفته میشود:
def divide_2(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "Dont Divide By Zero Please!"
    except TypeError as error:
        print(error)
        return "first and second must be numbers!"

print(divide_2(1, "Hello"))
# unsupported operand type(s) for /: 'int' and 'str'
# first and second must be numbers!
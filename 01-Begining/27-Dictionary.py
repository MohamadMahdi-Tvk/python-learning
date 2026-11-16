# Dictionary - part 2

my_info = {
    "name": "mohamadmahdi",
    "family": "tavakoli",
    "age": 30,
    "email": "mohamadmahditavakoli8@gmail.com"
}

# برای اینکه چک کنیم آیا کلید اصلی ای در دیکشنری موجود هست یا خیر، میتوان از ساختار زیر استفاده کرد:

is_exists = "email" in my_info
print(is_exists)  # True

# حالا میتوان ادامه فرآیند رو کدنویسی کرد، یعنی اگر وجود داشت، بیا و فلان عملیات را انجام بده:
if "email" in my_info:
    print(my_info["email"])
else:
    print("there is no email key in my_info dictionary!")


# چک کردن مقدار یک دیکشنری: باید بگیم برو داخل ولیو ها دنبالش بگرد، نه داخل کلید های اصلی
is_name_exists = "mohamadmahdi" in my_info.values()
print(is_name_exists)  # True

# --------------------------------------------------------------------------------------------------
# clear(): حذف کل آیتم های درون دیکشنری

my_information = {
    "name": "mohamadmahdi",
    "family": "tavakoli",
    "age": 30,
    "email": "mohamadmahditavakoli8@gmail.com"
}
print(my_information)
# {'name': 'mohamadmahdi', 'family': 'tavakoli', 'age': 30, 'email': 'mohamadmahditavakoli8@gmail.com'}

my_information.clear()

print(my_information)  # {}

# --------------------------------------------------------------------------------------------------
# copy(): گرفتن یک کپی از دیکشنری

my_information_2 = {
    "name": "mohamadmahdi",
    "family": "tavakoli",
    "age": 30,
    "email": "mohamadmahditavakoli8@gmail.com"
}

print(my_information_2)
# {'name': 'mohamadmahdi', 'family': 'tavakoli', 'age': 30, 'email': 'mohamadmahditavakoli8@gmail.com'}

info_copy = my_information_2.copy()

print(info_copy)
# {'name': 'mohamadmahdi', 'family': 'tavakoli', 'age': 30, 'email': 'mohamadmahditavakoli8@gmail.com'}

# اما واقعا این دو یکی هستند؟
print(my_information_2 == info_copy)  # True | بله مقادیرشان یکی هست
print(my_information_2 is info_copy) # False | اما رفرنس آن ها یکی نیستند و به یک خانه از حافظه اشاره نمی کنند

# --------------------------------------------------------------------------------------------------
# fromkeys(): میتوان یک دیکشنری جدید به همراه مقدار پیش فرض ایجاد کنیم
# We use fromkeys for generate default value

new_user = {}.fromkeys("name", "unknown")
# {'n': 'unknown', 'a': 'unknown', 'm': 'unknown', 'e': 'unknown'}
print(new_user)
# در اینجا اومده دونه دونه کارکتر های درون رشته در ورودی اول را جدا کرده و مقادیر هر کدام را آنون کرده
# چون استرینگ، لیستی از کارکتر ها هست، اومد و کارکتر ها را جدا کرد و به ازای هرکدام کلید ساخت

# حالا نام را داخل یک لیست قرار میدهیم:
new_user_2 = {}.fromkeys(["name"], "unknown")
print(new_user_2)  # {'name': 'unknown'}

# و حالا کامل ترش میکنیم و فامیلی هم به کلید ها اضافه می کنیم:
new_user_3 = {}.fromkeys(["name", "family"], "unknown")
print(new_user_3)  # {'name': 'unknown', 'family': 'unknown'}

# مجبور نیستیم از این روش استفاده کنیم؛ ولی فرضا اگر تعداد کلید های اصلی ما زیاد باشد،
# جالب نیست همان ابتدا مثلا 15 بار کلمه آنان رو قرار بدهیم، و راحت از این روش استفاده می کنیم و فقط یک بار آن را مینویسیم

# نکته: بجای آکولات میتوانیم از کلمه کلیدی دیکت هم استفاده کنیم، یعنی:
new_user_4 = dict.fromkeys(["name", "family"], "unknown")
print(new_user_4)  # {'name': 'unknown', 'family': 'unknown'}

# --------------------------------------------------------------------------------------------------
# get(key): کلید اصلی رو به ورودی پاس میدهیم و مقدار را به ما برمیگرداند

my_dict = {
    "name": "mohamadmahdi",
    "family": "tavakoli",
    "age": 30,
    "email": "mohamadmahditavakoli8@gmail.com"
}

print(my_dict.get("name")) # mohamadmahdi

# برخلاف روش قبلی بدست آوردن مقدار، در این روش اگر آن کلید وجود نداشت
# اروری نمی دهد و نان برمیگرداند؛ پس اپلیکیشن ما دچار مشکل نمیشود
print(my_dict.get("phone")) # None

# با همین نان، میتوان چک کرد که اگر کلید وجود داشت عملیاتی را انجام دهد:
is_phone_exist = my_dict.get("phone")
print(is_phone_exist) # None
print(is_phone_exist is None) # True

# Dictionary - part 3

my_info = {
    "name": "mohamad",
    "family": "tavakoli",
    "email": "mohamadmahditavakoli8@gmail.com"
}
print(my_info) # {'name': 'mohamad', 'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com'}

# pop: این متد، کلید اصلی را دریافت می کند و کلید اصلی و مقدار را باهم حذف می کند

my_info.pop("name")
print(my_info) # {'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com'}

# اگر کلیدی رو بدیم که وجود نداشته باشد، کی ارور میدهد:
# my_info.pop("age") # KeyError: 'age'

# متد پاپ، هنگام حذف آن آیتم، مقدار حذف شده را برای ما بر میگرداند و میتوانیم از آن در یک متغییر دیگری استفاده کنیم:
result = my_info.pop("email")
print(result) # mohamadmahditavakoli8@gmail.com

# --------------------------------------------------------------------------------------------------
# popitem: این متد از آخر دیکشنری مقدار را حذف میکند

my_info_2 = {
    "name": "mohamad",
    "family": "tavakoli",
    "email": "mohamadmahditavakoli8@gmail.com"
}
print(my_info_2) # {'name': 'mohamad', 'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com'}

my_info_2.popitem()
print(my_info_2) # {'name': 'mohamad', 'family': 'tavakoli'}

# نکته: در نسخه های قدیمی تر پایتون، این متد، بصورت رندوم یک آیتم را پاک می کند

# --------------------------------------------------------------------------------------------------
# update: به روز کردن یک دیکشنری توسط دیکشنری دیگر
# آن آیتم هایی که در دیکشنری نیستند، اضافه می شوند، و آنهایی هم که هستند، با مقدار جدید به روز رسانی می شوند

my_info_3 = {
    "name": "mohamadmahdi",
    "family": "tavakoli",
    "email": "mohamadmahditavakoli8@gmail.com"
}

second = {
    "age": 30,
    "name": "mohamad"
}
print(second) # {'age': 30, 'name': 'mohamad'}
second.update(my_info_3)
print(second) 
# {'age': 30, 'name': 'mohamadmahdi', 'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com'}

# می توانیم فقط یک کلید رو هم ویرایش کنیم:
second["name"] = "mahdi"
print(second) 
# {'age': 30, 'name': 'mahdi', 'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com'}

# کلید و مقدار جدیدی رو هم میتوان به این صورت به دیکشنری اضافه کرد:
second["city"] = "Tehran"
print(second) 
# {'age': 30, 'name': 'mahdi', 'family': 'tavakoli', 'email': 'mohamadmahditavakoli8@gmail.com', 'city': 'Tehran'}
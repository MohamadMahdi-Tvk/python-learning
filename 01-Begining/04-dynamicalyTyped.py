# انواع دیتاتایپ در پایتون:

# Integer: عدد صحیح
productPrice = 100000

# float: عدد اعشاری
productRating = 4.6

# String: رشته یا متن
productName = "Python Course"

# Boolean: درست یا غلط
isRecording = False

# list: لیستی از انواع داده ها را کنار هم قرار میدهد
productTag = ['python', 'python course', 'free python course', 2400, True, 12.4]

# Dictionary: دیکشنری، تعریف بصورت کلید اصلی و مقدار
product = {
    "priductName" : "Python Course",
    "productPrice" : 100000
}

# None Type: برای نوع دیتاتایپی که هیچ چیز داخلش نباشد و مقدار داخلش هیچی یا پوچ است
# برای این متغییر از این نوع تعریف میکنیم که قابل دسترس باشد و بعدا بتوانیم دوباره فراخوانی اش کنیم
myType = None # None Means EMPTY
print(myType) # None
print(type(myType)) # <class 'NoneType'>

# --------------------------------------------------------------------------------------------------
# Dynamic Type Language:

# زبان پایتون از نوع داینامیک تایپ هست؛ یعنی اینکه میتوان مقدار یک متغییری رو بعد از 
# مقداردهی هم عوض کنیم، اما جدای از آن میتوان حتی تایپ یک متغییری رو بعد از تعریف هم تغییر دهیم
# پس وقتی میگیم زبان برنامه نویسی از نوع داینامیک تایپ هست، یعنی متغییر در لحظه میتواند تغییر حالت دهد

myAge = 23
print(type(myAge)) # <class 'int'>

myAge = 50.4
print(type(myAge)) # <class 'float'>


myAge = "MohamadMahdi"
print(type(myAge)) # <class 'str'>


myAge = {
    "test" : 45
}
print(type(myAge)) # <class 'dict'>


# --------------------------------------------------------------------------------------------------
# Static Type Language:

# زبان های برنامه نویسی هستند که استاتیک تایپ هستند، مثل سی پلاس پلاس، سی شارپ
# در این نوع زبان های برنامه نویسی، حتما باید نوع متغییر رو تعریف کنیم و سپس مقداردهی کنیم و در خطوط بعد نمیتوانیم تغییرش دهیم
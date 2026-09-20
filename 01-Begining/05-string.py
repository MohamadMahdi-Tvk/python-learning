# String:

# --------------------------------------------------------------------------------------------------
# "" or '' => برای مقداردهی نوع رشته فرقی ندارد از کدام استفاده میکنیم

myName = "MohamadMahdi"
myFamily = 'Tavakoli'
myAge = 30

# --------------------------------------------------------------------------------------------------
# استفاده از نقل قول داخل متن:

# داخل دابل کوتیشن باید از سینگل کوتیشن استفاده کنیم، و داخل سینگل کوتیشن باید از دابل کوتیشن استفاده کنیم

sentence1 = "Mohamad Said: 'I am programmer'."
sentence2 = 'Mohamad Said: "I Love Python".'
print(sentence1)  # Mohamad Said: 'I am programmer'.
print(sentence2)  # Mohamad Said: "I Love Python".

# --------------------------------------------------------------------------------------------------
# String Escape Characters:

# اگر بخواهیم از یکسری کارکتر های خاص مثل کوتیشن داخل یک متنی استفاده کنیم، میتونیم از / قبل آن استفاده کنیم

# Python Escape Sequences Document Link:
# https://www.quackit.com/python/reference/python_3_escape_sequences.cfm

# \' \' :
# با این روش میتونیم داخل یک رشته که کل آن داخل تک کوتیشن هست، از تک کوتیشن استفاده کنیم
sentence3 = 'Mohamad Said: \'I Love Programming\''

# \n : برای رفتن به خط بعدی استفاده میشود
sentence4 = "This is my text and \n this is new line."

# \\ : اگر خواستیم از \ خالی استفاده کنیم، بهتر است از دوتا \\ استفاده کنیم
sentence5 = "This is Text \\ and this is new Text"


# --------------------------------------------------------------------------------------------------
# String Concatenation: برای چسباندن دو یا چند رشته به همدیگر

# using + :
print(myName + " " + myFamily)  # MohamadMahdi Tavakoli

# رشته با عدد نمیتوانند جمع شوند و خطا میدهد:
# result = myName + myAge
# print(result) # TypeError: can only concatenate str (not "int") to str

# دلیل خطا: متغییر مای ایج یک عدد هست و علامت اپراتور + برای عدد توقع دارد که مقدار بعدی هم
# یک عدد باشد، به همین دلیل وقتی رشته بعدش قرار میگیرد با ارور مواجه میشیم

# کد زیر باز هم ارور میدهد:
# print("My age is: " + myAge) # TypeError: can only concatenate str (not "int") to str


# افزودن رشته ای به رشته ی دیگر به روش اول:
courseName = "Python"
courseName = courseName + " Course"
print(courseName)  # Python Course

# افزودن رشته ای به رشته ی دیگر به روش دوم که کوتاه تر هست:
# += : مقدار سمت راست خودش را با مقدار متغییر سمت چپ جمع میکند و داخل خود متغییر میریزد، دقیقا مثل روش اول
courseName2 = "Python"
courseName2 += " Course"
print(courseName2)  # Python Course

# مثال با مقدار عددی:
number = 4
print(number)  # 4
number += 20
number -= 10
number *= 4
number /= 2
print(number)  # 28.0

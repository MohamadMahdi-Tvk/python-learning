# List Slicing:
# برای گرفتن یک کپی از آیتم های درون لیست استفاده می شود

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# یک کپی از ایندکس اول بگیر و بریز درون متغییر سلکتدنامبر:
selected_number = my_numbers[1]
print(selected_number)  # 2

# حالا میخوایم از چند تا از آیتم های درون لیست کپی بگیریم
# یکی از روش ها، اینه که یک حلقه ایجاد کنیم و بگیم از ایندکس های خاصی آیتم ها رو دونه دونه به آن متغییر اضافه کند
# اما روش ساده تری هم برای این کار وجود دارد؛ استفاده از اسلایسینگ؛ که یک فانکشن نیست، بلکه یک سبک کدنویسی هست
# سینتکس کلی به این صورت است:
# some_list[start:end:step]

# از ایندکس 2 به بعد، همه آیتم ها را بیاور
selected_numbers_from_list_1 = my_numbers[2:]

# از ایندکس 1 شروع کن تا ایندکس 7 برو با قدم 1
selected_numbers_from_list_2 = my_numbers[1:7:1]

print(selected_numbers_from_list_1)  # [3, 4, 5, 6, 7, 8, 9]
print(selected_numbers_from_list_2)  # [2, 3, 4, 5, 6, 7]


# نحوه قرارگیری بعد یا قبل از : مهم است، یعنی مثلا تا 4 را بخواهیم بیاورد
selected_numbers_from_list_3 = my_numbers[:4]
print(selected_numbers_from_list_3) # [1, 2, 3, 4]

# اگر عدد منفی بدهیم، از آخر آیتم میاورد
selected_numbers_from_list_4 = my_numbers[-5:]
print(selected_numbers_from_list_4)  # [5, 6, 7, 8, 9]

# تعیین گام برای آیتم ها - در ایجا میگیم دوتادوتا بالا برو
selected_numbers_from_list_5 = my_numbers[:9:2]
print(selected_numbers_from_list_5) # [1, 3, 5, 7, 9]

# اگر تعداد آیتم ها را نمیدانستیم ولی با گامی که میخواهیم آیتم را بیاورد، یعنی کل آیتم ها با گام 2
selected_numbers_from_list_6 = my_numbers[::2]
print(selected_numbers_from_list_6) # [1, 3, 5, 7, 9]


# اگر بخوایم از کل لیست کپی بگیریم:
# copy_of_numbers = my_numbers[0:] # میتوان 0 را قرار داد
copy_of_numbers = my_numbers[:] # عدد 0 را قرار ندهیم هم از کل آیتم ها کپی میگیرد
print(copy_of_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# پس در کپی کردن، دو تا آبجکت یا لیست ها، با همدیگر متفاوت هستند، یعنی به یک خانه از حافظه اشاره نمی کنند
print(my_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(copy_of_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_numbers == copy_of_numbers) # True مقادیرشان را چک میکند که ترو یعنی مقادیرشان برابر هستند

# در اینجا دو تا لیست با آیتم های دقیقا یکسان هستند؛ اما آیا باهمدیگر برابر هستند؟
print(my_numbers is copy_of_numbers) # False 

# --------------------------------------------------------------------------------------------------
# انجام عملیات ریورس با اسلایسینگ:

colors = ["red", "green", "blue", "yellow", "orange"]

# گام را منفی یک قرار میدهیم تا در کپی شدن از انتهای لیست با گام منفی یک اعداد لیست شوند
copy_of_colors = colors[::-1]  

# از این فانکشن هم استفاده می کنیم تا در نتایج خطوط بعدی مشاهده کنیم، که خروجی هر دو، چه با اسلایسینگ چه با فانکشن ریورس، یکسان هستند
colors.reverse()

print(colors) # ['orange', 'yellow', 'blue', 'green', 'red']
print(copy_of_colors) # ['orange', 'yellow', 'blue', 'green', 'red']

# --------------------------------------------------------------------------------------------------
# خود رشته ها هم نوعی شبیه لیست هستند، مثلا خود رشته از چندین کارکتر کنار همدیگر تشکیل شده اند
# یعنی ما لیستی از کارکتر ها را داریم که یک رشته را تشکیل می دهند

my_name = "mohammadmahdi"

print(my_name[:8]) # mohammad
print(my_name[::-1]) # idhamdammahom
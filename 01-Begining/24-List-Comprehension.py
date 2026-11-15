# List Comprehension:

# اگر بخواهیم اعداد یک لیستی رو دو برابر کنیم و داخل لیست دیگری قرار دهیم، میتوانیم از این روش استفاده کنیم:

my_numbers = [1, 2, 3, 4, 5]

# doubled_numbers = []
# for num in my_numbers:
#     doubled_numbers.append(num * 2)

print(my_numbers)  # [1, 2, 3, 4, 5]
# print(doubled_numbers)  # [2, 4, 6, 8, 10]

# اما پایتون، یک سینتکس خیلی خاصی رو برای انجام دادن اعمالی روی لیست ها پیاده سازی کرده است
# که به آن لیست کامپرهنشن می گویند؛ مثلا در مثال بالا، ما میتوانیم سینتکس حلقه فور را داشته باشیم
# سینتکس آن به این صورت است که دستوری که میخواهیم انجام شود را قبل از فور قرار میدهیم:

doubled_numbers = [num * 2 for num in my_numbers]

print(doubled_numbers)  # [2, 4, 6, 8, 10]


# یک مثال دیگر: چاپ تک تک کارکتر های یک رشته

my_name = "MohamadMahdi"
names_characters = [char for char in my_name]
print(names_characters)
# ['M', 'o', 'h', 'a', 'm', 'a', 'd', 'M', 'a', 'h', 'd', 'i']

# در این مثال کر، نماینده تک تک کارکتر های رشته ما هست، ما میتوانیم عملیات هر عملیاتی را روی آن قرار دهیم
# مثلا در دستورات زیر، اومدیم تک به تک کارکتر های نام را به حروف بزرگ تغییر دادیم:
names_characters_to_upper = [char.upper() for char in my_name]
print(names_characters_to_upper)
# ['M', 'O', 'H', 'A', 'M', 'A', 'D', 'M', 'A', 'H', 'D', 'I']


# مثال: میتوانیم عملیات منطقی هم در آن استفاده کنیم، مثل استفاده از دستورات ایف و الس
# در این مثال میخواهیم اعداد لیست را براساس زوج یا فرد بودن آن جدا کنیم

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [num for num in list_number if num % 2 == 0]

odd = [num for num in list_number if num % 2 != 0]

print(even)  # [2, 4, 6, 8]
print(odd)  # [1, 3, 5, 7, 9]


# مثال بعدی: در اینجا چون از الس استفاده میکنیم، جای فور با ایف عوض میشود

new_list = [num * 2 if num % 2 == 0 else num * 3 for num in list_number]

print(new_list)  # [3, 4, 9, 8, 15, 12, 21, 16, 27]

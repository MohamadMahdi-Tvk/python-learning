# Sorted

# sort: مرتب کردن یک لیست
numbers = [1, 5, 8, 2, 4, 3]
print(numbers)  # [1, 5, 8, 2, 4, 3]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5, 8]

# اما فانکشن سورت، خود لیست را تغییر می دهد؛ ما فانکشن سورتد هم داریم که
# هیچ تاثیری روی خود ایتربیل ندارد:
numbers_2 = [1, 5, 8, 2, 4, 3]
result = sorted(numbers_2)
print(result)  # [1, 2, 3, 4, 5, 8]
print(numbers_2)  # [1, 5, 8, 2, 4, 3] => خود لیست ما هیچ تغییری نکرده است

# reverse => تعیین جهت مرتب شدن لیست؛ یعنی بصورت نزولی
numbers_3 = [1, 5, 8, 2, 4, 3]
result = sorted(numbers_3, reverse=True)
print(result)  # [8, 5, 4, 3, 2, 1]

# --------------------------------------------------------------------------------------------------
# اگر یک لیستی از دیکشنری ها را داشته باشیم، و بخواهیم که براساس نام هر کاربر مرتب شوند، باید از لامبدا استفاده کنیم

users = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 32},
    {'name': 'taha', 'family': 'karimi', 'age': 41},
    {'name': 'sara', 'family': 'mohammadi', 'age': 38},
    {'name': 'ali', 'family': 'saeedi', 'age': 27},
]
print(sorted(users, key=lambda user: user['name']))
# [{'name': 'ali', 'family': 'saeedi', 'age': 33}, {'name': 'mohammad', 'family': 'ordookhani', 'age': 23}, {'name': 'sara', 'family': 'mohammadi', 'age': 28}, {'name': 'taha', 'family': 'karimi', 'age': 21}]

# اگر مستقیم بگیم لیست یوزرز رو سورت کن، متوجه نمی شود چجوری باید این مرتب سازی را انجام دهد
# باید برایش تعیین کنیم براساس کدام کلید اصلی میخوایم سورت کنیم؛ پس باید از لامبدا استفاده کنیم

# سورت براساس سن کاربران بصورت نزولی:
print(sorted(users, key=lambda user: user['age'], reverse=True))
# [{'name': 'taha', 'family': 'karimi', 'age': 41}, {'name': 'sara', 'family': 'mohammadi', 'age': 38}, {'name': 'mohammad', 'family': 'ordookhani', 'age': 32}, {'name': 'ali', 'family': 'saeedi', 'age': 27}]

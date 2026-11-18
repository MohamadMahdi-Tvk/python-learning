# Dictionary Comprehension

# در لیست ها به این شکل داشتیم:
list_numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in list_numbers]
print(doubled_numbers)  # [2, 4, 6, 8, 10]

numbers = dict(first=1, second=2, third=3)
print(numbers)  # {'first': 1, 'second': 2, 'third': 3}

# اما در دیکشنری ها به این صورت داریم:
dictionary_comprehension = {key: value for key, value in numbers.items()}
print(dictionary_comprehension)  # {'first': 1, 'second': 2, 'third': 3}

# پیمایش روی تک تک آیتم های دیکشنری و به توان 2 رساندن آن ها:
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}


# --------------------------------------------------------------------------------------------------
# نیازی نیست حتما یک دیکشنری اولیه داشته باشیم و سپس دیکشنری دومی را ایجاد کنیم:
# یک راست میتوان یک دیکشنری جدید ایجاد کنیم:

simple_numbers = {num: num for num in [1, 2, 3, 4, 5]}
print(simple_numbers)  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

doubled_numbers_2 = {num: num * 2 for num in [1, 2, 3, 4, 5]}
print(doubled_numbers_2)  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# میخواهیم اگر عدد فرد بود، بجای نام،، آد بنویسد و اگر زوج بود، ایون بنویسد
# چون از گزاره شرطی استفاده می کنیم، ساختار کدنویسی تغییر می کند و گزاره شرطی باید داخل پرانتز باشد:
even_or_odd = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}
print(even_or_odd) # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
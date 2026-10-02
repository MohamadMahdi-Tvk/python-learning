# List - Functions

myCourses = ["Python", "Django", "MySql"]

print(myCourses)  # ['Python', 'Django', 'MySql']

# --------------------------------------------------------------------------------------------------
# append: افزودن فقط یک آیتم به انتهای لیست

myCourses.append("Html")

print(myCourses)  # ['Python', 'Django', 'MySql', 'Html']

# --------------------------------------------------------------------------------------------------
# extend: افزودن لیست دیگری از آیتم ها به لیست اصلی خودمان

myCourses.extend(["JQuery", "Unity"])

print(myCourses)  # ['Python', 'Django', 'MySql', 'Html', 'JQuery', 'Unity']

# --------------------------------------------------------------------------------------------------
# insert: افزودن یک آیتم در جای مشخصی از لیست
# در ورودی اول شماره ایندکسی که میخواهیم آیتم جدید در اونجا باشد رو میدهیم و ورودی دوم هم مقدار خود آیتم جدید:

myCourses.insert(4, "Css")

print(myCourses)  # ['Python', 'Django', 'MySql', 'Html', 'Css', 'JQuery', 'Unity']

# اختصاص ایندکس منفی در ورودی اول:
myCourses.insert(-1, "JavaScript") # ['Python', 'Django', 'MySql', 'Html', 'Css', 'JQuery', 'JavaScript', 'Unity']

print(myCourses)
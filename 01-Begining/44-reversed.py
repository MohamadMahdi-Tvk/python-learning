# reversed

# reverse => خود لیست را وارونه می کند
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)  # [1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers)  # [6, 5, 4, 3, 2, 1]

# اما اگر از ریورسد استفاده کنیم:
numbers_2 = [1, 2, 3, 4, 5, 6]
print(reversed(numbers_2))  # <list_reverseiterator object at 0x000001E8AD4F50C0>
# اما میتونیم به لیست تبدیلش کنیم:
print(list(reversed(numbers_2)))  # [6, 5, 4, 3, 2, 1]

# یک رشته هم میتونیم براش ارسال کنیم:
print(list(reversed("hello")))  # ['o', 'l', 'l', 'e', 'h']

# اگر بخوایم یک رشته بصورت رشته برعکس شده برگردد، میتوانیم از اسلایسینگ استفاده کنیم:
print("hello"[::-1]) # olleh

# همین عمل را با ریورسد هم میتوان انجام داد:
name_result = ''
print(name_result.join(list(reversed("hello")))) # olleh

# یک مثال دیگر: چاپ اعداد از 9 تا 0 با حلقه فور
for num in reversed(range(0, 10)):
    print(num)
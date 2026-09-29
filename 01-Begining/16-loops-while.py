# while

# این حلقه، تا زمانی که یک گزاره شرطی درست باشد، دستور را اجرا میکند؛ یعنی دستور زیر تا ابد تکرار میشود:
# while True:
#     print("Hello, While...")

# Example 1:
# مثلا زمانی که بخواهیم از کاربر یک پسوردی بگیریم و تا زمانی که کاربر پسورد اشتباه رو وارد کند باید درخواست رمز عبور را تکرار کنیم

password = input("what is your password: ")
while password != "1234":
    print("your password is wrong!")
    password = input("what is your password: ")

print("your password is correct!")


# Example 2:
# چاپ اعداد یک تا ده

num = 1
while num < 11:
    print(num)
    num += 1


# Example 3:
# چاپ ایموجی خنده:

number = 1
while number < 11:
    print("\U0001f600" * number)
    number += 1


# break: برای شکستن حلقه از این کلمه کلیدی استفاده میکنیم
# در مثال زیر وقتی مای نامبر به پنج برسد حلقه متوقف میشود:
my_number = 1
while my_number <= 10:
    print(my_number)
    my_number += 1

    if my_number == 5:
        break

print("this is over!")

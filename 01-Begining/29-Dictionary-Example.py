# Dictionary Example

# در این مثال، دوره های مختلف برنامه نویسی رو در قالب دیکشنری پیاده سازی می کنیم
# به این صورت که هر دوره یکسری مشخصاتی دارند که به راحتی با دیکشنری ها میتوان پیاده سازی کرد:

course = {
    "title": "Python Course",
    "teacher": "Mohammad Ordookhani",
    "time": 8.5,
    "videoCount": 30,
    "tags": ["python", "online course", "free python course"],
    "shortLink": "toplearn.com/c/o2V3",
    "sessions": [
        {
            "title": "session-1",
            "time": 5
        },
        {
            "title": "session-2",
            "time": 7
        },
        {
            "title": "session-3",
            "time": 9
        },
    ],
    "relatedCourses": [
        {
            "title": "Java Course",
            "teacher": "Mohammad Ghari",
            "time": 20,
            "videoCount": 42,
            "tags": ["java", "online course", "free java course"],
            "shortLink": "toplearn.com/c/82m",
        },
        {
            "title": "CSharp Course",
            "teacher": "Iman Madaeny",
            "time": 10,
            "videoCount": 22,
            "tags": ["csharp", "online course", "free csharp course"],
            "shortLink": "toplearn.com/c/mZO",
        },
    ]
}

# خروجی گرفت از کل دیکشنری:
print(course)

# خروجی گرفتن از دوره های مرتبط:
print(course["relatedCourses"])

# استفاده از حلقه فور برای دوره های مرتبط:
for related in course["relatedCourses"]:
    print(related)

# داخل تر میرویم و عنوان دوره ی مرتبط رو بیرون می کشیم:
for related in course["relatedCourses"]:
    print(related["title"])

# محاسبه مجموع مقادیر در هر سشن:
total_time = 0
for session in course["sessions"]:
    total_time += session["time"]

print(total_time)  # 21

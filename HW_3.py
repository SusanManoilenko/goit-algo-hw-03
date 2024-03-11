from datetime import datetime, timedelta

# Заданий список користувачів з іменами та рядками з датами народження
users = [
    {"name": "Taylor Swift", "birthday": "1989.12.13"},
    {"name": "Dwayne Johnson", "birthday": "1972.05.02"},
    {"name": "Angelina Jolie", "birthday": "1975.03.16"}
]

def process_users(users):
    # Створюємо порожній список для збереження підготовлених користувачів
    prepared_users = []

    # Цикл для обробки кожного користувача
    for user in users:
        try:
            # Перетворюємо рядок з датою народження у об'єкт типу date
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

            # Додаємо підготовленого користувача у новий список
            prepared_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            # Обробляємо виняток, якщо формат дати некоректний
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return prepared_users

def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()

    # Якщо день народження вже минув 
    if days_ahead <= 0:
        days_ahead += 7 
    return d + timedelta(days=days_ahead)

# Функція отримання користувачів, яких потрібно привітати протягом наступних 'days' днів
def get_upcoming_birthdays(prepared_users, days=7):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)

            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

# Обробка користувачів та отримання списку підготовлених користувачів
prepared_users = process_users(users)

# Отримання списку користувачів, яких потрібно привітати протягом наступних 7 днів
upcoming_birthdays = get_upcoming_birthdays(prepared_users, days=7)
print("Список привітань цього тижня:", upcoming_birthdays)

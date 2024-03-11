from datetime import datetime

#Оголошуємо функцію
def get_days_from_today(date):
    try:
        # Перетворення рядка дати у формат 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')

        # Отримання поточної дати, використовуючи datetime.today()
        current_date = datetime.today()

        # Розрахунок різниці між поточною датою та заданою датою
        date_difference = input_date - current_date

        # Повернення різниці у днях як ціле число
        return (f"Кількість днів між {input_date.strftime('%Y-%m-%d')} та поточную датою: {date_difference.days + 1} ")

    except ValueError:
        # Повернення помилки, якщо користувач ввів неправильні вхідні дані
        return "Помилка: неправильні вхідні дані"

# Запитуємо у користувача ввести дату 
input_date = input("Введіть будь-яку дату в форматі 'РРРР-ММ-ДД':")
 
# Визиваємо функціі і виводимо результат у консоль 
print(get_days_from_today(input_date))

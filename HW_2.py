import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевіряємо, чи введені параметри знаходяться в допустимих межах
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []  # Якщо параметри не є допустимими, повертаємо порожній список

    numbers_set = set()  # Створюємо порожню множину для зберігання унікальних випадкових чисел
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))  # Додаємо випадкове число до множини

    return sorted(list(numbers_set))  # Повертаємо відсортований список унікальних випадкових чисел

# Приклад використання:
print(get_numbers_ticket(1, 49, 6))  # Створюємо список з 6 унікальних випадкових чисел в діапазоні від 1 до 49

import math
squares = [x ** 2 for x in range(1, 11)]
print(f"1. {squares}")
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_dict = {day: i+1 for i, day in enumerate(days)}
print(f"2. {days_dict}")
libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_set = {lib.lower() for lib in libraries}
print(f"3. {tags_set}")
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"4. {even_numbers}")
factorials_dict = {n: math.factorial(n) for n in range(1, 6)}
print(f"5. {factorials_dict}")
year = 2024
print(f"year = {year}")
print("Результат:")
if (year % 4 == 0 or year% 400 == 0) and year % 100 != 0:
    print("Високосный год")
else:
    print("Обычный год")

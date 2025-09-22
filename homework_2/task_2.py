b=123321
str_number = f'{b:0>6}'
digits = list(map(int, str_number))
print(f"number: {str_number}")
print("Результат:")
if sum(digits[:3])==sum(digits[3:]):
    print("Счастливый билет")
else:
    print("Несчастливый билет")

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys)!=len(girls):
    print("Результат: Внимание, кто-то может остаться без пары!")
else:
    boys_sort=sorted(boys)
    girls_sort=sorted(girls)
    print("Результат:")
    for i in range(len(boys_sort)):
        print(f" {boys_sort[i]} и {girls_sort[i]} ")

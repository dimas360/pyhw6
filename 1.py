"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-да
Вывод:
Парам пам-пам
"""
# Идеальное решение: 

# lowskill
lol = lambda sss: sum(1 for i in sss if i in 'аеёиоуыэюя')
string = input().lower().split(" ")
print('Парам пам-пам' if all([lol(i) == lol(string[0]) for i in string]) else 'Пам парам')

# hardskill
string = input().lower().split(" ")
print("Парам пам-пам" if len(set(map(lambda ss : sum(1 for i in ss if i in 'аеёиоуыэюя'), string))) == 1 else "Пам парам")

# ЧТО ТУТ ПРОИСХОДИТ !?!?!?!?
print("Парам пам-пам" if len(set(map(lambda s : sum(1 for i in s if i in 'аеёиоуыэюя'), input().lower().split(" ")))) == 1 else "Пам парам")

# Стандартное решение:

# 1 вариант
string = input().lower().split(" ")
lam = lambda strr: sum(1 for i in strr if i in 'аеёиоуыэюя')
tmp = lam(string[0])
print('Парам пам-пам' if all([lam(i) == tmp for i in string]) else 'Пам парам')

# 2 вариант
lamm = lambda strin: sum(1 for i in strin if i in 'аеёиоуыэюя')
string = input().lower().split(" ")
print('Парам пам-пам' if len(set(list(map(lamm, string)))) == 1 else 'Пам парам')
        
# Представление в виде цикла:
klassnie_glasnie = ['а', 'e', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
string = input().lower().split(" ")
result = list()
for i in string:
    count = 0
    for j in i:
        if j in klassnie_glasnie:
            count += 1
    result.append(count)
if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
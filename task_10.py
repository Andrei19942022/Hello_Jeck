# 10.	С помощью цикла while просите пользователя решить пример, пока он не введет правильный ответ.

# Так же у пользователя есть заданное количество попыток. Если он их использовал, то вывести об этом сообщение

equation = "3 + 4 - 7"
answer = 0
attempts = 3
print(f"solve the equation: {equation}")
answer_us = int(input())
while answer_us != answer and attempts > 0:
    attempts -= 1
    if attempts > 0:
        print("Решение не верное")
        answer_us = int(input("Введите ещё раз"))
    else:
        print("У вас закончились попытки")

if attempts > 0:
    print("Решение верное")

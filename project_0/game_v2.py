"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
# воспользуемся алгоритмом бинарного поиска
    count = 0
# обнулим счетчик количества угадываний
    lower_bound = 1
# нижняя граница интервала для угадывания
    upper_bound = 101
# верхняя граница интервала для угадывания
# создали цикл с условием выхода сравнение нижней и верхней границы интервала
    while lower_bound <= upper_bound:
        predict_number = (lower_bound + upper_bound) // 2
# находим средину интервала путем целочисленного деления на 2
        count += 1
# увеличиваем на 1 количество попыток угадывания предполагаемое число
        if number == predict_number:
            break
# выход из цикла, если угадали
# сравниваем искомое число с серединой интервала
        elif number < predict_number:
            upper_bound = predict_number - 1
# если искомое число меньше середины интервала, устанавливаем
# верхнюю границу интервала равной середине интервала уменьшенное на 1
        else:
            lower_bound = predict_number + 1
# если искомое число больше середины интервала, устанавливаем
# нижнюю границу интервала равной середине интервала увеличенную на 1
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает
    наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
# фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
# загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict)

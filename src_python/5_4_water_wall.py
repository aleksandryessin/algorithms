"""
«Container With Most Water» / максимальная площадь между двумя «стенками».

Дано: массив высот. Выбираем две позиции i < j; площадь = (j - i) * min(h[i], h[j]).

Два указателя с краёв: на каждом шаге считаем площадь для текущей пары.
Чтобы не пропустить максимум: двигаем тот указатель, у которого высота меньше —
у более низкой стенки сдвиг может только увеличить min или длину, смысл жадного шага.

Сложность: O(N) время, O(1) память.
"""


def max_water_area(walls: list) -> int:
    start = 0
    end = len(walls) - 1
    max_area = 0

    while start < end:
        width = end - start
        height = min(walls[start], walls[end])
        max_area = max(max_area, width * height)

        # Убираем более низкую сторону — она уже не улучшит ответ для этой пары.
        if walls[start] < walls[end]:
            start += 1
        else:
            end -= 1

    return max_area


if __name__ == "__main__":
    walls = [2, 6, 7, 3, 5, 7, 4]
    print(max_water_area(walls))  # 24

    walls2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_water_area(walls2))  # 49

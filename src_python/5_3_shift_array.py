"""
Циклический сдвиг массива вправо на n позиций за O(N) времени и O(1) памяти.

Трюк «три реверса»:
1) Развернуть весь массив.
2) Развернуть левую часть длины shift (то, что должно оказаться справа после сдвига).
3) Развернуть правую оставшуюся часть.

Пример: [1,2,3,4,5], сдвиг 2 вправо → [4,5,1,2,3].
После шага 1: [5,4,3,2,1]. Нужно shift=2: реверс [0:2] → [4,5,3,2,1], реверс [2:5] → [4,5,1,2,3].

Формула shift = ((n % len) + len) % len — корректно для отрицательных n и n > len(arr).
"""


def reverse(arr: list, start: int, end: int):
    """Поменять местами элементы с индексами start..end включительно (два указателя к центру)."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def shift_array(arr: list, n: int):
    shift = ((n % len(arr)) + len(arr)) % len(arr)
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, shift - 1)
    reverse(arr, shift, len(arr) - 1)


if __name__ == "__main__":
    arr = [1, 1, 5, 3, 6, 9]
    print(arr)
    shift_array(arr, 4)
    print(arr)  # [5, 3, 6, 9, 1, 1]

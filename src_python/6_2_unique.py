"""
Проверка: все символы в строке различны (в рамках выбранного алфавита).

Здесь: печатные ASCII — 95 символов от пробела (32) до тильды (126).
Если длина строки больше 95, по принципу голубиных норок дубликат неизбежен — сразу False.

Массив seen[0..94] — флаг «символ с этим смещением уже встречался».
ord(ch) - 32 переводит символ в индекс 0..94.
Сложность: O(N) по времени, O(1) по памяти (фиксированный массив 95).
"""


def is_unique(s: str) -> bool:
    if len(s) > 95:
        return False
    chars = [False] * 95
    for ch in s:
        code = ord(ch) - 32
        if chars[code]:
            return False
        chars[code] = True
    return True


if __name__ == "__main__":
    char_list1 = 'abfb'
    char_list2 = 'abcdef'
    print(is_unique(char_list1))
    print(is_unique(char_list2))

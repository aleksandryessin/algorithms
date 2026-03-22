"""
Подсчитать количество «слов», состоящих только из латинских букв A–Z и a–z.

Логика конечного автомата:
- latin = True означает: текущее слово (с начала или после пробела) пока состоит только из латиницы.
- Пробел: если latin ещё True — мы закончили хорошее слово, count++.
  Если latin был False — слово было «испорчено» не-латиницей; начинаем новое слово с latin=True.
- Не-пробел: если код символа вне диапазонов латиницы — latin=False (это слово не засчитаем).

В конце строки: если последнее слово не закончилось пробелом и latin=True — увеличиваем count.

Диапазоны Unicode-кодов: A–Z = 65–90, a–z = 97–122.
"""


def count_latin_words(s: str) -> int:
    count = 0
    latin = True
    for ch in s:
        code = ord(ch)
        if code == 32:
            if latin:
                count += 1
            else:
                latin = True
        else:
            if (code < 65) or (90 < code < 97) or (code > 122):
                latin = False
    if latin:
        count += 1
    return count


if __name__ == "__main__":
    char_list1 = 'hello world'
    char_list2 = 'hello world123 foo'
    char_list3 = '23 456'
    char_list4 = 'cat one dog 1wo'
    print(count_latin_words(char_list1))
    print(count_latin_words(char_list2))
    print(count_latin_words(char_list3))
    print(count_latin_words(char_list4))

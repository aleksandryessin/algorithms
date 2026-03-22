"""
Изоморфные строки: можно ли сопоставить символам первой строки символы второй однозначно
(как «a→x», «b→y»), без коллизий в обе стороны.

Трюк с «последней позицией»: для каждого символа храним номер позиции (1-based), где он последний раз
участвовал в согласовании. На шаге i символы s1[i] и s2[i] должны иметь одинаковую «историю»:
если num_s1[c1] != num_s2[c2], значит раньше один из символов уже вёл себя иначе — не изоморфизм.

Индексы символов: ord(ch) - 32 для печатного ASCII (95 символов).

Сложность: O(N) по времени, O(1) по памяти (два массива фиксированного размера).
"""


def is_isomorphic(s1: str, s2: str) -> bool:
    num_s1 = [0] * 95
    num_s2 = [0] * 95

    for i in range(len(s1)):
        code1 = ord(s1[i]) - 32
        code2 = ord(s2[i]) - 32
        if num_s1[code1] != num_s2[code2]:
            return False
        num_s1[code1] = i + 1
        num_s2[code2] = i + 1

    return True


if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))       # True
    print(is_isomorphic("foo", "bar"))       # False
    print(is_isomorphic("paper", "title"))   # True
    print(is_isomorphic("ab", "aa"))         # False
    print(is_isomorphic("abc", "abc"))       # True

"""
Проверить, является ли одна строка перестановкой другой (одинаковый набор букв).

Условие: одинаковая длина; только строчные латинские буквы (как в учебной задаче).

Счётчики на 26 позиций: при проходе по i-му символу увеличиваем для s1[i], уменьшаем для s2[i].
Если в итоге все 26 ячеек нули — частоты совпали.

Сложность: O(N) по времени, O(1) по памяти (26 константа).
"""


def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    count_letters = [0] * 26
    for i in range(len(s1)):
        count_letters[ord(s1[i]) - ord('a')] += 1
        count_letters[ord(s2[i]) - ord('a')] -= 1

    for c in count_letters:
        if c != 0:
            return False
    return True


if __name__ == "__main__":
    print(is_permutation("abc", "cba"))     # True
    print(is_permutation("abc", "abc"))     # True
    print(is_permutation("abc", "abd"))     # False
    print(is_permutation("aab", "aba"))     # True
    print(is_permutation("abc", "abcd"))    # False

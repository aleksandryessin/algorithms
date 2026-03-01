
def is_permutation(s1: str, s2: str) -> bool:

    """
    O(N) по времени, O(1) по памяти
    1. Если длины разные — сразу False.
    2. Массив на 26 элементов (по числу латинских букв).
    3. Для первой строки увеличиваем счётчик, для второй — уменьшаем.
    4. Если все счётчики равны 0 — перестановка.
    """
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

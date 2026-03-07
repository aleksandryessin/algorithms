
def is_isomorphic(s1: str, s2: str) -> bool:

    """
    O(N) по времени, O(1) по памяти
    Два массива на 95 элементов (печатные ASCII).
    Записываем позицию последнего появления символа.
    Если позиции не совпадают — не изоморфны.
    """
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

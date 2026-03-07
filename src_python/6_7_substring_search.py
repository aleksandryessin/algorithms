
def substring_search(s1: str, s2: str) -> int:

    """
    O(A*B) по времени, O(1) по памяти
    Наивный поиск подстроки: для каждой позиции в s1
    проверяем, совпадает ли подстрока длиной len(s2).
    """
    if len(s2) > len(s1):
        return -1

    for L in range(len(s1) - len(s2) + 1):
        S = 0
        while S < len(s2):
            if s2[S] != s1[L + S]:
                break
            S += 1
        if S == len(s2):
            return L

    return -1


if __name__ == "__main__":
    print(substring_search("hello world", "world"))   # 6
    print(substring_search("hello world", "hello"))   # 0
    print(substring_search("hello world", "xyz"))     # -1
    print(substring_search("aaabaaab", "aaab"))       # 0
    print(substring_search("abc", "abcdef"))          # -1
    print(substring_search("program", "ram"))         # 4

"""
В отсортированном по возрастанию массиве найти все пары индексов (i, j), i < j,
такие что arr[i] + arr[j] == n.

Два указателя: start слева, end справа.
- Если сумма меньше n — увеличить левую (нужно больше сумма).
- Если больше n — уменьшить правую.
- Если равна n — записать пару и сдвинуть оба (ищем другие пары).

Предусловие: массив отсортирован. Сложность: O(N) по времени.
Память: O(K) на список результатов, K — число пар.
"""


def pairs_n_sum(arr: list, n: int) -> list:
    result = []
    start = 0
    end = len(arr) - 1

    while start < end:
        s = arr[start] + arr[end]
        if s == n:
            result.append([start, end])
            start += 1
            end -= 1
        elif s < n:
            start += 1
        else:
            end -= 1

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = 8
    pairs = pairs_n_sum(arr, n)
    for pair in pairs:
        print(f"[{pair[0]}, {pair[1]}]")
    # [0, 6]  (1+7=8)
    # [1, 5]  (2+6=8)
    # [2, 4]  (3+5=8)

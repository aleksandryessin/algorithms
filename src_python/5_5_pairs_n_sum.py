
def pairs_n_sum(arr: list, n: int) -> list:

    """
    O(N) по времени, O(1) по памяти (не считая результата)
    Два указателя: находим все пары индексов,
    сумма элементов которых равна n.
    """
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

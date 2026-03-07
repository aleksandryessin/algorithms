
def remove_duplicates(arr: list) -> int:

    """
    O(N) по времени, O(1) по памяти
    Удаляет дубликаты из отсортированного массива,
    возвращает длину массива без дубликатов.
    """
    if len(arr) == 1:
        return 1
    L = 1
    for R in range(2, len(arr)):
        val = arr[R]
        if arr[L - 1] == val:
            continue
        L += 1
    return L


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 7, 7, 7, 7]
    print(remove_duplicates(arr))  # 5

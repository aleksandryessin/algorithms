
def reverse(arr: list, start: int, end: int):
    """Реверс подмассива на месте."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def shift_array(arr: list, n: int):

    """
    O(N) по времени, O(1) по памяти
    Циклический сдвиг массива на n позиций вправо
    через три реверса.
    """
    shift = ((n % len(arr)) + len(arr)) % len(arr)
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, shift - 1)
    reverse(arr, shift, len(arr) - 1)


if __name__ == "__main__":
    arr = [1, 1, 5, 3, 6, 9]
    print(arr)
    shift_array(arr, 4)
    print(arr)  # [5, 3, 6, 9, 1, 1]

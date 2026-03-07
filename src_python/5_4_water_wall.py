
def max_water_area(walls: list) -> int:

    """
    O(N) по времени, O(1) по памяти
    Container With Most Water — два указателя.
    """
    start = 0
    end = len(walls) - 1
    max_area = 0

    while start < end:
        width = end - start
        height = min(walls[start], walls[end])
        max_area = max(max_area, width * height)

        if walls[start] < walls[end]:
            start += 1
        else:
            end -= 1

    return max_area


if __name__ == "__main__":
    walls = [2, 6, 7, 3, 5, 7, 4]
    print(max_water_area(walls))  # 24

    walls2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_water_area(walls2))  # 49

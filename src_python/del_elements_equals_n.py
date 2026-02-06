from ast import main
from os import name


class Del_element():

    def __init__(self) -> None:
        pass 

    def del_element(self, array: [int], n: int):

        """
        1. Проходим по массиву двумя указателями L и R (R идет слева направо).
        2. Если текущий элемент array[R] НЕ равен n, то записываем его в позицию L.
        3. L увеличиваем только когда записали элемент, который остается.
        4. R всегда увеличивается на каждом шаге цикла.
        5. Цикл заканчивается, когда R прошел всю длину массива.
        6. L — это количество оставшихся элементов (новая длина).
        7. Массив изменяется на месте: актуальная часть — array[:L].
        """
        L = 0
        R = 0
    
        for R in range(len(array)):
            if array[R] == n:
                continue
            else:
                array[L] = array[R]
            L+=1
        return print(f"Исходная строка: {array}\nИсходная длина = {len(array)}\nНайдено элементов n: {len(array)-L}\nДлина после удаления {n}-элемента = {L}\nФинальная строка: {array[:L]}")


if __name__ == "__main__":
    My_test = Del_element()
    arr = [1, 2, 2, 3, 4, 2, 5, 2, 6, 10]
    n = 2
    My_test.del_element(arr, n)
    
    
"""
Найти дубликаты в массиве чисел из диапазона 1..32000, используя O(N) времени
и O(1) дополнительной памяти относительно ограничения задачи (битовый вектор фиксированного размера).

Идея: один бит на возможное значение числа. Встретили число k — смотрим бит (k-1);
если уже установлен — это второй раз, печатаем; иначе ставим бит.
"""

class BitVector:
    def __init__(self, bits: int):
        if bits <= 0 or bits > 68719476704:
            raise Exception("Invalid size")
        self.max_index = bits - 1
        size = ((bits - 1) >> 5) + 1
        self.bit_vector = [0] * size

    def _check_index(self, index: int):
        if index < 0 or index > self.max_index:
            raise Exception("Index out of range")

    def _get_row(self, index: int) -> int:
        return index >> 5

    def _get_col(self, index: int) -> int:
        return index % 32

    def set_bit(self, index: int):
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        self.bit_vector[row] |= (1 << col)

    def is_set_bit(self, index: int) -> bool:
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        return (self.bit_vector[row] & (1 << col)) != 0


def print_duplicates(numbers: list):
    bv = BitVector(32000)
    for num in numbers:
        idx = num - 1  # переводим 1..32000 в 0..31999
        if bv.is_set_bit(idx):
            print(num)
        else:
            bv.set_bit(idx)


if __name__ == "__main__":
    numbers = [1, 5, 4, 5, 4, 10, 11, 12, 21, 3, 3, 5, 7, 22, 21]
    print_duplicates(numbers)

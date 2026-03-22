"""
Задача: среди огромного количества неотрицательных чисел найти одно отсутствующее
(в классической постановке — из диапазона 0..2^31-1 или похожего).

Идея с битовым вектором на 2^31 позиций: для каждого прочитанного числа ставим бит.
Потом ищем первый нулевой бит — это и есть отсутствующее значение.

Внимание: такой вектор в памяти огромен; в учебной задаче важна именно идея «пометить
все встреченные за один проход». На практике для 2^31 бит нужны гигабайты — возможны
другие трюки (внешняя память, разбиение на блоки и т.д.).

Чтение из файла: числа могут быть разделены пробелами и переносами строк.
"""

import sys


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


def find_missing_number(path: str) -> int:
    # Покрываем все возможные 32-битные неотрицательные int в типичной постановке (0 .. 2^31-1).
    bv = BitVector(2_147_483_648)
    with open(path, 'r') as f:
        for line in f:
            for num_str in line.split():
                bv.set_bit(int(num_str))
    for i in range(2_147_483_648):
        if not bv.is_set_bit(i):
            return i
    raise Exception("No missing number found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2_8_find_number.py <inputFilePath>")
    else:
        missing = find_missing_number(sys.argv[1])
        print(f"The missing number is: {missing}")

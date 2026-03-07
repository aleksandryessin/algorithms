
# Дано 3 млрд неотрицательных чисел. Вывести 1 число, которого нет в файле.
# Ограничение по памяти — 512 Мб.
# Используем битовый вектор на 2^31 значений.

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

"""
Битовый вектор: храним много булевых флагов в массиве целых чисел по 32 бита.

Почему не один огромный int? Так тоже можно, но массив «слов» по 32 бита —
классический компактный вариант (как в низкоуровневых структурах).

Индекс бита index → номер «слова» row = index // 32 (здесь через >> 5)
и позиция внутри слова col = index % 32.
"""


class BitVector:
    def __init__(self, bits: int):
        if bits <= 0 or bits > 68719476704:
            raise Exception("Invalid size")
        self.max_index = bits - 1
        # Количество 32-битных ячеек: округление вверх от bits/32.
        size = ((bits - 1) >> 5) + 1
        self.bit_vector = [0] * size

    def _check_index(self, index: int):
        if index < 0 or index > self.max_index:
            raise Exception("Index out of range")

    def _get_row(self, index: int) -> int:
        return index >> 5  # деление на 32

    def _get_col(self, index: int) -> int:
        return index % 32  # смещение внутри 32-битного слова

    def set_bit(self, index: int):
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        mask = 1 << col
        # OR включает бит независимо от предыдущего значения.
        self.bit_vector[row] |= mask

    def unset_bit(self, index: int):
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        # ~(1 << col) — единицу только в этом бите обнулили в маске; AND выключает бит.
        mask = ~(1 << col)
        self.bit_vector[row] &= mask

    def inverse_bit(self, index: int):
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        mask = 1 << col
        self.bit_vector[row] ^= mask

    def is_set_bit(self, index: int) -> bool:
        self._check_index(index)
        row = self._get_row(index)
        col = self._get_col(index)
        mask = 1 << col
        bit = self.bit_vector[row] & mask
        return bit != 0


if __name__ == "__main__":
    bv = BitVector(96)
    bv.set_bit(70)
    print(bv.is_set_bit(70))  # True

"""
То же решение, что в 2_5_bit.py: вставка битов B в диапазон [end, start] числа A.

Кратко по шагам:
- mask_l + mask_r — в A сохраняются биты вне «окна», внутри окна — нули.
- B << end поднимает нужный фрагмент; mask_b обрезает лишнее сверху.
- A | B склеивает очищенное A с вставленным фрагментом; & 0xFFFFFFFF — ровно 32 бита.
"""

A = 285689642
B = 1132478069
start = 16
end = 5

mask_l = (-1 << (start + 1)) & 0xFFFFFFFF
mask_r = (1 << end) - 1
mask_a = mask_l | mask_r
A &= mask_a

B <<= end
mask_b = (1 << (start + 1)) - 1
B &= mask_b

result = (A | B) & 0xFFFFFFFF
if result >= 0x80000000:
    result -= 0x100000000
print(result)

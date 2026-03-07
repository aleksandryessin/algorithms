
# Решение: вставить младшие биты B в позиции [end, start] числа A
A = 285689642
B = 1132478069
start = 16
end = 5

# Единицы в старших битах до start
mask_l = (-1 << (start + 1)) & 0xFFFFFFFF
# Единицы в младших битах после end
mask_r = (1 << end) - 1
mask_a = mask_l | mask_r
A &= mask_a

# Пододвигаем младшие биты B к нашему диапазону
B <<= end
# Единицы в B после start
mask_b = (1 << (start + 1)) - 1
B &= mask_b

result = (A | B) & 0xFFFFFFFF
if result >= 0x80000000:
    result -= 0x100000000
print(result)


# Вставить младшие биты B в позиции [end, start] числа A
# В Python нет переполнения int, но логика та же

A = 285689642
B = 1132478069
start = 16
end = 5

# mask left: единицы от 31 до start+1
# В Python int произвольной длины, поэтому -1 << (start+1) работает напрямую,
# но нужно обрезать до 32 бит
mask_l = (-1 << (start + 1)) & 0xFFFFFFFF

# mask right: единицы от end-1 до 0
mask_r = (1 << end) - 1

mask_a = mask_l | mask_r
A &= mask_a

# Сдвигаем B на end позиций влево
B <<= end

# Зануляем старшие биты в B (оставляем только биты 0..start)
mask_b = (1 << (start + 1)) - 1
B &= mask_b

result = (A | B) & 0xFFFFFFFF
# Преобразуем в знаковое 32-битное число
if result >= 0x80000000:
    result -= 0x100000000
print(result)

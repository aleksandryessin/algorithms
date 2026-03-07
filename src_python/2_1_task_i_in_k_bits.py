
# Установить i-й бит в k-ю позицию
# a = 0x63 = 0110 0011, k = 3, i = 3
a = 0x63
result = (a | 8) & 0xFF
print(result)

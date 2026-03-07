
# Проверка установлен ли бит (AND с маской)
def is_bit(a: int) -> bool:
    result = a & 0x02
    return result != 0


if __name__ == "__main__":
    a = 0x16
    print(is_bit(a))

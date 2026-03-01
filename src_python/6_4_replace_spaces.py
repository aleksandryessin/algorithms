
def replace_spaces(s: str) -> str:

    """
    O(N) по времени
    1. Считаем пробелы, вычисляем длину нового массива.
    2. Создаём массив символов нужной длины.
    3. Проходим по строке: пробел → '%20', иначе → копируем символ.
    4. Собираем строку из массива.
    """
    count_spaces = sum(1 for ch in s if ch == ' ')
    res = [''] * (len(s) + count_spaces * 2)
    free = 0
    for ch in s:
        if ch == ' ':
            res[free] = '%'
            res[free + 1] = '2'
            res[free + 2] = '0'
            free += 3
        else:
            res[free] = ch
            free += 1
    return ''.join(res)


if __name__=="__main__":
    print(replace_spaces('hello world'))        # hello%20world
    print(replace_spaces('a b c'))              # a%20b%20c
    print(replace_spaces('nospaces'))           # nospaces
    print(replace_spaces(' hi '))               # %20hi%20

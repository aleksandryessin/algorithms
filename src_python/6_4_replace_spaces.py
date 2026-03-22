"""
Заменить каждый пробел на три символа '%20' (как в типичной задаче про URL).

Один пробел → три символа, значит новая длина = len(s) + 2 * (число пробелов).

Два прохода (здесь совмещено в один цикл по исходной строке):
1) посчитать пробелы и выделить массив нужной длины;
2) заполнить: обычный символ копируется один раз, пробел — тройкой '%', '2', '0'.

Сложность: O(N) по времени и по памяти под результат.
"""


def replace_spaces(s: str) -> str:
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


if __name__ == "__main__":
    print(replace_spaces('hello world'))        # hello%20world
    print(replace_spaces('a b c'))              # a%20b%20c
    print(replace_spaces('nospaces'))           # nospaces
    print(replace_spaces(' hi '))               # %20hi%20

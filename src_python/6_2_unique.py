from os import name


def is_unique(s: str) -> bool:
    if len(s) > 95:
        return False
    chars = [False]*95
    for ch in s:
        code = ord(ch) - 32 # смещение, чтобы соответствовать печатным символам и символам в строке s
        if chars[code]:
            return False
        chars[code] = True
    return True

if __name__=="__main__":
    char_list1 = 'abfb'
    char_list2 = 'abcdef'
    print(is_unique(char_list1))
    print(is_unique(char_list2))
        
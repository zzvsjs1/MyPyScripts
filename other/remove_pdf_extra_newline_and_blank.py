import re
import pyperclip


def remove(string: str):
    return re.sub(r'\s+', ' ', string)
    # return re.sub(r' {2,}', ' ', re.sub(r'\s+', ' ', string))


if __name__ == '__main__':
    pyperclip.copy(remove(pyperclip.paste()))

import os
from sys import argv
from time import sleep

argc = len(argv)
lang = ""
clear = lambda: os.system("cls")
line = lambda: print("="*80)
txt = {
    "en": "",
    "kr": ""
}
def txts(en="", kr=""):
    global lang, txt
    txt["en"] = en
    txt["kr"] = kr
    return txt[lang]


class Main:
    def __init__(self):
        ...

if __name__ == "__main__":
    if argc == 1:
        lang = "en"
    elif argc == 2:
        if argv[1] == "-e":
            lang = "en"
        elif argv[1] == "-k":
            lang = "kr"
        else:
            print("Invalid command.")
            exit(1)
    else:
        print("Invalid command.")
        exit(1)
    line()
    print(txts(
        "Escape from Hakurei shrine        v0.00",
        "하쿠레이 신사에서 탈출하기        v0.00"
    ))
    print(txts(
        "This is second creation of Touhou project.",
        "해당 프로그램은 동방프로젝트의 2차창작물입니다."
    ))
    line()
    Main()
    exit(0)

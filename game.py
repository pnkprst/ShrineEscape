import os
from sys import argv

argc = len(argv)
lang = ""
clear = lambda: os.system("cls")
line = lambda: print("="*80)
def prompt(name, group):
    return input("[%s|%s] $ " % (name, group))

user = [" ", " "]
difficulty = ''


class Main:
    def __init__(self):
        ...

if __name__ == "__main__":
    if argc == 1:
        lang = 0
    elif argc == 2:
        if argv[1] == "-e":
            lang = 0
        elif argv[1] == "-k":
            lang = 1
        elif argv[1] == "-j":
            lang = 2
        elif argv[1] == "-c":
            lang = 3
        elif argv[1] == "-r":
            lang = 4
        else:
            print("Invalid command.")
            exit(1)
    else:
        print("Invalid command.")
        exit(1)
    line()
    print([
        "  Escape from Hakurei shrine        v0.00",
        "  하쿠레이 신사에서 탈출하기        v0.00",
        "  日本語訳はまだ",
        "  中文翻译",
        "  Перевод с русского на"
    ][lang])
    print([
        "  This is second creation of Touhou project.",
        "  해당 프로그램은 동방프로젝트의 2차창작물입니다.",
        "  提供されていません。",
        "  还没有提供。",
        "  русский пока не доступен."
    ][lang])
    line()
    print([
        "To start, please login.",
        "시작하시려면 로그인하십시오.",
        "次のアップデートをお待ちください。",
        "请等待下一个更新。",
        "Ждите следующих обновлений."
    ][lang])
    while True:
        cmd = prompt(user[0], user[1]).split()
        if len(cmd) == 1:
            if cmd[0] == "logout":
                print([
                    "Close the program.",
                    "프로그램을 종료합니다."
                    "プログラムを終了します。",
                    "退出程序。",
                    "Выйти из приложения."
                ][lang])
                exit(0)
        elif len(cmd) == 2:
            if cmd[1][0] != '-':
                cmd.insert(1, "-e")
            else:
                print([
                    "No account name in command.",
                    "계정명을 입력하셔야 합니다."
                    "<japanese text>",
                    "<chinese text>",
                    "<russian text>"
                ][lang])
                continue
        elif len(cmd) > 3:
            print([
                "Invalid command.",
                "옳바르지 못한 명령어입니다."
                "<japanese text>",
                "<chinese text>",
                "<russian text>"
            ][lang])
            continue
        if cmd[0] == "login":
            if cmd[1][1] in ('e', 'n', 'h', 'l'):
                difficulty = cmd[1][1]
                if cmd[2] in ("mrskr", "skyiz", "kcysn", "hctylp"):
                    user[0] = cmd[2]
                    if user[0] == "mrskr":
                        user[1] = "usrf"
                    else:
                        user[1] = "usrg"
                    print(["Welcome " + user[0],
                        user[0] + "님, 환영합니다.",
                        user[0] + "<japanese text>",
                        "<chinese text>" + user[0],
                        "<russian text>" + user[0]
                    ][lang])
                    break
                elif cmd[2] == "rimhk":
                    print([
                        "Cannot login by that account.",
                        "접근 불가능한 계정입니다."
                        "<japanese text>",
                        "<chinese text>",
                        "<russian text>"
                    ][lang])
                    continue
                else:
                    print([
                        "Unexist account.",
                        "존재하지 않는 계정입니다."
                        "<japanese text>",
                        "<chinese text>",
                        "<russian text>"
                    ][lang])
                    continue
            else:
                print([
                    "Invalid mode.",
                    "해당 난이도는 없습니다."
                    "<japanese text>",
                    "<chinese text>",
                    "<russian text>"
                ][lang])
                continue
        print([
            "Invalid command.",
            "옳바르지 못한 명령어입니다."
            "<japanese text>",
            "<chinese text>",
            "<russian text>"
        ][lang])
    Main()
    exit(0)

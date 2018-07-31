import random

def hangman(word):
    wrong = 0
    stages = [
        "",
        "_____     ",
        "|         ",
        "|    |    ",
        "|    O    ",
        "|   /|\   ",
        "|   / \   ",
        "|         "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    print("リタイアするには'escape'と入力してね")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg).rstrip().lower()
        if char == "escape":
            break
        if char in rletters and char != "$":
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("\n")
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

animal_easy = ["cat", "dog", "fox", "cow", "pig", "bird", "wolf", "lion", "bear"]
animal_normal = ["mouse", "horse", "sheep", "zebra", "rabbit", "monkey", "donkey", "hamster", "leopard", "giraffe"]
answer_list = []

diff = input("難易度を選択してください\neasy: 3～4文字\nnormal: 5～7文字\n").rstrip().lower()
if diff == "easy":
    answer_list = animal_easy
elif diff == "normal":
    answer_list = animal_normal
else:
    diff = "easy"
    answer_list = animal_easy
print("難易度{}\n".format(diff))
answer_index = random.randint(0, len(answer_list)-1)
hangman(answer_list[answer_index])

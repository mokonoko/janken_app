import random
import tkinter as tk
from PIL import Image, ImageTk

GU, CHOKI, PA = 'グー', 'チョキ', 'パー'
hands = ['グー', 'チョキ', 'パー']
WIN, DRAW, LOSE = "勝ち", "あいこ", "負け"

rules = {
    (0, 0): DRAW, (0, 1): WIN, (0, 2): LOSE,
    (1, 0): LOSE, (1, 1): DRAW, (1, 2): WIN,
    (2, 0): WIN, (2, 1): LOSE, (2, 2): DRAW,
}

root = tk.Tk()
root.geometry('420x400')

gu_image = Image.open('img/gu.png').convert('RGB').resize((100, 100))
gu_image = ImageTk.PhotoImage(gu_image)

choki_image = Image.open('img/choki.png').convert('RGB').resize((100, 100))
choki_image = ImageTk.PhotoImage(choki_image)

pa_image = Image.open('img/pa.png').convert('RGB').resize((100, 100))
pa_image = ImageTk.PhotoImage(pa_image)


def press_gu():
    judge(0)


def press_choki():
    judge(1)


def press_pa():
    judge(2)


tk.Label(root, image=gu_image).place(x=20, y=200)
tk.Label(root, image=choki_image).place(x=160, y=200)
tk.Label(root, image=pa_image).place(x=300, y=200)

gu_btn = tk.Button(root, text='グー', command=press_gu)
gu_btn.place(x=50, y=320)

choki_btn = tk.Button(root, text='チョキ',  command=press_choki)
choki_btn.place(x=190, y=320)

pa_btn = tk.Button(root, text='パー',  command=press_pa)
pa_btn.place(x=335, y=320)

enemy_label = tk.Label(root, image=gu_image)
enemy_label.place(x=160, y=20)
text_label = tk.Label(root, text='最初はグー！じゃんけん！')
text_label.place(x=140, y=140)


def retry():
    retry_btn.place_forget()
    gu_btn['state'] = tk.ACTIVE
    choki_btn['state'] = tk.ACTIVE
    pa_btn['state'] = tk.ACTIVE


retry_btn = tk.Button(root, text='リトライ', command=retry)


def show_retry():
    retry_btn.place(x=185, y=360)
    gu_btn['state'] = tk.DISABLED
    choki_btn['state'] = tk.DISABLED
    pa_btn['state'] = tk.DISABLED


def judge(me):
    enemy = random.randint(0, 2)

    result = rules[(me, enemy)]

    if result == DRAW:
        text_label.configure(text='あいこでしょ！')
    elif result == WIN:
        text_label.configure(text='勝ち！')
        show_retry()
    else:
        text_label.configure(text='負け！')
        show_retry()


root.mainloop()

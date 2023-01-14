import os
import tkinter as tk
from PIL import Image, ImageTk
import time
from pygame import init, mixer
import random
import music_data

init()
current_song = ""

window = tk.Tk()
window.title("Rhythm Rampage")
window.geometry("1000x700+100+100")
window.resizable(False, False)

window.iconbitmap(False, tk.PhotoImage("icons/rhythm.ico"))

c = tk.Canvas(window, width=1000, height=700, bg="black", highlightthickness=0)
c.pack()

c.create_rectangle(300, 580, 700, 585, fill="red")

line_coords = [[350 + 100 * i, 0, 355 + 100 * i, 700] for i in range(4)]
for i in line_coords:
    c.create_rectangle(i, fill="white")

imgs = {
    "up": ImageTk.PhotoImage(Image.open("images/up.png")),
    "down": ImageTk.PhotoImage(Image.open("images/down.png")),
    "left": ImageTk.PhotoImage(Image.open("images/left.png")),
    "right": ImageTk.PhotoImage(Image.open("images/right.png"))
}

score = 0
user_all_percent = 0
arrows_list = []
songs_list = [i for i in list(music_data.music_data.keys())]
current_song = songs_list[0]


score_text = c.create_text(140, 55, text=f"Счет: 0", fill="white", font=("Arial", 30))
duration_text = c.create_text(960, 30, text="0", fill="white", font=("Arial", 30))


def create_arrow():
    if len(new_beats_list) == 0:
        return

    if time.time() >= new_beats_list[0]:
        new_beats_list.pop(0)
        coords = random.choice(line_coords)
        img = random.choice(list(imgs.values()))
        arrow = c.create_image(coords[0], coords[1], image=img, tag=list(imgs.keys())[list(imgs.values()).index(img)])
        arrows_list.append(arrow)


def move_arrows():
    if not game_over:
        for arrow in arrows_list:
            if c.coords(arrow)[1] > 710:
                arrows_list.remove(arrow)
                c.delete(arrow)
            else:
                c.move(arrow, 0, 3)


new_beats_list = []
start = 0
clicks_count = 0
song_choosing = False
def key_press_handler(event):
    global score, user_all_percent, starting, arrows_list, game_over, clicks_count, song_choosing, current_song
    p = 20
    min_y = 580 - p
    max_y = 680
    if len(arrows_list) != 0 and not game_over:
        if event.keysym == "Right":
            clicks_count += 1
            for arrow in arrows_list:
                if min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) == "pyimage4":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    score += 1
                    c.itemconfigure(score_text, text=f"Счет: {score}")
                    numbers = {i for i in range(150, 851)} ^ {i for i in range(100, 650)}
                    beat_text = c.create_text(random.choice(list(numbers)), random.randint(200, 500), text=random.choice(["В цель!", "Под бит!", "Так держать!"]), fill="white", font=("Arial", random.randint(8, 20), "bold"))
                    window.after(random.randint(700, 1000), lambda: c.delete(beat_text))
                    break

                elif min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) != "pyimage4":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    break

        elif event.keysym == "Left":
            clicks_count += 1
            for arrow in arrows_list:
                if min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) == "pyimage3":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    score += 1
                    c.itemconfigure(score_text, text=f"Счет: {score}")
                    numbers = {i for i in range(150, 851)} ^ {i for i in range(100, 650)}
                    beat_text = c.create_text(random.choice(list(numbers)), random.randint(200, 500), text=random.choice(["В цель!", "Под бит!", "Так держать!"]), fill="white", font=("Arial", random.randint(8, 20), "bold"))
                    window.after(random.randint(700, 1000), lambda: c.delete(beat_text))
                    break
                elif min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) != "pyimage3":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    break

        elif event.keysym == "Up":
            clicks_count += 1
            for arrow in arrows_list:
                if min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) == "pyimage1":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    score += 1
                    c.itemconfigure(score_text, text=f"Счет: {score}")
                    numbers = {i for i in range(150, 851)} ^ {i for i in range(100, 650)}
                    beat_text = c.create_text(random.choice(list(numbers)), random.randint(200, 500), text=random.choice(["В цель!", "Под бит!", "Так держать!"]), fill="white", font=("Arial", random.randint(8, 20), "bold"))
                    window.after(random.randint(700, 1000), lambda: c.delete(beat_text))
                    break
                elif min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) != "pyimage1":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    break

        elif event.keysym == "Down":
            clicks_count += 1
            for arrow in arrows_list:
                if min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) == "pyimage2":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    score += 1
                    c.itemconfigure(score_text, text=f"Счет: {score}")
                    numbers = {i for i in range(150, 851)} ^ {i for i in range(100, 650)}
                    beat_text = c.create_text(random.choice(list(numbers)), random.randint(200, 500), text=random.choice(["В цель!", "Под бит!", "Так держать!"]), fill="white", font=("Arial", random.randint(8, 20), "bold"))
                    window.after(random.randint(700, 1000), lambda: c.delete(beat_text))
                    break
                elif min_y < c.coords(arrow)[1] < max_y and str(c.itemcget(arrow, "image")) != "pyimage2":
                    c.delete(arrow)
                    arrows_list.remove(arrow)
                    break

    elif starting:
        if song_choosing and event.keysym == "Down":
            try:
                current_song = songs_list[songs_list.index(current_song) + 1]
            except IndexError:
                current_song = songs_list[0]
            if 36 <= len(current_song):
                c.itemconfigure(menu_objects[-1], text="> " + current_song + " <", font=("Consolas", round(len(current_song) * 0.7), "bold"))
            else:
                c.itemconfigure(menu_objects[-1], text="> " + current_song + " <", font=("Consolas", round(len(current_song) * 1.4), "bold"))

        elif song_choosing and event.keysym == "Up":
            current_song = songs_list[songs_list.index(current_song) - 1]
            if 36 <= len(current_song):
                c.itemconfigure(menu_objects[-1], text="> " + current_song + " <", font=("Consolas", round(len(current_song) * 0.7), "bold"))
            else:
                c.itemconfigure(menu_objects[-1], text="> " + current_song + " <", font=("Consolas", round(len(current_song) * 1.4), "bold"))

        elif event.keysym == "e":
            if song_choosing:
                song_choosing = False
                reload_game()
            else:
                song_choosing = True
                for i in menu_objects:
                    c.delete(menu_objects)

                menu_objects.append(c.create_rectangle(0, 0, 1000, 700, fill="black"))
                menu_objects.append(c.create_text(500, 100, text="Rhythm Rampage", justify=tk.CENTER, fill="white", font=("Comic Sans MS", 80, "bold")))
                menu_objects.append(c.create_text(500, 255, text=f"Выберите песню используя джойстик и кнопку E для выбора",justify=tk.CENTER, fill="white", font=("Consolas", 20, "bold")))

                if 36 <= len(current_song):
                    menu_objects.append(c.create_text(500, 400, text="> " + current_song + " <", justify=tk.CENTER, fill="white", font=("Consolas", round(len(current_song)*0.7), "bold")))
                else:
                    menu_objects.append(c.create_text(500, 400, text="> " + current_song + " <", justify=tk.CENTER, fill="white", font=("Consolas", round(len(current_song)*1.4), "bold")))


        elif event.keysym == "q":
            on_close_window()





pause_text = None
def reload_game():
    global new_beats_list, start, current_song, score, starting, game_over, user_all_percent, arrows_list, clicks_count

    starting = False
    game_over = False
    for i in menu_objects:
        c.delete(i)

    c.itemconfigure(score_text, text=f"Счет: {score}")
    current_time = time.time()
    new_beats_list = [current_time + i - 1 for i in music_data.music_data[current_song]["beat_times"]]
    start = time.time()
    score = 0
    user_all_percent = 0
    arrows_list = []
    clicks_count = 0

    game_loop()
    mixer.Channel(0).play(mixer.Sound(music_data.music_data[current_song]["filename"]))
    window.after(1000, update_duration)


def show_game_end_window():
    global starting, user_all_percent, score, game_over, arrows_list

    for i in arrows_list:
        c.delete(i)

    user_all_percent = round((score / len(music_data.music_data[current_song]["beat_times"])) * 100)

    mixer.Channel(0).stop()
    starting = True
    menu_objects.append(c.create_rectangle(0, 0, 1000, 700, fill="black"))
    menu_objects.append(c.create_text(500, 100, text="Rhythm Rampage", justify=tk.CENTER, fill="white", font=("Comic Sans MS", 80, "bold")))
    menu_objects.append(c.create_text(500, 255, text=f"Всего битов было: {len(music_data.music_data[current_song]['beat_times'])}", justify=tk.CENTER, fill="white", font=("Consolas", 20, "bold")))
    menu_objects.append(c.create_text(500, 285, text=f"Вы попали в биты {score} раз(-а) - это {round(score/len(music_data.music_data[current_song]['beat_times']) * 100)}%", justify=tk.CENTER, fill="white", font=("Consolas", 20, "bold")))
    menu_objects.append(c.create_text(500, 315, text=f"Вы пытались попасть {clicks_count} раз(-а), а смогли {score} раз(-а) - это {round((score / clicks_count) * 100)}%", justify=tk.CENTER, fill="white", font=("Consolas", 20, "bold")))

    menu_objects.append(c.create_text(500, 500, text="E - Сыграть еще раз\nQ - Выйти", justify=tk.CENTER, fill="white", font=("Arial", 40, "bold")))


game_over = False
def update_duration():
    current_left_time = round(music_data.music_data[current_song]['duration']-(time.time()-start))
    c.itemconfigure(duration_text, text=current_left_time if current_left_time >= 0 else 0)
    if current_left_time < -2:
        global game_over
        game_over = True
        show_game_end_window()
    else:
        window.after(1000, update_duration)

def game_loop():
    create_arrow()
    move_arrows()

    if not game_over:
        window.after(10, game_loop)


starting = True
menu_objects = []
def start_game():
    menu_objects.append(c.create_rectangle(0, 0, 1000, 700, fill="black"))
    menu_objects.append(c.create_text(500, 100, text="Rhythm Rampage", justify=tk.CENTER, fill="white", font=("Comic Sans MS", 80, "bold")))
    menu_objects.append(c.create_text(500, 350, text="E - Начать игру\nQ - Выйти", justify=tk.CENTER, fill="white", font=("Courier New", 50, "bold")))
    menu_objects.append(c.create_text(500, 600, text="Суть игры: следи за ритмом и двигай джойстиком!\nКак только бит окажется под линией подвинь джойстик в нужную сторону чтобы получить очки", fill="white", justify=tk.CENTER, font=("Consolas", 14, "bold")))


def on_close_window():
    for i in os.listdir("music/custom/"):
        os.remove("music/custom/"+i)
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close_window)
window.bind("<KeyPress>", key_press_handler)
start_game()
window.mainloop()

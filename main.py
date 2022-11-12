from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work = 0
timer = "None"

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, work, timer
    screen.after_cancel(timer)  # Stop the timer from counting
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
    flash_label.config(text="")
    reps = 0
    work = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def timer_mech():
    global reps
    reps += 1
    work_sec = WORK_MIN * 1
    break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work")
        count_down(work_sec)
    if reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(break_sec)
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global work, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = screen.after(1000, count_down, count - 1)
    else:
        timer_mech()
        if reps % 2 == 0:
            work += 1
            flash_label.config(text=f"✔" * work)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightbackground=YELLOW, command=timer_mech)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

flash_label = Label(text=f"", bg=YELLOW, fg=GREEN)
flash_label.grid(column=1, row=4)

# Displaying an image on the Tk screen and writing on the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
screen.mainloop()

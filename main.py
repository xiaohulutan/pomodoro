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
repo = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(clock)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    track.config(text="")
    global repo
    repo = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repo
    repo += 1
    if repo % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", fg=RED)
    elif repo % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", fg=YELLOW)
    else:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg="Black")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    elif count <= 0:
        start_timer()
        marks = ""
        working_session = math.floor(repo / 2)
        for _ in range(working_session):
            marks += "✔"
        track.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="White")
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg="Black", bg=GREEN)
timer.config(font=(FONT_NAME, 25, "bold"))
timer.grid(column=1, row=0)

track = Label(bg=GREEN, fg=RED)
track.grid(column=1, row=3)

start = Button(text="Start", bg=GREEN, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=GREEN, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

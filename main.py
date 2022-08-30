import math
from tkinter import *
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
marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    heading_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps < 9:
        if reps % 8 == 0:
            heading_label.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
        elif reps % 2 == 1:
            heading_label.config(text="Work", fg=GREEN)
            count_down(WORK_MIN * 60)
        elif reps % 2 == 0:
            heading_label.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 10)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global marks, timer
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(text_timer, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 1:
            marks += "✔"
        tick_label.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=50, pady=50)


canvas = Canvas(width=250, height=330, bg=YELLOW, highlightthickness=0)
canvas_img = PhotoImage(file="tomato.png")
canvas.create_image(120, 150, image=canvas_img)
text_timer = canvas.create_text(120, 170, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

heading_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
heading_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
start_button.config(command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=3)

tick_label = Label(bg=YELLOW, fg=RED)
tick_label.grid(column=1, row=3)


window.mainloop()

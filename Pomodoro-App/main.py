import tkinter as tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

def reset_timer():
    
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global REPS
    REPS = 0

def start_timer():
    
    global REPS
    REPS += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
        
def count_down(count):
    
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
        
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmarks.config(text=marks)
        
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file=r"Pomodoro-App\data\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
title = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55))
title.grid(column=1, row=0)

# Buttons
start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start.config(bd=0, bg=GREEN, fg="white", font=(FONT_NAME, 15), activeforeground="white")
start.grid(column=0, row=2)

reset = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.config(bd=0, bg=GREEN, fg="white", font=(FONT_NAME, 15), activeforeground="white")
reset.grid(column=2, row=2)

# Checkmarks
checkmarks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmarks.grid(column=1, row=3)

window.mainloop()


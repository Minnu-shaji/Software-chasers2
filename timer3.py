import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("400x400")
window.configure(bg="#FAFC97")

WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60
work_time, break_time = WORK_TIME, SHORT_BREAK_TIME
is_work_time, pomodoros_completed, is_running = True, 0, False

def start_timer():
    global is_running
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    is_running = True
    update_timer()

def stop_timer():
    global is_running
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    is_running = False

def update_timer():
    global is_running, work_time, break_time, is_work_time, pomodoros_completed
    if is_running:
        if is_work_time:
            work_time -= 1
            if work_time == 0:
                is_work_time = False
                pomodoros_completed += 1
                break_time = LONG_BREAK_TIME if pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                messagebox.showinfo(
                    "Great job!" if pomodoros_completed % 4 == 0 else "Good job!",
                    "Take a long break and rest your mind."
                    if pomodoros_completed % 4 == 0
                    else "Take a short break and stretch your legs!"
                )
                disp_label.config(text="Break Time!")
        else:
            break_time -= 1
            if break_time == 0:
                is_work_time, work_time = True, WORK_TIME
                messagebox.showinfo("Work Time", "Get back to work!")
                disp_label.config(text="Work Time!")
        minutes, seconds = divmod(work_time if is_work_time else break_time, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        window.after(1000, update_timer)

disp_label=tk.Label(window,text="Work Time!",bg="#FFFFE0",font=("Georgia",20))
disp_label.pack(pady=10)

timer_label = tk.Label(window, text="00:00", font=("Comic Sans MS", 40),bg="#FAFC97")
timer_label.pack(pady=20)

start_button = tk.Button(window, text="Start",bg="#FB97AE",fg="#FAFC97",width=8, font=("Comic Sans MS",12),command=start_timer)
start_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop",bg="#FB97AE",fg="#FAFC97",width=8, font=("Comic Sans MS",12), command=stop_timer, state=tk.DISABLED)
stop_button.pack(pady=5)

window.mainloop()

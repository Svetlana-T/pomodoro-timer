from tkinter import *
from time import sleep

win = Tk()
win.title("Pomodoro Timer")
win.iconbitmap("icon.ico")

win.geometry("300x140")

label = Label(win, text="25:00", font=("Helvetica bold", 40))
label.pack()


def timer():
    if button["text"] == "Start":
        button["text"] = "Reset"
        seconds = 1500
        while seconds >= 0:
            label['text'] = str(int(seconds / 60)) + ":" + str(seconds % 60)
            sleep(1)
            seconds -= 1
    else:
        label["text"] = "25:00"
        button["text"] = "Start"


button = Button(win, text="Start", font=("Helvetica bold", 20), command=timer)
button.pack()

frame = Frame(win)

frame.pack()
win.mainloop()

#Copyright 2021   Andrew John Roy Stephenson 
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from tkinter import *
from time import sleep
from playsound import playsound
import _thread

win = Tk()
win.title("Pomodoro Timer")
win.iconbitmap("icon.ico")

win.geometry("300x140")

label = Label(win, text="25:00", font=("Helvetica bold", 40))
label.pack()

started = False


def timer():
    global started
    started = True
    if button["text"] == "Start":
        button["text"] = "Reset"
        seconds = 1500
        while seconds >= 0 and started:
            label["text"] = str(int(seconds / 60)) + ":" + ("0" + str(seconds % 60) if seconds % 60 < 10 else
                                                            str(seconds % 60))
            if seconds == 0:
                playsound("zapsplat_bells_bell_small_hand_ring_ping_single_soft_003_67992.mp3")
            sleep(1)
            seconds -= 1


def start():
    global started
    if not started:
        _thread.start_new_thread(timer, ())
    else:
        started = False
        button["text"] = "Start"
        label["text"] = "25:00"


button = Button(win, text="Start", font=("Helvetica bold", 20), command=start)
button.pack()

frame = Frame(win)

frame.pack()
win.mainloop()

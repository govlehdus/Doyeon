import tkinter
import random

colors = ['red','orange','yellow','green','blue','purple','white','black']
score = 0

timeleft = 30

def start_Game(event):
    if timeleft == 30:
        count_down()

    next_color()

def next_color():
    global score
    global timeleft

    if timeleft > 0 :

        e.focus_set()

        if e.get().lower() == colors[1].lower():
            score +=1

        e.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg = str(colors[1]), text = str(colors[0]))
        scoreLabel.config(text = "Score: " + str(score))

def count_down():
    global timeleft
    if timeleft > 0:
        timeleft -=1

        timeLabel.config(text = "Time left: " + str(timeleft))

        timeLabel.after(1000, count_down)

root = tkinter.Tk()
root.title("Color Game")
root.geometry("380x200")

instruction = tkinter.Label(root, text = "Type in the color"
                            "Of the words, not the word text",
                            font = ("Helvetica", 12))
instruction.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start",
                           font =  ("Helvetica", 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " +
                          str(timeleft), font =  ("Helvetica", 12))
timeLabel.pack()

label = tkinter.Label(root, font = ("Helvetica", 60))
label.pack()

e = tkinter.Entry(root)

root.bind("<Return>", start_Game)

e.pack()
e.focus_set()
root.mainloop()
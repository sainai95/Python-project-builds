from Tkinter import *

master = Tk()
master.configure(bg='black')
master.wm_attributes("-topmost", 1)

w = Canvas(master, width=150, height=40, bd=0,relief='ridge',)
w.pack()

color = 100
x0 = 2
y0 = 2
x1 = 151
y1 = 2

while y0 < 20 :
    r = color
    g = color
    b = color
    rgb = r, g, b
    Hex = '#%02x%02x%02x' % rgb
    w.create_line(x0, y0, x1, y1,fill=str(Hex), width=1)
    color = color - 2
    y0 = y0 + 1
    y1 = y1 + 1

color = 10

while y0 < 40 :
    r = color
    g = color
    b = color
    rgb = r, g, b
    Hex = '#%02x%02x%02x' % rgb
    w.create_line(x0, y0, x1, y1,fill=str(Hex), width=1)
    color = color + 4
    y0 = y0 + 1
    y1 = y1 + 1

w.mainloop()
import tkinter
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()

def krizik(sur):
    x=sur.x
    y=sur.y
    canvas.create_line(x-30,y-30,x+30,y+30,width=5)
    canvas.create_line(x+30,y-30,x-30,y+30,width=5)   
canvas.bind('<Button-1>',krizik)

canvas.mainloop()
from tkinter import *

root = Tk()
root.title("Ayan's Calculator")
root.geometry("633x433")
root.wm_iconbitmap("Calculator_30001.ico")
root.config(background = "grey")


def click(event):
    global screenvar
    text = event.widget.cget("text")
    if(text == "="):
        if screenvar.get().isdigit():
            value = int(screenvar.get())
        else:
           try:
               value = eval(screenvar.get())
           except Exception as e:
               print(e)
               screenvar.set("Error")
               display.update()
        screenvar.set(value)
        display.update()
    elif(text == "Del"):
        val = screenvar.get()
        l = list(val)
        l.pop()
        val = "".join(l)
        screenvar.set(val)
    elif(text == "C"):
        screenvar.set("")
        display.update()
    else:
        screenvar.set(screenvar.get()+text)
        display.update()

screenvar = StringVar()
screenvar.set("")
display = Entry(root , textvar = screenvar, font="Helvetica 25 bold")
display.pack(ipady =15 ,padx = 5,pady = 10,fill = "x")

f1 = Frame(root , background = "sky blue")
f1.pack(side = LEFT, anchor = "n", ipadx = 45)


but9 = Button(f1, text = "9", padx = 20,pady = 10, font = "lucida 20 bold")
but9.grid(row = 0, column = 0, padx = 5, pady = 5)
but9.bind("<Button-1>", click)
but8 = Button(f1, text = "8", padx = 20,pady = 10, font = "lucida 20 bold")
but8.grid(row = 0, column = 1, padx = 5, pady = 5)
but8.bind("<Button-1>", click)
but7 = Button(f1, text = "7", padx = 20,pady = 10, font = "lucida 20 bold")
but7.grid(row = 0, column = 2, padx = 5, pady = 5)
but7.bind("<Button-1>", click)
but6 = Button(f1, text = "6", padx = 20,pady = 10, font = "lucida 20 bold")
but6.grid(row = 1, column = 0, padx = 5, pady = 5)
but6.bind("<Button-1>", click)
but5 = Button(f1, text = "5", padx = 20,pady = 10, font = "lucida 20 bold")
but5.grid(row = 1, column = 1, padx = 5, pady = 5)
but5.bind("<Button-1>", click)
but4 = Button(f1,text = "4", padx = 20,pady = 10, font = "lucida 20 bold")
but4.grid(row = 1, column = 2, padx = 5, pady = 5)
but4.bind("<Button-1>", click)
but3 = Button(f1, text = "3", padx = 20,pady = 10, font = "lucida 20 bold")
but3.grid(row = 2, column = 0, padx = 5, pady = 5)
but3.bind("<Button-1>", click)
but2 = Button(f1, text = "2", padx = 20,pady = 10, font = "lucida 20 bold")
but2.grid(row = 2, column = 1, padx = 5, pady = 5)
but2.bind("<Button-1>", click)
but1 = Button(f1,text = "1", padx = 20,pady = 10, font = "lucida 20 bold")
but1.grid(row = 2, column = 2, padx = 5, pady = 5)
but1.bind("<Button-1>", click)
but0 = Button(f1,text = "0", padx = 20,pady = 10, font = "lucida 20 bold")
but0.grid(row = 3, column = 1, padx = 5, pady = 5)
but17 = Button(f1, text = ".", padx = 20,pady = 10, font = "lucida 20 bold")
but17.grid(row = 3, column = 0, padx = 5, pady = 5)
but17.bind("<Button-1>", click)
but16 = Button(f1, text = "=", padx = 20,pady = 10, font = "lucida 20 bold")
but16.grid(row = 3, column = 2, padx = 5, pady = 5)
but16.bind("<Button-1>", click)
but0.bind("<Button-1>", click)


f2 = Frame(root , background = "blue")
f2.pack(side=RIGHT)
but18 = Button(f2, text = "Del", padx = 12,pady = 10, font = "lucida 20 bold")
but18.grid(row = 0, column = 0, padx = 5, pady = 5)
but18.bind("<Button-1>", click)
but10 = Button(f2, text = "C", padx = 20,pady = 10, font = "lucida 20 bold")
but10.grid(row = 0, column = 1, padx = 5, pady = 5)
but10.bind("<Button-1>", click)
but11 = Button(f2, text = "+", padx = 20,pady = 10, font = "lucida 20 bold")
but11.grid(row = 1, column = 0, padx = 5, pady = 5)
but11.bind("<Button-1>", click)
but12 = Button(f2, text = "-", padx = 20,pady = 10, font = "lucida 20 bold")
but12.grid(row = 1 ,column = 1, padx = 5, pady = 5)
but12.bind("<Button-1>", click)
but13 = Button(f2, text = "*", padx = 20,pady = 10, font = "lucida 20 bold")
but13.grid(row = 2, column = 0, padx = 5, pady = 5)
but13.bind("<Button-1>", click)
but14 = Button(f2, text = "/", padx = 20,pady = 10, font = "lucida 20 bold")
but14.grid(row = 2, column = 1, padx = 5, pady = 5)
but14.bind("<Button-1>", click)
but15 = Button(f2, text = "%", padx = 20,pady = 10, font = "lucida 20 bold")
but15.grid(row = 3, column = 0, padx = 5, pady = 5)
but15.bind("<Button-1>", click)
but16 = Button(f2, text = "=", padx = 20, pady = 10, font = "lucida 20 bold")
but16.grid(row = 0, column = 2, padx = 5, pady = 5)
but16.bind("<Button-1>", click)
but19 = Button(f2, text = "**",padx = 20,pady = 10, font = "lucida 20 bold")
but19.grid(row = 3, column = 1, padx = 5, pady = 5)
but19.bind("<Button-1>", click)
but20 = Button(f2, text = "(", padx = 20,pady = 10, font = "lucida 20 bold")
but20.grid(row = 2, column = 2, padx = 5, pady = 5)
but20.bind("<Button-1>", click)
but21 = Button(f2, text = ")", padx = 20,pady = 10, font = "lucida 20 bold")
but21.grid(row = 3, column = 2, padx = 5, pady = 5)
but21.bind("<Button-1>", click)

root.mainloop()

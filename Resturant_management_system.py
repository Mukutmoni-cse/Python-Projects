from tkinter import *
import time
from tkinter import font


system = Tk()

system.title("Resturant management system")
system.geometry("960x720")

head = Label(system,text = "Resturant management system", fg="blue",bg="yellow")
head.config(font=('Helvatical bold',20))
head.pack(fill=X, pady=10, padx=10, ipady=10)
localtime = time.asctime(time.localtime(time.time()))
time = Label(system,font=('arial',20,'bold'),text=localtime)
time.pack(fill=X, ipadx=10)


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


def cal(event):
    global refvar,strvar,vegvar,fishvar,chikvar,mutvar,drinksvar,totvar,gstvar,tot1var
    text = event.widget.cget("text")
    if(text=="Calculate"):
        Meal = (strvar.get()*20)+(vegvar.get()*40)+(fishvar.get()*50)+(chikvar.get()*60)+(mutvar.get()*70)+(drinksvar.get()*15)+(eggvar.get()*45)
        gst = (0.05*Meal)
        total = Meal+gst
        totvar.set(Meal)
        totentry.update()
        gstvar.set(gst)
        gstentry.update()
        tot1var.set(total)
        tot1entry.update()
    elif(text == "Reset"):
        drinksvar.set("0")
        drinksentry.update()
        refvar.set("")
        Refentry.update()
        vegvar.set("0")
        vegentry.update()
        eggvar.set("0")
        eggentry.update()
        chikvar.set("0")
        chikentry.update()
        mutvar.set("0")
        mutentry.update()
        strvar.set("0")
        strentry.update()
        totvar.set("0")
        totentry.update()
        gstvar.set("0")
        gstentry.update()
        tot1var.set("0")
        tot1entry.update()
        fishvar.set("0")
        fishentry.update()



f1 = Frame(system)
f1.pack(side = LEFT, anchor = "n", ipadx = 45,pady=20)
Reference = Label(f1, text="Reference : ",font="20")
Reference.grid(row=0, column=0,padx=20)
refvar = IntVar()
refvar.set("")
Refentry = Entry(f1, textvariable=refvar)
Refentry.grid(row=0, column=1)

starter = Label(f1, text="Starters(20) : ",font="20")
starter.grid(row=1,column=0, padx=20,pady=10)
strvar = IntVar()
strentry = Entry(f1, textvariable=strvar)
strentry.grid(row=1,column=1,padx=20)

veg = Label(f1, text="Veg meal(40) : ",font="20")
veg.grid(row=2,column=0, padx=20,pady=10)
vegvar = IntVar()
vegentry = Entry(f1, textvariable=vegvar)
vegentry.grid(row=2,column=1,padx=20)

egg = Label(f1, text="Egg meal(45) : ",font="20")
egg.grid(row=3,column=0, padx=20,pady=10)
eggvar = IntVar()
eggentry = Entry(f1, textvariable=eggvar)
eggentry.grid(row=3,column=1,padx=20)


fish = Label(f1, text="Fish meal(50) : ",font="20")
fish.grid(row=4,column=0, padx=20,pady=10)
fishvar = IntVar()
fishentry = Entry(f1, textvariable=fishvar)
fishentry.grid(row=4,column=1,padx=20)

chik = Label(f1, text="Chicken meal(60) : ",font="20")
chik.grid(row=5,column=0, padx=20,pady=10)
chikvar = IntVar()
chikentry = Entry(f1, textvariable=chikvar)
chikentry.grid(row=5,column=1,padx=20)

mut = Label(f1, text="Mutton meal(70) : ",font="20")
mut.grid(row=6,column=0, padx=20,pady=10)
mutvar = IntVar()
mutentry = Entry(f1, textvariable=mutvar)
mutentry.grid(row=6,column=1,padx=20)

drinks = Label(f1, text="Drinks(15) : ",font="20")
drinks.grid(row=7,column=0, padx=20,pady=10)
drinksvar = IntVar()
drinksentry = Entry(f1, textvariable=drinksvar)
drinksentry.grid(row=7,column=1,padx=20)



tot = Label(f1, text="Cost of meal : ",font="20")
tot.grid(row=8,column=0, padx=20,pady=10)
totvar = IntVar()
totentry = Entry(f1, textvariable=totvar,state=DISABLED)
totentry.grid(row=8,column=1,padx=20)

gst = Label(f1, text="Tax(GST 5%) : ",font="20")
gst.grid(row=9,column=0, padx=20,pady=10)
gstvar = IntVar()
gstentry = Entry(f1, textvariable=gstvar,state=DISABLED)
gstentry.grid(row=9,column=1,padx=20)

tot1 = Label(f1, text="Total cost : ",font="20")
tot1.grid(row=10,column=0, padx=20,pady=10)
tot1var = IntVar()
tot1entry = Entry(f1, textvariable=tot1var,state=DISABLED)
tot1entry.grid(row=10,column=1,padx=20)

button1 = Button(f1, text = "Calculate",bg="skyblue")
button1.grid(row=11, column=0,padx=20,pady=10, ipadx=30,ipady=10)
button1.bind("<Button-1>", cal)
button2 = Button(f1, text = "Reset",bg="skyblue")
button2.grid(row=11, column=1,padx=20,pady=10, ipadx=30,ipady=10)
button2.bind("<Button-1>", cal)




f2 = Frame(system , background = "sky blue",relief=SUNKEN)
f2.pack(side = RIGHT, anchor="n",pady=40)
but9 = Button(f2, text = "9", padx = 20,pady = 10, font = "lucida 20 bold")
but9.grid(row = 1, column = 0, padx = 5, pady = 5)
but9.bind("<Button-1>", click)
but8 = Button(f2, text = "8", padx = 20,pady = 10, font = "lucida 20 bold")
but8.grid(row = 1, column = 1, padx = 5, pady = 5)
but8.bind("<Button-1>", click)
but7 = Button(f2, text = "7", padx = 20,pady = 10, font = "lucida 20 bold")
but7.grid(row = 1, column = 2, padx = 5, pady = 5)
but7.bind("<Button-1>", click)
but6 = Button(f2, text = "6", padx = 20,pady = 10, font = "lucida 20 bold")
but6.grid(row = 2, column = 0, padx = 5, pady = 5)
but6.bind("<Button-1>", click)
but5 = Button(f2, text = "5", padx = 20,pady = 10, font = "lucida 20 bold")
but5.grid(row = 2, column = 1, padx = 5, pady = 5)
but5.bind("<Button-1>", click)
but4 = Button(f2,text = "4", padx = 20,pady = 10, font = "lucida 20 bold")
but4.grid(row = 2, column = 2, padx = 5, pady = 5)
but4.bind("<Button-1>", click)
but3 = Button(f2, text = "3", padx = 20,pady = 10, font = "lucida 20 bold")
but3.grid(row = 3, column = 0, padx = 5, pady = 5)
but3.bind("<Button-1>", click)
but2 = Button(f2, text = "2", padx = 20,pady = 10, font = "lucida 20 bold")
but2.grid(row = 3, column = 1, padx = 5, pady = 5)
but2.bind("<Button-1>", click)
but1 = Button(f2,text = "1", padx = 20,pady = 10, font = "lucida 20 bold")
but1.grid(row = 3, column = 2, padx = 5, pady = 5)
but1.bind("<Button-1>", click)
but0 = Button(f2,text = "0", padx = 20,pady = 10, font = "lucida 20 bold")
but0.grid(row = 4, column = 1, padx = 5, pady = 5)
but17 = Button(f2, text = ".", padx = 20,pady = 10, font = "lucida 20 bold")
but17.grid(row = 4, column = 4, padx = 5, pady = 5)
but17.bind("<Button-1>", click)
but16 = Button(f2, text = "=", padx = 20,pady = 10, font = "lucida 20 bold")
but16.grid(row = 4, column = 3, padx = 5, pady = 5)
but16.bind("<Button-1>", click)
but0.bind("<Button-1>", click)
but18 = Button(f2, text = "Del", padx = 10,pady = 10, font = "lucida 20 bold")
but18.grid(row = 1, column = 4, padx = 5, pady = 5)
but18.bind("<Button-1>", click)
but10 = Button(f2, text = "C", padx = 20,pady = 10, font = "lucida 20 bold")
but10.grid(row = 1, column = 3, padx = 5, pady = 5)
but10.bind("<Button-1>", click)
but11 = Button(f2, text = "+", padx = 20,pady = 10, font = "lucida 20 bold")
but11.grid(row = 2, column = 3, padx = 5, pady = 5)
but11.bind("<Button-1>", click)
but12 = Button(f2, text = "-", padx = 20,pady = 10, font = "lucida 20 bold")
but12.grid(row = 2 ,column = 4, padx = 5, pady = 5)
but12.bind("<Button-1>", click)
but13 = Button(f2, text = "*", padx = 20,pady = 10, font = "lucida 20 bold")
but13.grid(row = 3, column = 3, padx = 5, pady = 5)
but13.bind("<Button-1>", click)
but14 = Button(f2, text = "/", padx = 20,pady = 10, font = "lucida 20 bold")
but14.grid(row = 3, column = 4, padx = 5, pady = 5)
but14.bind("<Button-1>", click)

screenvar = StringVar()
screenvar.set("")
display = Entry(f2, textvar = screenvar, font="Helvetica 25 bold")
display.grid(row=0,columnspan=9,ipady=10)

system.resizable(0,0)
system.mainloop()
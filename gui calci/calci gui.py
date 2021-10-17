from tkinter import *
root=Tk()

root.geometry("644x644")
root.title("CALCULATOR")
#root.configure(background="black")

def func(event):
    global value
    text=event.widget.cget("text")
    if text=="=":
        if value.get().isdigit():
            val=int(value.get())
        else:
            try:
                val=eval(Screen.get())
            except Exception as e:
                val="Error"
                print(e)
        value.set(val)
        Screen.update()
    elif text=="AC":
        value.set("")
        Screen.update()

    else:
        value.set(value.get()+text)
        Screen.update()

value=StringVar()
value.set("")
#importan(Dont forget it)
Screen=Entry(root,textvariable=value,borderwidth=20,font=("lucida",20,"bold"),bg="white")
Screen.pack(fill=X,padx=12,pady=20)

f1=Frame(root)
b1=Button(f1,text='9',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b1.pack(side=LEFT,padx=30)
b1.bind("<Button-1>",func)

b2=Button(f1,text='8',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b2.pack(side=LEFT,padx=30)
b2.bind("<Button-1>",func)

b3=Button(f1,text='7',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b3.pack(side=LEFT,padx=30)
b3.bind("<Button-1>",func)

b4=Button(f1,text="AC",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b4.pack(side=LEFT,padx=30)
b4.bind("<Button-1>",func)
f1.pack(fill=X)

f2=Frame(root)
b5=Button(f2,text='6',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b5.pack(side=LEFT,padx=30)
b5.bind("<Button-1>",func)

b6=Button(f2,text='5',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b6.pack(side=LEFT,padx=30)
b6.bind("<Button-1>",func)

b7=Button(f2,text='4',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b7.pack(side=LEFT,padx=30)
b7.bind("<Button-1>",func)

b8=Button(f2,text="+",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b8.pack(side=LEFT,padx=30)
b8.bind("<Button-1>",func)
f2.pack(fill=X)

f3=Frame(root)
b9=Button(f3,text='3',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b9.pack(side=LEFT,padx=30)
b9.bind("<Button-1>",func)

b10=Button(f3,text='2',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b10.pack(side=LEFT,padx=30)
b10.bind("<Button-1>",func)

b11=Button(f3,text='1',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b11.pack(side=LEFT,padx=30)
b11.bind("<Button-1>",func)

b12=Button(f3,text="-",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b12.pack(side=LEFT,padx=30)
b12.bind("<Button-1>",func)
f3.pack(fill=X)

f4=Frame(root)
b13=Button(f4,text='0',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b13.pack(side=LEFT,padx=30)
b13.bind("<Button-1>",func)

b14=Button(f4,text='00',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b14.pack(side=LEFT,padx=30)
b14.bind("<Button-1>",func)

b15=Button(f4,text='*',bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b15.pack(side=LEFT,padx=30)
b15.bind("<Button-1>",func)

b16=Button(f4,text="/",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b16.pack(side=LEFT,padx=30)
b16.bind("<Button-1>",func)
f4.pack(fill=X)

f5=Frame(root)
b17=Button(f5,text=".",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b17.pack(side=LEFT,padx=30)
b17.bind("<Button-1>",func)

b18=Button(f5,text="%",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b18.pack(side=LEFT,padx=30)
b18.bind("<Button-1>",func)



b19=Button(f5,text="=",bg="orange",fg="brown",borderwidth=10,relief=SUNKEN,padx=20,pady=20,font="lucida 15 bold")
b19.pack(side=LEFT,padx=30)
b19.bind("<Button-1>",func)

f5.pack(fill=X)

root.mainloop()
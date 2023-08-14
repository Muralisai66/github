import tkinter
from tkinter import *

method=Tk()
method.title("Calculator")
method.geometry("570x600+100+5")
method.resizable(False,False)
method.configure(bg="ivory")


equation=""

def display(val):
    global equation
    equation+=val
    result.config(text=equation)

def clear():
    global equation
    equation+=""
    result.config(text=equation)



def calculate():
    global equation
    resul1=""
    if equation!="":
        try:
            resul1=eval(equation)
        except:
            resul1="error"
            equation=""
    result.config(text=resul1)

result=Label(method,width=25,height=2,text="",font=("arial",30))
result.pack()

Button(method,text="c",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(method,text="/",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("/")).place(x=150,y=100)
Button(method,text="%",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("%")).place(x=290,y=100)
Button(method,text="*",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("*")).place(x=430,y=100)

Button(method,text="7",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("7")).place(x=10,y=200)
Button(method,text="8",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("8")).place(x=150,y=200)
Button(method,text="9",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("9")).place(x=290,y=200)
Button(method,text="-",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("-")).place(x=430,y=200)


Button(method,text="4",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("4")).place(x=10,y=300)
Button(method,text="5",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("5")).place(x=150,y=300)
Button(method,text="6",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("6")).place(x=290,y=300)
Button(method,text="+",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("+")).place(x=430,y=300)

Button(method,text="1",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("1")).place(x=10,y=400)
Button(method,text="2",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("2")).place(x=150,y=400)
Button(method,text="3",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("3")).place(x=290,y=400)
Button(method,text="0",width=11,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("0")).place(x=10,y=500)

Button(method,text=".",width=5,height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: display(".")).place(x=290,y=500)
Button(method,text="=",width=5,height=3,font=("arial",30,"bold"), bd=1,fg="#fff",bg="yellow",command=lambda: calculate()).place(x=430,y=410)

method.mainloop()

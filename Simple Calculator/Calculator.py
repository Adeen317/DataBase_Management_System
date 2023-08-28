from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("570x580+200+100")
root.resizable(False,False)
root.configure(bg="grey15")

#Functionality Part

equation=""
def off():
    root.destroy()

def show(value):
    global equation
    equation+=value
    heading.config(text=equation)

def clear():
    global equation
    equation=""
    heading.config(text=equation)

def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result = str(eval(equation))
            
        except:
            result = "Error"
            equation = ""
    heading.config(text=result)

#GUI
heading=Label(root,width=25,height=2,text='',font=('Times new roman',30,'bold'))
heading.pack()

Button(root,text='AC',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='skyblue4',fg='Black',cursor='hand2',activeforeground='black',command=lambda: clear()).place(x=10,y=130)

Button(root,text='(',width=5,height=1,font=('arial',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("(")).place(x=150,y=130)

Button(root,text=')',width=5,height=1,font=('arial',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show(")")).place(x=290,y=130)

Button(root,text='/',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("/")).place(x=430,y=130)

Button(root,text='7',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("7")).place(x=10,y=220)

Button(root,text='8',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("8")).place(x=150,y=220)

Button(root,text='9',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("9")).place(x=290,y=220)

Button(root,text='X',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("*")).place(x=430,y=220)

Button(root,text='4',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("4")).place(x=10,y=310)

Button(root,text='5',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("5")).place(x=150,y=310)

Button(root,text='6',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("6")).place(x=290,y=310)

Button(root,text='-',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("-")).place(x=430,y=310)

Button(root,text='1',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("1")).place(x=10,y=400)

Button(root,text='2',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("2")).place(x=150,y=400)

Button(root,text='3',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("3")).place(x=290,y=400)

Button(root,text='+',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("+")).place(x=430,y=400)

Button(root,text='0',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show("0")).place(x=10,y=490)

Button(root,text='.',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='black',fg='white',cursor='hand2',activeforeground='black',command=lambda: show(".")).place(x=150,y=490)

Button(root,text='OFF',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='red4',fg='white',cursor='hand2',activeforeground='black',command=lambda: off()).place(x=290,y=490)

Button(root,text='=',width=5,height=1,font=('Times new roman',30,'bold'),
              bg='orange3',fg='black',cursor='hand2',activeforeground='black',command=lambda: calculate()).place(x=430,y=490)


root.mainloop()

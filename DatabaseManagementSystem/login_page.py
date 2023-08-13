from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql
#Functionality Part


def clear():
    email.delete(0,END)
    password.delete(0,END)


    
def on_enter(event):
    if email.get()=='Email Address':
        email.delete(0,END)

def on_enter1(event):
    if password.get()=='Password':
        password.delete(0,END)        
        

def login_user():
    if email.get()=='' or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=sql.connect(host='localhost',user='root',password='*****')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established Try Again')
            return
        
        query='use userdata1'
        mycursor.execute(query)
        query='select * from data where email=%s and password=%s'
        mycursor.execute(query,(email.get(),password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid email or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            clear()
            root.destroy()
            import GUIMAIN
        
def sign_in():
    root.destroy()
    import GUIMAIN

def newaccount():
    root.destroy()
    import registration
    

    
def hide():
    password.config(show='*')
    button1.config(command=show)

def show():
     password.config(show='')
     button1.config(command=hide)

def forget_pass():
    root.destroy()
    import reset_password

    
#GUI Part
root=Tk()
root.resizable()
root.geometry('1920x1080+50+50')
root.title('Login')
bgImage=ImageTk.PhotoImage(file='bglogin1.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(root,width=20,text='Sign In',font=('Bodoni MT Black',23),
              bd=0,bg='DeepPink3',fg='White')
heading.place(x=10,y=30)


heading1=Label(root,text='Email Address',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading1.place(x=30,y=85)



email=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
email.place(x=30,y=110)
email.insert(0,'Email Address')

email.bind('<FocusIn>',on_enter)

Frame1=Frame(root,width=354,height=1,bg='Black')
Frame1.place(x=30,y=135)

heading2=Label(root,text='Password',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading2.place(x=30,y=155)


password=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
password.place(x=30,y=180)
password.insert(0,'Password')

password.bind('<FocusIn>',on_enter1)

Frame2=Frame(root,width=354,height=1,bg='Black')
Frame2.place(x=30,y=205)

button1=Button(root,text='Show',font=('Times New Roman',10,'bold'),
               bd=0,bg='Lightgrey',fg='Black',cursor='hand2',
               command=hide,activeforeground='Lightgrey')
button1.place(x=345,y=182)


forget=Button(root,text='Forget Login Details?',font=('Times New Roman',10),
               bd=0,bg='White',fg='Black',cursor='hand2',
               activeforeground='white',command=forget_pass)
forget.place(x=30,y=210)


sign=Button(root,width=12,text='Login',font=('Times New Roman',12,'bold'),
               bd=0,bg='Purple',fg='white',cursor='hand2',
               activeforeground='purple',command=login_user)
sign.place(x=270,y=210)

bgImage1=ImageTk.PhotoImage(file='login 6.jpg')
bgLabel1=Label(root,image=bgImage1)
bgLabel1.place(x=30,y=250)

bgImage2=ImageTk.PhotoImage(file='login bg33.jpg')
bgLabel2=Button(root,image=bgImage2,bd=0,cursor='hand2')
bgLabel2.place(x=10,y=280)

bgImage3=ImageTk.PhotoImage(file='login bg4.jpg')
bgLabel3=Button(root,image=bgImage3,bd=0,cursor='hand2')
bgLabel3.place(x=230,y=280)

bgImage4=ImageTk.PhotoImage(file='login bg5.jpg')
bgLabel4=Button(root,image=bgImage4,bd=0,cursor='hand2')
bgLabel4.place(x=10,y=320)

noacc=Label(root,text='Do Not have an account?',font=('Times New Roman',9,'bold'),
               bd=0,bg='white',fg='black',cursor='hand2',
               activeforeground='white')
noacc.place(x=10,y=360)

#bgImage5=ImageTk.PhotoImage(file='Capture3.jpg')
#bgLabel5=Label(root,image=bgImage5,bd=0)
#bgLabel5.place(x=460,y=20)

newacc=Button(root,text='Create New One.',font=('Times New Roman',9,'bold'),
               bd=0,bg='white',fg='Darkblue',cursor='hand2',
               activeforeground='white',command=newaccount)
newacc.place(x=180,y=360)

Frame2=Frame(root,width=95,height=1,bg='Darkblue')
Frame2.place(x=180,y=378)


root.mainloop()


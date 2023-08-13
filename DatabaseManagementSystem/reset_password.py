from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql
#Functionality Part

def clear():
    email.delete(0,END)
    password.delete(0,END)
    repassword.delete(0,END)
    user.delete(0,END)

def on_enter1(event):
    if password.get()=='Password':
        password.delete(0,END)

def on_enter(event):
    if user.get()=='Enter Username':
        user.delete(0,END)

        
def on_enter2(event):
    if repassword.get()=='Confirm Password':
        repassword.delete(0,END)


def on_enter3(event):
    if email.get()=='Enter Email':
        email.delete(0,END)  
        
        
def go_to():
    root.destroy()
    import login_page

def back():
    root.destroy()
    import login_page

    
def hide():
    password.config(show='*')
    button1.config(command=show)

def hide1():
    repassword.config(show='*')
    button2.config(command=show1)

def show():
     password.config(show='')
     button1.config(command=hide)

def show1():
     repassword.config(show='')
     button2.config(command=hide1)

def connect_database():
    if password.get()=='' or user.get()=='' or  repassword.get()=='' or email.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif password.get() != repassword.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        con=sql.connect(host='localhost',user='root',password='',database='userdata1')
        mycursor=con.cursor()
        query='select * from data where username=%s and email=%s'
        mycursor.execute(query, (user.get(),email.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Username or Email')
        else:
            query='update data set password=%s where username=%s'
            mycursor.execute(query,(password.get(),user.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Successful','Password is Changed')
            clear()
            root.destroy()
            import login_page


        
#GUI Part
     
root=Tk()
root.resizable()
root.title('Reset Password')
bgImage=ImageTk.PhotoImage(file='pgb.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,width=20,text='Reset Password',font=('Bodoni MT Black',23),
              bd=0,bg='grey7',fg='White')
heading.place(x=10,y=30)


heading1=Label(root,text='Username',font=('Times New Roman',15,'bold'),
              bd=0,bg='grey7',fg='white')
heading1.place(x=30,y=85)



user=Entry(root,width=35,font=('Times New Roman',15),bg='grey7',fg='white')
user.place(x=30,y=110)
user.insert(0,'Enter Username')

user.bind('<FocusIn>',on_enter)

Frame1=Frame(root,width=354,height=1,bg='white')
Frame1.place(x=30,y=135)

heading5=Label(root,text='Email Address',font=('Times New Roman',15,'bold'),
              bd=0,bg='grey7',fg='white')
heading5.place(x=30,y=275)

email=Entry(root,width=35,font=('Times New Roman',15),bg='grey7',fg='white')
email.place(x=30,y=300)
email.insert(0,'Enter Email')

email.bind('<FocusIn>',on_enter3)

Frame5=Frame(root,width=354,height=1,bg='white')
Frame5.place(x=30,y=325)

heading2=Label(root,text='New Password',font=('Times New Roman',15,'bold'),
              bd=0,bg='grey7',fg='white')
heading2.place(x=30,y=155)


password=Entry(root,width=35,font=('Times New Roman',15),bg='grey7',fg='white')
password.place(x=30,y=180)
password.insert(0,'Password')

password.bind('<FocusIn>',on_enter1)

Frame2=Frame(root,width=354,height=1,bg='white')
Frame2.place(x=30,y=205)


button1=Button(root,text='Show',font=('Times New Roman',10,'bold'),
               bd=0,bg='grey7',fg='white',cursor='hand2',
               command=hide,activeforeground='Lightgrey')
button1.place(x=345,y=182)

heading3=Label(root,text='Confirm New Password',font=('Times New Roman',15,'bold'),
              bd=0,bg='grey7',fg='white')
heading3.place(x=30,y=215)

repassword=Entry(root,width=35,font=('Times New Roman',15),bg='grey7',fg='white')
repassword.place(x=30,y=240)
repassword.insert(0,'Confirm Password')

repassword.bind('<FocusIn>',on_enter2)

Frame3=Frame(root,width=354,height=1,bg='white')
Frame3.place(x=30,y=265)

button2=Button(root,text='Show',font=('Times New Roman',10,'bold'),
               bd=0,bg='grey7',fg='white',cursor='hand2',
               command=hide1,activeforeground='Lightgrey')
button2.place(x=345,y=242)


submit=Button(root,width=32,text='Submit',font=('Times New Roman',15,'bold'),
               bd=0,bg='Purple',fg='white',cursor='hand2',
               activeforeground='purple',command=connect_database)
submit.place(x=10,y=350)

back=Button(root,width=5,text='back',font=('Times New Roman',15,'bold'),
               bd=0,bg='grey7',fg='white',cursor='hand2',
               activeforeground='purple',command=back)
back.place(x=500,y=10)


root.mainloop()

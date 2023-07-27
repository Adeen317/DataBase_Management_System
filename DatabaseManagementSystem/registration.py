from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql
#Functionality Part

def clear():
    email.delete(0,END)
    password.delete(0,END)
    repassword.delete(0,END)
    name.delete(0,END)
    user.delete(0,END)
    check.set(0)

def on_enter(event):
    if email.get()=='Email Address':
        email.delete(0,END)

def on_enter1(event):
    if password.get()=='Password':
        password.delete(0,END)

def on_enter2(event):
    if repassword.get()=='Confirm Password':
        repassword.delete(0,END)

def on_enter3(event):
    if name.get()=='Enter Full Name':
        name.delete(0,END)

def on_enter4(event):
    if user.get()=='Enter Username':
        user.delete(0,END)  
        
        
def go_to():
    root.destroy()
    import login_page

def update_stat():
    root.destroy()
    import update_stat
    

    
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
    if email.get()=='' or name.get()=='' or password.get()=='' or user.get()=='' or  repassword.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif password.get() != repassword.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Condition')
    else:
        try:
            con=sql.connect(host='localhost',user='root',password='ayaan1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again.')
            return
        try:
            query='create database userdata1'
            mycursor.execute(query)
            query='use userdata1'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,Full_name varchar(50),email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata1')

        query='insert into data(Full_name,email,username,password)  values(%s,%s,%s,%s)'
        mycursor.execute(query,(name.get(),email.get(),user.get(),password.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Successful','Registration is Successful')
        clear()
        root.destroy()
        import login_page


        
#GUI Part
     
root=Tk()
root.resizable()
root.title('Registration')
bgImage=ImageTk.PhotoImage(file='wbg.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,width=20,text='Create An Account',font=('Bodoni MT Black',23),
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

heading4=Label(root,text='Enter Full Name',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading4.place(x=470,y=85)

name=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
name.place(x=470,y=110)
name.insert(0,'Enter Full Name')

name.bind('<FocusIn>',on_enter3)

Frame4=Frame(root,width=354,height=1,bg='Black')
Frame4.place(x=470,y=135)

heading2=Label(root,text='Password',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading2.place(x=30,y=155)


password=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
password.place(x=30,y=180)
password.insert(0,'Password')

password.bind('<FocusIn>',on_enter1)

Frame2=Frame(root,width=354,height=1,bg='Black')
Frame2.place(x=30,y=205)

heading5=Label(root,text='Username',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading5.place(x=470,y=155)

user=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
user.place(x=470,y=180)
user.insert(0,'Enter Username')

user.bind('<FocusIn>',on_enter4)

Frame5=Frame(root,width=354,height=1,bg='Black')
Frame5.place(x=470,y=205)

button1=Button(root,text='Show',font=('Times New Roman',10,'bold'),
               bd=0,bg='Lightgrey',fg='Black',cursor='hand2',
               command=hide,activeforeground='Lightgrey')
button1.place(x=345,y=182)

heading3=Label(root,text='Confirm Password',font=('Times New Roman',15,'bold'),
              bd=0,bg='White',fg='Black')
heading3.place(x=30,y=215)

repassword=Entry(root,width=35,font=('Times New Roman',15),bg='Lightgrey',fg='Black')
repassword.place(x=30,y=240)
repassword.insert(0,'Confirm Password')

repassword.bind('<FocusIn>',on_enter2)

Frame3=Frame(root,width=354,height=1,bg='Black')
Frame3.place(x=30,y=265)

button2=Button(root,text='Show',font=('Times New Roman',10,'bold'),
               bd=0,bg='Lightgrey',fg='Black',cursor='hand2',
               command=hide1,activeforeground='Lightgrey')
button2.place(x=345,y=242)

check=IntVar()

terms=Checkbutton(text='I Agree to the Terms & Conditions',font=('Times New Roman',10),
               bd=0,bg='White smoke',fg='Black',pady=10,
                  cursor='hand2',variable=check)
terms.place(x=30,y=275)

#forget=Button(root,text='Forget Login Details?',font=('Times New Roman',10),
               #bd=0,bg='White smoke',fg='Black',cursor='hand2',
               #activeforeground='white')
#forget.place(x=30,y=250)


signup=Button(root,width=20,text='Sign Up',font=('Times New Roman',18,'bold'),
               bd=0,bg='Purple',fg='white',cursor='hand2',
               activeforeground='purple',command=connect_database)
signup.place(x=270,y=300)


noacc=Label(root,text='Already have an account?',font=('Times New Roman',9,'bold'),
               bd=0,bg='white smoke',fg='black')
noacc.place(x=10,y=360)

bgImage5=ImageTk.PhotoImage(file='Capture3.jpg')
bgLabel5=Label(root,image=bgImage5,bd=0)
bgLabel5.place(x=460,y=20)

newacc=Button(root,text='Go to Login Page.',font=('Times New Roman',9,'bold'),
               bd=0,bg='white smoke',fg='Darkblue',cursor='hand2',
               activeforeground='white',command=go_to)
newacc.place(x=180,y=360)

Frame2=Frame(root,width=95,height=1,bg='Darkblue')
Frame2.place(x=180,y=378)


root.mainloop()


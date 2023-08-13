from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql
from tkinter import ttk
import requests 
from PIL import Image
from io import BytesIO

#Functonality Part

def on_enter(event):
    if Task.get()=='Enter Task':
        Task.delete(0,END)

def on_enter1(event):
    if Deadline.get()=='Enter Deadline':
        Deadline.delete(0,END)

def on_enter2(event):
    if Time.get()=='Enter Time':
        Time.delete(0,END)

#Connection

def connect_database():
    if Task.get()=='' or Deadline.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    else:
        try:
            con=sql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again.')
            return
        try:
            query='create database todolist'
            mycursor.execute(query)
            query='use todolist'
            mycursor.execute(query)
            query='create table list(id int auto_increment primary key not null,Task varchar(50),Deadline varchar(50),Time varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use todolist')

        query='insert into list(Task,Deadline,Time)  values(%s,%s,%s)'
        mycursor.execute(query,(Task.get(),Deadline.get(),Time.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Task Added','Task is added')
        clear()
        root.close()

def markasdone():
    try:
        con=sql.connect(host='localhost',user='root',password='',database='todolist')
        mycursor=con.cursor()
    except:
        mycursor.execute('use todolist')

    if Task.get()=='':
        messagebox.showerror('Error','Enter Task')
    elif check.get()==0:
        messagebox.showerror('Cannot be updated','First Mark as done')
    else:
        query='delete from list where Task=%s'
        mycursor.execute(query,(Task.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Successfull','Task is completed')
        root.destroy()
        import To_do_List
        
        

def search():
    try:
        con=sql.connect(host='localhost',user='root',password='',database='todolist')
        mycursor=con.cursor()
        query='select * from list'
        mycursor.execute(query)
        rows=mycursor.fetchall()
        my_tag=my_tree.tag_configure("gray",foreground="white",background="black")
        for dt in rows:
            my_tree.insert("",'end',values=dt,tags=my_tag)
    except:
        messagebox.showerror('!!!!',' There is some error Please Try Again!!')


#Image Download
r=requests.get("https://wallpaperset.com/w/full/7/f/5/437958.jpg")

i = Image.open(BytesIO(r.content))
fp=open("img.jpg","wb")
i.save(fp)
fp.close()


#GUI
root=Tk()
root.geometry('800x350+50+50')
root.title('TO-DO-LIST')
bgImage=ImageTk.PhotoImage(file='img.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,text='TO-DO-LIST',font=('Bodoni MT Black',30,'bold'),
              bg='black',fg='white')
heading.place(x=210,y=10)


Task=Entry(root,width=20,font=('Times New Roman',13,'bold'),bg='Black',fg='White')
Task.place(x=610,y=150)
Task.insert(0,'Enter Task')

Task.bind('<FocusIn>',on_enter)

Frame1=Frame(root,width=185,height=2)
Frame1.place(x=610,y=170)

Deadline=Entry(root,width=20,font=('Times New Roman',13,'bold'),bg='Black',fg='White')
Deadline.place(x=610,y=190)
Deadline.insert(0,'Enter Deadline')

Deadline.bind('<FocusIn>',on_enter1)

Frame2=Frame(root,width=185,height=2)
Frame2.place(x=610,y=210)

Time=Entry(root,width=20,font=('Times New Roman',13,'bold'),bg='Black',fg='White')
Time.place(x=610,y=110)
Time.insert(0,'Enter Time')

Time.bind('<FocusIn>',on_enter2)

Frame1=Frame(root,width=185,height=2)
Frame1.place(x=610,y=130)

#Checkbutton
check=IntVar()
terms=Checkbutton(text='Mark As done',font=('Times New Roman',13),
               bd=0,bg='black',fg='white',pady=10,
                  cursor='hand2',variable=check,command=markasdone)
terms.place(x=610,y=230)

Frame3=Frame(root,width=125,height=2)
Frame3.place(x=610,y=270)


button4=Button(root,text='Add to the List',font=('Times New Roman',16,'bold'),
               bg='black',fg='white',cursor='hand2',
               activeforeground='black',command=connect_database)
button4.place(x=610,y=290)

Frame4=Frame(root,width=150,height=2)
Frame4.place(x=610,y=330)

button5=Button(root,text='Show All Task',font=('Times New Roman',16,'bold'),
               bg='black',fg='white',cursor='hand2',
               activeforeground='black',command=search)
button5.place(x=610,y=30)

Frame5=Frame(root,width=150,height=2)
Frame5.place(x=610,y=70)


#Table
my_tree=ttk.Treeview(root)
my_tree.place(x=-395,y=100,height=244,width=1000,relx=0.0000001)


my_tree.tag_configure("gray",foreground="white",background="black")
my_tag='gray'

my_tree.configure(
    columns=("id","Task","Deadline","Time(AM/PM)")
)

my_tree.heading("id",text="No.",anchor='w')
my_tree.heading("Task",text="Task",anchor='w')
my_tree.heading("Deadline",text="Deadline",anchor='w')
my_tree.heading("Time(AM/PM)",text="Time(AM/PM)",anchor='w')



root.mainloop()


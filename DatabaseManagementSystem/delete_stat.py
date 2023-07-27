from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql

#Functionality Part

def on_enter(event):
    if teamname.get()=='Enter Team Name':
        teamname.delete(0,END)

def on_e(event):
    if win.get()=='Wins':
        win.delete(0,END)

def on_en(event):
    if draw.get()=='Draws':
        draw.delete(0,END)
        

def on_ent(event):
    if lose.get()=='Lose':
        lose.delete(0,END)

def on_ente(event):
    if Goaldiff.get()=='GoalDiff':
        Goaldiff.delete(0,END)

def on(event):
    if pts.get()=='Points':
        pts.delete(0,END)

def o(event):
    if stan.get()=='MP':
        stan.delete(0,END)        
        
def insert():
    try:
        con=sql.connect(host='localhost',user='root',password='ayaan1234',database='userdata1')
        mycursor=con.cursor()
        query='create table league(MatchPlayed varchar(10) not null,Team_name varchar(30) primary key not null,win varchar(10) not null,draw varchar(10) not null,lose varchar not null,Goal_diff varchar(10) not null,points varchar(10) not null)'
        mycursor.execute(query)
    except:
        mycursor.execute('use userdata1')

    if teamname.get()=='' or stan.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        query='delete from league where Team_name=%s and MatchPlayed=%s'
        mycursor.execute(query,(teamname.get(),stan.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Successfull','Data is Deleted Successfully')

def back():
    root.destroy()
    import GUIMAIN

#GUI Part
root=Tk()
root.resizable()
root.geometry()
root.title('Update Stat')
bgImage=ImageTk.PhotoImage(file='bg12.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,text='DELETE',font=('Bodoni MT Black',30,'bold'),
              bg='Grey',fg='Black')
heading.place(x=100,y=10)

button1=Button(root,text='Delete Team Stats',font=('Times New Roman',15,'bold'),
               bg='Grey',fg='white',cursor='hand2',
               activeforeground='Black',command=insert)
button1.place(x=30,y=170)

button2=Button(root,text='BACK',font=('Times New Roman',15,'bold'),
               bg='Grey',fg='white',cursor='hand2',
               activeforeground='Black',command=back)
button2.place(x=600,y=10)

teamname=Entry(root,width=20,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
teamname.place(x=30,y=100)
teamname.insert(0,'Enter Team Name')

teamname.bind('<FocusIn>',on_enter)


stan=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
stan.place(x=30,y=130)
stan.insert(0,'MP')

stan.bind('<FocusIn>',o)


root.mainloop()




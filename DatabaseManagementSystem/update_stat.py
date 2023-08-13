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

def back():
    root.destroy()
    import GUIMAIN


def insert():
    try:
        con=sql.connect(host='localhost',user='root',password='',database='userdata1')
        mycursor=con.cursor()
        query='create table league(MatchPlayed varchar(10) not null,Team_name varchar(30) primary key not null,win varchar(10) not null,draw varchar(10) not null,lose varchar(15) not null,Goal_diff varchar(10) not null,points varchar(10) not null)'
        mycursor.execute(query)
    except:
        mycursor.execute('use userdata1')

    if teamname.get()=='' or win.get()=='' or draw.get()=='' or lose.get()=='' or Goaldiff.get()=='' or pts.get()=='' or stan.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        query='insert into league(MatchPlayed,Team_name,win,draw,lose,Goal_diff,points) values (%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(stan.get(),teamname.get(),win.get(),draw.get(),lose.get(),Goaldiff.get(),pts.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Successfull','Data is Entered Successfully')




#GUI Part
root=Tk()
root.resizable()
root.geometry()
root.title('Insert Stat')
bgImage=ImageTk.PhotoImage(file='bg1.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,text='Insert',font=('Bodoni MT Black',30,'bold'),
              bg='Grey',fg='Black')
heading.place(x=100,y=10)

button1=Button(root,text='Insert Team Stats',font=('Times New Roman',15,'bold'),
               bg='Grey',fg='white',cursor='hand2',
               activeforeground='Black',command=insert)
button1.place(x=200,y=250)

teamname=Entry(root,width=20,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
teamname.place(x=30,y=100)
teamname.insert(0,'Enter Team Name')

teamname.bind('<FocusIn>',on_enter)

button2=Button(root,text='BACK',font=('Times New Roman',15,'bold'),
               bg='Grey',fg='white',cursor='hand2',
               activeforeground='Black',command=back)
button2.place(x=580,y=10)

win=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
win.place(x=30,y=130)
win.insert(0,'Wins')

win.bind('<FocusIn>',on_e)

draw=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
draw.place(x=30,y=160)
draw.insert(0,'Draws')

draw.bind('<FocusIn>',on_en)

lose=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
lose.place(x=30,y=190)
lose.insert(0,'Lose')

lose.bind('<FocusIn>',on_ent)

Goaldiff=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
Goaldiff.place(x=30,y=220)
Goaldiff.insert(0,'GoalDiff')

Goaldiff.bind('<FocusIn>',on_ente)

pts=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
pts.place(x=30,y=250)
pts.insert(0,'Points')

pts.bind('<FocusIn>',on)

stan=Entry(root,width=8,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
stan.place(x=30,y=280)
stan.insert(0,'MP')

stan.bind('<FocusIn>',o)


root.mainloop()




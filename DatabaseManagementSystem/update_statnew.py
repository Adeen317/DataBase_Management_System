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
        if teamname.get()=="":
           messagebox.showerror("Error","please enter club")
        else:
            con=sql.connect(host="localhost",user="root",password="ayaan1234",database="userdata1")
            my_cursor=con.cursor()
            
            query='update league set win=%s,draw=%s,lose=%s,Goal_diff=%s,points=%s,MatchPlayed=%s where Team_name=%s'
            my_cursor.execute(query,(teamname.get(),win.get(),draw.get(),lose.get(),Goaldiff.get(),pts.get(),stan.get()))
            con.commit()  
            my_cursor.fetchall()
            con.close()         
            messagebox.showinfo("Update","League details has been updated successfully")
            import GUIMAIN



#GUI Part
root=Tk()
root.resizable()
root.geometry()
root.title('Update Stat')
bgImage=ImageTk.PhotoImage(file='bg1.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,text='Update',font=('Bodoni MT Black',30,'bold'),
              bg='Grey',fg='Black')
heading.place(x=100,y=10)

button1=Button(root,text='Update Team Stats',font=('Times New Roman',15,'bold'),
               bg='Grey',fg='white',cursor='hand2',
               activeforeground='Black',command=insert)
button1.place(x=200,y=250)

teamname=Entry(root,width=20,font=('Times New Roman',15,'bold'),bg='Grey',fg='White')
teamname.place(x=30,y=100)
teamname.insert(0,'Enter Team Name')

teamname.bind('<FocusIn>',on_enter)

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




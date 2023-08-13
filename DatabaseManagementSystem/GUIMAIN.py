from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as sql
from tkinter import ttk
#Functionality Part

#def on_enter(event):
     #if teamname.get()=='Enter Team Name':
        #teamname.delete(0,END)
        
def best_player():
    root.destroy()
    import BestPlayerStat

def update_stat():
    def on_en(event):
        if dell.get()=='':
            dell.delete(0,END)
    def login():
        if dell.get()=='9876':
            root.destroy()
            des.destroy()
            import update_stat
        else:
            messagebox.showerror('Error','Wrong Password')
            des.destroy()
        
    try:
        des=Tk()
        des.title('Admin Login')
        des.geometry('300x300+50+50')
        heading1=Label(des,text='ADMIN LOGIN',font=('Times New Roman',20,'bold'),
              bg='white',fg='black')
        heading1.place(x=50,y=10)
        heading=Label(des,text='Enter Password',font=('Times New Roman',15,'bold'),
              bg='white',fg='black')
        heading.place(x=70,y=70)
        dell=Entry(des,width=18,font=('Times New Roman',10,'bold'),text='*',bg='grey',fg='black')
        dell.place(x=70,y=100)
        dell.insert(0,'')
        dell.bind('<FocusIn>',on_en)
        dell.config(show='*')
        login=Button(des,text='Login',font=('Times New Roman',15,'bold'),
               bg='black',fg='white',cursor='hand2',
               activeforeground='white',command=login)
        login.place(x=75,y=150)
    except:
            messagebox.showerror('Error','Wrong Password')
            
    
def log_out():
    messagebox.showinfo('!!!!',' Are you sure you want to log out?')
    root.destroy()
    import login_page
    
def search():
    try:
        con=sql.connect(host='localhost',user='root',password='*****',database='******')
        mycursor=con.cursor()
        query='select * from league order by points desc'
        mycursor.execute(query)
        rows=mycursor.fetchall()
        my_tag=my_tree.tag_configure("gray",foreground="white",background="black")
        for dt in rows:
            my_tree.insert("",'end',values=dt,tags=my_tag)
    except:
        messagebox.showerror('!!!!',' There is some error Please Try Again!!')



def delete():
    def on_en(event):
        if dell.get()=='':
            dell.delete(0,END)
    def login():
        if dell.get()=='9876':
            root.destroy()
            des.destroy()
            import delete_stat
        else:
            messagebox.showerror('Error','Wrong Password')
            des.destroy()
        
    try:
        des=Tk()
        des.title('Admin Login')
        des.geometry('300x300+50+50')
        heading1=Label(des,text='ADMIN LOGIN',font=('Times New Roman',20,'bold'),
              bg='white',fg='black')
        heading1.place(x=50,y=10)
        heading=Label(des,text='Enter Password',font=('Times New Roman',15,'bold'),
              bg='white',fg='black')
        heading.place(x=70,y=70)
        dell=Entry(des,width=18,font=('Times New Roman',10,'bold'),text='*',bg='grey',fg='black')
        dell.place(x=70,y=100)
        dell.insert(0,'')
        dell.bind('<FocusIn>',on_en)
        dell.config(show='*')
        login=Button(des,text='Login',font=('Times New Roman',15,'bold'),
               bg='black',fg='white',cursor='hand2',
               activeforeground='white',command=login)
        login.place(x=75,y=150)
    except:
            messagebox.showerror('Error','Wrong Password')



def update():
    def on_en(event):
        if dell.get()=='':
            dell.delete(0,END)
    def login():
        if dell.get()=='9876':
            root.destroy()
            des.destroy()
            import update_statnew
        else:
            messagebox.showerror('Error','Wrong Password')
            des.destroy()
        
    try:
        des=Tk()
        des.title('Admin Login')
        des.geometry('300x300+50+50')

        heading1=Label(des,text='ADMIN LOGIN',font=('Times New Roman',20,'bold'),
              bg='white',fg='black')
        heading1.place(x=50,y=10)
        heading=Label(des,text='Enter Password',font=('Times New Roman',15,'bold'),
              bg='white',fg='black')
        heading.place(x=70,y=70)
        dell=Entry(des,width=18,font=('Times New Roman',10,'bold'),text='*',bg='grey',fg='black')
        dell.place(x=70,y=100)
        dell.insert(0,'')
        dell.bind('<FocusIn>',on_en)
        dell.config(show='*')
        login=Button(des,text='Login',font=('Times New Roman',15,'bold'),
               bg='black',fg='white',cursor='hand2',
               activeforeground='white',command=login)
        login.place(x=75,y=150)
    except:
            messagebox.showerror('Error','Wrong Password')

#GUI Part
root=Tk()
root.geometry('1920x700+50+50')
root.title('League')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(root,text='English Premier League',font=('Bodoni MT Black',30,'bold'),
              bg='darkOrchid4',fg='White')
heading.place(x=730,y=10)

#heading1=Label(root,text='Enter Team Name',font=('Times New Roman',15,'bold'),
              #bg='darkOrchid4',fg='White')
#heading1.place(x=1100,y=66)


#Frame3=Frame(root,width=160,height=2)
#Frame3.place(x=1100,y=90)


#teamname=Entry(root,width=25,font=('Times New Roman',15,'bold'),bg='DeepPink3',fg='White')
#teamname.place(x=1100,y=100)
#teamname.insert(0,'Enter Team Name')

#teamname.bind('<FocusIn>',on_enter)

#Frame1=Frame(root,width=254,height=2)
#Frame1.place(x=1100,y=130)

button1=Button(root,text='Search',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               command=search,activeforeground='white')
button1.place(x=800,y=200)

Frame4=Frame(root,width=75,height=2)
Frame4.place(x=800,y=242)

button2=Button(root,text='Top 5 Best Players',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               activeforeground='white',command=best_player)
button2.place(x=10,y=600)

button3=Button(root,text='Insert Stats',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               activeforeground='white',command=update_stat)
button3.place(x=650,y=200)

Frame2=Frame(root,width=176,height=2)
Frame2.place(x=10,y=692)

Frame3=Frame(root,width=116,height=2)
Frame3.place(x=650,y=242)

button4=Button(root,text='Delete Stats',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               activeforeground='white',command=delete)
button4.place(x=900,y=200)

Frame3=Frame(root,width=120,height=2)
Frame3.place(x=900,y=242)

button4=Button(root,text='Update Stats',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               activeforeground='white',command=update)
button4.place(x=1050,y=200)

Frame3=Frame(root,width=126,height=2)
Frame3.place(x=1050,y=242)


my_tree=ttk.Treeview(root)
my_tree.place(x=-180,y=250,height=344,width=1550,relx=0.0001)


my_tree.tag_configure("gray",foreground="white",background="black")
my_tag='gray'

my_tree.configure(
    columns=("MatchPlayed","Team_name","win","draw","lose","Goal_diff","points")
)

my_tree.heading("MatchPlayed",text="MP",anchor='w')
my_tree.heading("Team_name",text="CLUB",anchor='w')
my_tree.heading("win",text="WIN",anchor='w')
my_tree.heading("draw",text="DRAW",anchor='w')
my_tree.heading("lose",text="LOSE",anchor='w')
my_tree.heading("Goal_diff",text="GD",anchor='w')
my_tree.heading("points",text="Pts",anchor='w')


button3=Button(root,text='Log Out',font=('Times New Roman',15,'bold'),
               bg='DeepPink3',fg='White',cursor='hand2',
               activeforeground='white',command=log_out)
button3.place(x=1180,y=600)

Frame3=Frame(root,width=86,height=2)
Frame3.place(x=1100,y=692)

root.mainloop()


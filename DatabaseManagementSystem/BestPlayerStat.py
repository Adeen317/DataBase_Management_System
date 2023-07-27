from tkinter import *
from PIL import ImageTk
#Functionality Part

def back():
    root.destroy()
    import GUIMAIN

#GUI Part
root=Tk()
root.resizable()
root.geometry()
root.title('Best Players')
bgImage=ImageTk.PhotoImage(file='bglogin.png')

bgLabel=Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

#heading=Label(root,text='BEST 5',font=('Bodoni MT Black',30,'bold'),
              #bg='DarkSeaGreen1',fg='Black')
#heading.place(x=100,y=10)

#heading1=Label(root,text='GOALS',font=('Bodoni MT Black',15,'bold'),
              #bg='DarkSeaGreen1',fg='Black')
#heading1.place(x=150,y=80)

bgImage1=ImageTk.PhotoImage(file='goals.jpg')

bgLabel1=Label(root,image=bgImage1)
bgLabel1.place(x=150,y=10)


bgImage2=ImageTk.PhotoImage(file='assist.jpg')

bgLabel2=Label(root,image=bgImage2)
bgLabel2.place(x=150,y=400)

submit=Button(root,text='Go Back',font=('Times New Roman',15,'bold'),
               bd=0,bg='grey7',fg='white',cursor='hand2',
               activeforeground='grey7',command=back)
submit.place(x=10,y=20)


heading2=Label(root,text='ASSISTS',font=('Bodoni MT Black',15,'bold'),
              bg='grey7',fg='white')
heading2.place(x=150,y=370)
root.mainloop()



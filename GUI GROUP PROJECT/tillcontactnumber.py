from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
class Register:
        def __init__(self,root):
            self.root=root
            self.root.title("Student Registration Form")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="teal")
            # BG IMAGE #

            self.bg=ImageTk.PhotoImage(file="images/stcet.png")#this bg is object of class
            bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)#this bg is object of root window

            # LEFT IMAGE COLLEGE LOGO #

            self.left=ImageTk.PhotoImage(file="images/1.png")
            left=Label(self.root,image=self.left).place(x=80,y=100,width=280,height=360)

            #  REGISTRATION FRAME #
            frame1=Frame(self.root,bg="white")    #we are making the frame in the root window
            frame1.place(x=360,y=100,width=700,height=360)

            title=Label(frame1,text="PLEASE ENTER YOUR DETAILS HERE",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=5)
            # STUDENT NAME #
            
            name=Label(frame1,text="NAME  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=10,y=50)
            # making the entry field #
            txt_name=Entry(frame1,font=("verdana",10),bg="lightgray").place(x=150,y=50)

            # PARENT'S NAME #

            fname=Label(frame1,text="FATHER'S NAME  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=10,y=70)
            txt_fname=Entry(frame1,font=("verdana",10),bg="lightgray").place(x=150,y=70)
            mname=Label(frame1,text="MOTHER'S NAME  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=320,y=70)
            txt_mname=Entry(frame1,font=("verdana",10),bg="lightgray").place(x=460,y=70)

            # MAIL ID #

            mail=Label(frame1,text="EMAIL ID  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=10,y=90)
            txt_mail=Entry(frame1,font=("verdana",10),bg="lightgray").place(x=150,y=90)

            # SEX #
            sex=Label(frame1,text="SEX  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=10,y=110)
            # RADIOBUTTON #
            rad1=Radiobutton(frame1,text="MALE",value=1)
            rad2=Radiobutton(frame1,text="FEMALE",value=2)

            rad1.place(x="150",y=110)
            rad2.place(x="230",y=110)

            # CONTACT NUMBER #
            num=Label(frame1,text="PHONE NUMBER  ",font=("verdana",10,"bold"),bg="white",fg="black").place(x=10,y=130)
            txt_num=Entry(frame1,font=("verdana",10),bg="lightgray").place(x=150,y=130)
            



root=Tk()
obj=Register(root)
root.mainloop()

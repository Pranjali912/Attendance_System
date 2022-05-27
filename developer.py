from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1630x750+0+0")
        self.root.title("face recognition system")

        title_lbl= Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top= Image.open(r"C:\Users\pc\Documents\web development\face recognition\images\developer1.jpg")
        img_top = img_top.resize((1500,650),Image.ANTIALIAS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl= Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1500,height=650)
        #----frame--------

        main_frame= Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=200)

        img_top1= Image.open(r"C:\Users\pc\Documents\web development\face recognition\images\developer3.png")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1= ImageTk.PhotoImage(img_top1)

        f_lbl= Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)
     #-----developer info------
        dev_label= Label(main_frame,text="Hello,I am Pranjali",font =("times new roman",16,"bold"))
        dev_label.place(x=0,y=5)

        dev_label= Label(main_frame,text="I am a 2nd year Btech Student",font =("times new roman",16,"bold"))
        dev_label.place(x=0,y=40)
        dev_label= Label(main_frame,text="Hope you liked this project",font =("times new roman",16,"bold"))
        dev_label.place(x=0,y=80)

        

























if __name__ =="__main__":
   root=Tk()
   obj=Developer(root)
   root.mainloop()        
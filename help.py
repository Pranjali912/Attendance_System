from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1630x750+0+0")
        self.root.title("face recognition system")

        title_lbl= Label(self.root,text="HEPL DESK",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top= Image.open(r"C:\Users\pc\Documents\web development\face recognition\images\help5.jpg")
        img_top = img_top.resize((1500,650),Image.ANTIALIAS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl= Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=650)
        

        dev_label= Label(f_lbl,text="Need Help!!",font =("times new roman",30,"bold"),bg="black",fg="white")
        dev_label.place(x=100,y=100)
        

        dev_label= Label(f_lbl,text=" Contact via Email : pranjalipriya001@gmail.com",font =("times new roman",20,"bold"),bg="black",fg="white")
        dev_label.place(x=100,y=200)










if __name__ =="__main__":
   root=Tk()
   obj=Help(root)
   root.mainloop()
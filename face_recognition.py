from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1630x750+0+0")
        self.root.title("face recognition system")



        title_lbl= Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #--------first img-----
        img_top= Image.open(r"C:\Users\pc\Documents\web development\face recognition\images\img1.jpg")
        img_top = img_top.resize((650,680),Image.ANTIALIAS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl= Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=680)

   #--------2nd img-------
        img_bottom= Image.open(r"C:\Users\pc\Documents\web development\face recognition\images\face_recog.jpg")
        img_bottom = img_bottom.resize((850,680),Image.ANTIALIAS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        f_lbl= Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=850,height=680)

        b1_1=Button(f_lbl,text="Face Recognize",cursor="hand2",command=self.face_recog,font=("times new roman",17,"bold"),bg="green",fg="white")
        b1_1.place(x=335,y=550,width=200,height=30)


    #----------attendance------------

    def mark_attedance(self,i,r,n,d):
        with open("record.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and  (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

             





    #-----------face recognition------------
    def face_recog(self):
      def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
          gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
          features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

          coord=[]

          for (x,y,w,h) in features:
               cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
               id,predict = clf.predict(gray_image[y:y+h,x:x+w])
               confidence= int((100*(1-predict/300)))

               conn= mysql.connector.connect(host="localhost",username="root",password="#pranjali_data1",database="face_recognition")
               my_cursor=conn.cursor()

               my_cursor.execute("Select Name from student where Student_id="+str(id))
               n=my_cursor.fetchone()
               n=str(n)
               n="+".join(n)

               my_cursor.execute("Select Roll from student where Student_id="+str(id))
               r=my_cursor.fetchone()
               r=str(r)
               r="+".join(r)

               my_cursor.execute("Select Dep from student where Student_id="+str(id))
               d=my_cursor.fetchone()
               d=str(d)
               d="+".join(d)

               my_cursor.execute("Select Student_id from student where Student_id="+str(id))
               i=my_cursor.fetchone()
               i=str(i)
               i="+".join(i)

               if confidence>60:
                   cv2.putText(img,f"ID:{str(i)}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                   cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                   cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                   cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                   self.mark_attedance(i,r,n,d)
   
               else:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                   cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            
               coord=[x,y,w,h]


          return coord
         
      def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

      faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      clf= cv2.face.LBPHFaceRecognizer_create()
      clf.read("classifier.xml")
      video_cap= cv2.VideoCapture(0)


      while True:
             ret,img=video_cap.read()
             img = recognize(img,clf,faceCascade)
             cv2.imshow("Welcome To face Recognition",img)

             if cv2.waitKey(1)==13:
                 break
                
      video_cap.release()
      cv2.destroyAllWindows()


             





if __name__ =="__main__":
   root=Tk()
   obj=Face_Recognition(root)
   root.mainloop()         
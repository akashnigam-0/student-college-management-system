from lib2to3.pytree import LeafPattern
from operator import imod
import sqlite3
import re
from datetime import *
import time
from math import *
from tkinter import*
import os
from turtle import title, width
from PIL import Image,ImageTk, ImageDraw 
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
from tkinter.tix import Tree


class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")
        #=== ICONS ===
        self.logo_desh=ImageTk.PhotoImage(file="images/logo_p.png")
        #=== TITLE ===
        title= Label(self.root,text="Student Result Management System",padx=14,compound=LEFT,image=self.logo_desh,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=60)
        #=== MENU ===
        M_Frame = LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1270,height=80)
        #=== BUTTONS ===
        btn_course= Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=150,height=40)
        btn_student= Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=200,y=5,width=150,height=40)
        btn_result= Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=380,y=5,width=150,height=40)
        btn_view = Button(M_Frame,text="View Students Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=560,y=5,width=300,height=40)
        btn_logout= Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=160,height=40)
        btn_exit = Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1090,y=5,width=150,height=40)

        #=== content_windows ===
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg= Label(self.root,image=self.bg_img).place(x=400,y=180,width=880,height=350)
        #==Update_details===
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=545,width=280,height=100)
        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=700,y=545,width=280,height=100)
        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1000,y=545,width=280,height=100)
        
        #====== CLOCK=====
        self.lbl= Label(self.root,text="\nTime",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#0B1923",bd=0)
        self.lbl.place(x=10,y=200,height=430,width=350)
        
        self.working()

        #=== FOOTER ===
        footer= Label(self.root,text="SRMS - Student Result Management System",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.Update_details()
    #======================================================
    def Update_details(self):
        con= sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            
            
            
            self.lbl_course.after(200,self.Update_details)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to update {str(ex)}")


    def working(self):
        h= datetime.now().time().hour
        m= datetime.now().time().minute
        s= datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec_)
        self.clock_image(hr, min_, sec_)
        self.img= ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw= ImageDraw.Draw(clock)

        # === For Clock Image
        bg = Image.open("images\c.png")
        # bg= bg.resize((300,300),Image.ANTIALIAS)
        bg= bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))
        #==Hour Line Image===
        #       x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #==Min Line Image===
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #==Sec Line Image===
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("clock_new.png")

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op == True:
            self.root.destroy()
            



if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
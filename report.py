# from lib2to3.pytree import LeafPattern
# from multiprocessing import parent_process
# from os import stat
# import re
# from socket import VMADDR_CID_HOST
from tkinter import*
from tkinter.tix import Tree
from turtle import heading, title, width
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

         #=== TITLE ===
        title= Label(self.root,text="View Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
        #==== Search====
        self.var_search= StringVar()
        self.var_id=""
        lb1_search = Label(self.root,text="Search by Roll No",font=("goudy old style",15,'bold'),bg="white").place(x=280,y=100)
        txt_search = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow").place(x=500,y=100,width=155)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="grey",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=30)

        #==== result Labels =============
        lb1_roll = Label(self.root,text="Roll No",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=140,height=50)
        lb1_name = Label(self.root,text="Name",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=290,y=230,width=140,height=50)
        lb1_course = Label(self.root,text="Course",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=430,y=230,width=140,height=50)
        lb1_marks = Label(self.root,text="Marks Obtained",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=570,y=230,width=160,height=50)
        lb1_full = Label(self.root,text="Total Marks",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=730,y=230,width=150,height=50)
        lb1_per = Label(self.root,text="Percentage",font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE).place(x=880,y=230,width=150,height=50)

        self.roll = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=140,height=50)
        self.name = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=290,y=280,width=140,height=50)
        self.course = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=430,y=280,width=140,height=50)
        self.marks = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=570,y=280,width=160,height=50)
        self.full = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=730,y=280,width=150,height=50)
        self.per = Label(self.root,font=("Arial",15,'bold'),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=880,y=280,width=150,height=50)

        #==== Button delete ==========
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=500,y=380,width=150,height=30)

    #======================================

    def search(self):
        con= sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll no. Should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:  
                    messagebox.showerror("Error","no record found",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con= sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student result",parent=self.root)
                else:
                    op = messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to detete {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()
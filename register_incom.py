from tkinter import *
from tkinter import font
from turtle import title, width
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1300x600+0+0")
        self.root.config(bg="white")

        #=== Bg Images =====
        self.bg= ImageTk.PhotoImage(file="images/b2.jpg")
        bg= Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #===Left Image=========
        self.left= ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #======= Register Frame=============
        frame1= Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title= Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #   ROW 1
        # self.var_fname= StringVar()
        f_name= Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name= Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=370,y=130,width=250)

        #-----------------

        contact= Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)

        email= Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)

        #----- row 3------
        question= Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmd_quest= ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)
        self.cmd_quest['values']=("Select","Your First Pet Name","Your birth place")
        self.cmd_quest.place(x=50,y=270,width=250)
        self.cmd_quest.current(0)

        answer= Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_answer.place(x=370,y=270,width=250)

        #------------------

        password= Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_password.place(x=50,y=340,width=250)
        cpassword= Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword= Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #---- TERMS ----------
        self.var_chk=IntVar()
        chk= Checkbutton(frame1,text="I agree the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        self.btn_img= ImageTk.PhotoImage(file="images/register.png")
        btn_register = Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login = Button(self.root,text="Sign in",font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=480,width=160)

    #===========
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields are reequired",parent=self.root)
        elif self.txt_password.get() !=  self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password didn't match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please accept T&C",parent=self.root)
        else:
            try:

            except Exception as es:
                messagebox.showinfo("Success","Registration Successful",parent= self.root)


        

root=Tk()
obj=Register(root)
root.mainloop()
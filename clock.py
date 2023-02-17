from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1200x650+10+10")
        self.root.config(bg="#021e2f")

        title= Label(self.root,text="Ankur Ananlog Clock",font=("times new roman",50,"bold"),bg="#04444e",fg="white").place(x=0,y=50,relwidth=1)

        self.lbl= Label(self.root,bg="white",bd=10,relief=RAISED)
        self.lbl.place(x=400,y=170,height=400,width=400)
        # self.clock_image()
        self.working()

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw= ImageDraw.Draw(clock)

        # === For Clock Image
        bg = Image.open("images\cl.jpg")
        # bg= bg.resize((300,300),Image.ANTIALIAS)
        bg= bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))
        #==Hour Line Image===
        #       x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        #==Min Line Image===
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        #==Sec Line Image===
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")

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
        



root = Tk()
obj=Clock(root)
root.mainloop()
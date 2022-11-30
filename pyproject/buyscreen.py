# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:35:31 2022

@author: ritu
"""
from tkinter import *
from tkinter import *

def make_item():
    st=""
    def tag_screen():
     root1=Tk() 
     s=StringVar(root1) 
     c=StringVar(root1)  
     
     def click1():
        nonlocal entry
        nonlocal s
        nonlocal c
        nonlocal st
        st+=str(s.get())+","
        c.set(st)
        entry.delete(0,END)
     def click2():
        nonlocal tgs
        tgs.set(st)
        root1.destroy()     
     root1.title("Tags")
     root1.geometry("400x200")
     info=Label(root1,text="Enter tags that describe your product:",bg="red",fg="white",bd="5")
     info.pack()
     entry=Entry(root1,textvariable=s,bg="red",fg="white",bd="5")
     entry.pack()
     btn=Button(root1,text="Enter",bg="red",fg="white",bd="5",command=click1)
     btn.pack() 
     disp=Label(root1,textvariable=c,bg="red",fg="white",bd="5")
     disp.pack()
     over=Button(root1,text="Done",bg="red",fg="white",bd="5",command=click2)
     over.pack()
     root1.mainloop()    
     
    root=Tk()
    root.title("New Item")
    root.geometry("600x600")
    name=StringVar(root)
    price=StringVar(root)
    tgs=StringVar(root)
    inamreq=Label(text="Enter name of item")
    inamreq.pack()
    inam=Entry(textvariable=name)
    inam.pack()
    pricereq=Label(text="Enter price of item")
    pricereq.pack()
    price=Entry(textvariable=price)
    price.pack()
    tags=Button(text="add tags",command=tag_screen)
    tags.pack()
    tgsdisp=Label(textvariable=tgs)
    tgsdisp.pack()
    over=Button(text="Done",command=root.destroy)
    over.pack()
    root.mainloop()
make_item()


    

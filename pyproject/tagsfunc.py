# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 19:58:43 2022

@author: ritu
"""
from tkinter import *
def tag_screen():
    st=""
    root=Tk() 
    s=StringVar(root) 
    c=StringVar(root)
    def click():
        nonlocal s
        nonlocal c
        nonlocal st
        st+=str(s.get())+","
        c.set(st)
    root.title("Tags")
    root.geometry("400x200")
    info=Label(text="Enter tags that describe your product:",bg="red",fg="white",bd="5")
    info.pack()
    entry=Entry(textvariable=s,bg="red",fg="white",bd="5")
    entry.pack()
    btn=Button(text="Enter",bg="red",fg="white",bd="5",command=click)
    btn.pack() 
    disp=Label(textvariable=c,bg="red",fg="white",bd="5")
    disp.pack()
    over=Button(text="Done",bg="red",fg="white",bd="5",command=root.destroy)
    over.pack()
    root.mainloop()
tag_screen()

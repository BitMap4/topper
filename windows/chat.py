# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:00:27 2022

@author: STUDENT
"""
import tkinter as tk
import tkinter.font as tkFont

# palette
bg_primary = "#36393f"
bg_secondary = "#202225"
accent = "#f7b163"
text_primary = "#eeeeee"

root = tk.Tk()

#setting title
root.title("undefined")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.configure(background=bg_primary)
root.tk_setPalette(background=bg_primary)

Textbox=tk.Entry(root)
Textbox["borderwidth"] = "0px"
ft = tkFont.Font(family='Times',size=10)
Textbox["bg"] = bg_secondary
Textbox["font"] = ft
Textbox["fg"] = "#333333"
Textbox["justify"] = "left"
Textbox["text"] = "Entry"
Textbox.place(x=10,y=450,width=530,height=40)

Send_btn=tk.Button(root)
Send_btn["bg"] = "#f0f0f0"
Send_btn["borderwidth"] = "0px"
ft = tkFont.Font(family='Times',size=10)
Send_btn["font"] = ft
Send_btn["fg"] = "#000000"
Send_btn["justify"] = "center"
Send_btn["text"] = "Send"
Send_btn["relief"] = "flat"
Send_btn.place(x=550,y=450,width=40,height=40)

'''
GLabel_753=tk.Label(root)
GLabel_753["bg"] = "#393d49"
ft = tkFont.Font(family='Times',size=10)
GLabel_753["font"] = ft
GLabel_753["fg"] = "#333333"
GLabel_753["justify"] = "center"
GLabel_753["text"] = "label"
GLabel_753.place(x=10,y=60,width=40,height=40)

GLabel_842=tk.Label(root)
ft = tkFont.Font(family='Times',size=13)
GLabel_842["font"] = ft
GLabel_842["fg"] = "#333333"
GLabel_842["justify"] = "left"
GLabel_842["text"] = "User 1"
GLabel_842.place(x=60,y=60,width=520,height=25)

GLabel_554=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_554["font"] = ft
GLabel_554["fg"] = "#333333"
GLabel_554["justify"] = "left"
GLabel_554["text"] = "message content here"
GLabel_554.place(x=60,y=80,width=520,height=25)
'''

Navbar=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Navbar["font"] = ft
Navbar["bg"] = accent
Navbar["fg"] = "#333333"
Navbar["justify"] = "center"
Navbar["text"] = ""
Navbar.place(x=0,y=0,width=100,height=50)

Pfp_img=tk.Label(root)
Pfp_img["bg"] = "#393d49"
ft = tkFont.Font(family='Times',size=10)
Pfp_img["font"] = ft
Pfp_img["fg"] = "#333333"
Pfp_img["justify"] = "center"
Pfp_img["text"] = "label"
Pfp_img.place(x=550,y=5,width=40,height=40)

Signout=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Signout["font"] = ft
Signout["bg"] = accent
Signout["fg"] = "#333333"
Signout["justify"] = "right"
Signout["text"] = "Sign Out"
Signout.place(x=470,y=20,width=70,height=25)

User_username=tk.Label(root)
ft = tkFont.Font(family='Times',size=13)
User_username["font"] = ft
User_username["bg"] = accent
User_username["fg"] = "#333333"
User_username["justify"] = "right"
User_username["text"] = "User 1"
User_username.place(x=470,y=5,width=70,height=25)

Logo_link=tk.Label(root)
ft = tkFont.Font(family='Times',size=13)
Logo_link["font"] = ft
Logo_link["fg"] = "#333333"
Logo_link["bg"] = accent
Logo_link["justify"] = "left"
Logo_link["text"] = "Link"
Logo_link.place(x=10,y=10,width=70,height=25)

root.mainloop()
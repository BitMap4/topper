from tkinter import *

w=Tk()
w.geometry('3000x5000')
w.configure(bg="#141414")
def bttn1(x,y,text,bcolor,fcolor,):
    
    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
        
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor
        
    def openNewWindow1():
             newWindow = Toplevel(w)
             newWindow.title("New Window")
             newWindow.geometry("200x200")
             Label(newWindow,text ="BUYER WINDOW").pack()
     
    
    mybutton=Button(w,width=42,height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=openNewWindow1 ,)
    
    mybutton.bind(",<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)
    
    mybutton.place(x=x,y=y)

bttn1(0,0,"B U Y E R","#ffcc66","#141414")



def bttn2(x,y,text,bcolor,fcolor,):
    
    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
        
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor
        
    def openNewWindow2():
             newWindow = Toplevel(w)
             newWindow.title("New Window")
             newWindow.geometry("200x200")
             Label(newWindow,text ="SELLER WINDOW").pack()
     
    
    mybutton=Button(w,width=42,height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=openNewWindow2,)
    
    mybutton.bind(",<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)
    
    mybutton.place(x=x,y=y)
    
bttn2(0,37,"S E L L E R","#25dae9","#141414")


w.mainloop()

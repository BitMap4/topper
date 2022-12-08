from signup import *
from backbone import *
# palette
bg_primary = "#36393f"
bg_secondary = "#202225"
accent = "#f7b163"
text_primary = "#eeeeee"
    
def loginWin(tk, tkFont):
    def signup():
        login.destroy()
        signupWin(tk, tkFont)
    
    # create login window
    login = tk.Tk()

    # login window title and dimension
    #setting title
    login.title("Log In")
    #setting window size
    width=600
    height=500
    login['bg']=bg_primary
    screenwidth = login.winfo_screenwidth()
    screenheight = login.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    login.geometry(alignstr)
    login.resizable(width=False, height=False)
    login.tk_setPalette(background=bg_primary, foreground=text_primary)


    Heading=tk.Label(login)
    ft = tkFont.Font(size=30)
    Heading["font"] = ft
    Heading["fg"] = accent
    Heading["text"] = "Welcome back"
    Heading["relief"] = "flat"
    Heading.place(x=175,y=50,width=240,height=50)

    Username_label=tk.Label(login)
    ft = tkFont.Font(size=13)
    Username_label["font"] = ft
    Username_label["fg"] = text_primary
    Username_label["anchor"] = "w"
    Username_label["text"] = "Username"
    Username_label["borderwidth"] = '0px'
    Username_label.place(x=100,y=120,width=120,height=50)

    Pwd_label=tk.Label(login)
    ft = tkFont.Font(size=13)
    Pwd_label["font"] = ft
    Pwd_label["fg"] = text_primary
    Pwd_label["anchor"] = "w"
    Pwd_label["text"] = "Password"
    Pwd_label["borderwidth"] = '0px'
    Pwd_label.place(x=100,y=200,width=120,height=50)

    Username_input=tk.Entry(login)
    Username_input["bg"] = bg_secondary
    Username_input["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Username_input["font"] = ft
    Username_input["fg"] = "#aaaaaa"
    Username_input["justify"] = "left"
    Username_input.place(x=100,y=160,width=400,height=40)

    Pwd_input=tk.Entry(login)
    Pwd_input["bg"] = bg_secondary
    Pwd_input["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Pwd_input["font"] = ft
    Pwd_input["fg"] = "#aaaaaa"
    Pwd_input["justify"] = "left"
    Pwd_input["text"] = ""
    Pwd_input["relief"] = "flat"
    Pwd_input.place(x=100,y=240,width=400,height=40)
    Pwd_input["show"] = "•"

    Login_btn=tk.Button(login)
    Login_btn["bg"] = accent
    Login_btn["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Login_btn["font"] = ft
    Login_btn["bg"] = accent
    Login_btn["fg"] = text_primary
    Login_btn["justify"] = "center"
    Login_btn["text"] = "Log In"
    Login_btn["relief"] = "flat"
    Login_btn.place(x=100,y=310,width=400,height=40)

    Signup_label=tk.Label(login)
    ft = tkFont.Font(size=10)
    Signup_label["font"] = ft
    Signup_label["fg"] = text_primary
    Signup_label["justify"] = "left"
    Signup_label["text"] = "Don't have an account?"
    Signup_label.place(x=100,y=355,width=140,height=25)

    Signup_btn=tk.Button(login, command = signup)
    Signup_btn["borderwidth"] = "0px"
    ft = tkFont.Font(size=10)
    Signup_btn["font"] = ft
    Signup_btn["bg"] = bg_primary
    Signup_btn["fg"] = accent
    Signup_btn["anchor"] = "w"
    Signup_btn["text"] = "Sign up"
    Signup_btn.place(x=233,y=356,width=70,height=25)


    # Execute Tkinter
    login.mainloop()

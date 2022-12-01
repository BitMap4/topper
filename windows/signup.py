from login import *

# palette
bg_primary = "#36393f"
bg_secondary = "#202225"
accent = "#f7b163"
text_primary = "#eeeeee"

def signupWin(tk, tkFont):
    def login():
        signup.destroy()
        loginWin(tk, tkFont)
    
    # create signup window
    signup = tk.Tk()

    # signup window title and dimension
    #setting title
    signup.title("Sign Up")
    #setting window size
    width=600
    height=500
    signup['bg']=bg_primary
    screenwidth = signup.winfo_screenwidth()
    screenheight = signup.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    signup.geometry(alignstr)
    signup.resizable(width=False, height=False)
    signup.tk_setPalette(background=bg_primary, foreground=text_primary)


    Heading=tk.Label(signup)
    ft = tkFont.Font(size=30)
    Heading["font"] = ft
    Heading["fg"] = accent
    Heading["text"] = "Create a new account"
    Heading["relief"] = "flat"
    Heading.place(x=150,y=50,width=300,height=50)
    
    Name_label=tk.Label(signup)
    ft = tkFont.Font(size=13)
    Name_label["font"] = ft
    Name_label["fg"] = text_primary
    Name_label["anchor"] = "w"
    Name_label["text"] = "Name"
    Name_label["borderwidth"] = '0px'
    Name_label.place(x=100,y=120,width=120,height=50)

    Username_label=tk.Label(signup)
    ft = tkFont.Font(size=13)
    Username_label["font"] = ft
    Username_label["fg"] = text_primary
    Username_label["anchor"] = "w"
    Username_label["text"] = "Username"
    Username_label["borderwidth"] = '0px'
    Username_label.place(x=100,y=200,width=120,height=50)

    Pwd_label=tk.Label(signup)
    ft = tkFont.Font(size=13)
    Pwd_label["font"] = ft
    Pwd_label["fg"] = text_primary
    Pwd_label["anchor"] = "w"
    Pwd_label["text"] = "Password"
    Pwd_label["borderwidth"] = '0px'
    Pwd_label.place(x=100,y=280,width=120,height=50)
    
    Name_input=tk.Entry(signup)
    Name_input["bg"] = bg_secondary
    Name_input["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Name_input["font"] = ft
    Name_input["fg"] = "#aaaaaa"
    Name_input["justify"] = "left"
    Name_input.place(x=100,y=160,width=400,height=40)

    Username_input=tk.Entry(signup)
    Username_input["bg"] = bg_secondary
    Username_input["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Username_input["font"] = ft
    Username_input["fg"] = "#aaaaaa"
    Username_input["justify"] = "left"
    Username_input.place(x=100,y=240,width=400,height=40)

    Pwd_input=tk.Entry(signup)
    Pwd_input["bg"] = bg_secondary
    Pwd_input["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Pwd_input["font"] = ft
    Pwd_input["fg"] = "#aaaaaa"
    Pwd_input["justify"] = "left"
    Pwd_input["text"] = ""
    Pwd_input["relief"] = "flat"
    Pwd_input.place(x=100,y=320,width=400,height=40)
    Pwd_input["show"] = "•"

    Signup_btn=tk.Button(signup)
    Signup_btn["bg"] = accent
    Signup_btn["borderwidth"] = "0px"
    ft = tkFont.Font(size=13)
    Signup_btn["font"] = ft
    Signup_btn["bg"] = accent
    Signup_btn["fg"] = text_primary
    Signup_btn["justify"] = "center"
    Signup_btn["text"] = "Log In"
    Signup_btn["relief"] = "flat"
    Signup_btn.place(x=100,y=390,width=400,height=40)

    Login_label=tk.Label(signup)
    ft = tkFont.Font(size=10)
    Login_label["font"] = ft
    Login_label["fg"] = text_primary
    Login_label["justify"] = "left"
    Login_label["text"] = "Already have an account?"
    Login_label.place(x=100,y=435,width=140,height=25)

    Login_btn=tk.Button(signup, command = login)
    Login_btn["borderwidth"] = "0px"
    ft = tkFont.Font(size=10)
    Login_btn["font"] = ft
    Login_btn["bg"] = bg_primary
    Login_btn["fg"] = accent
    Login_btn["justify"] = "left"
    Login_btn["text"] = "Log in"
    Login_btn.place(x=233,y=436,width=70,height=25)


    # Execute Tkinter
    signup.mainloop()

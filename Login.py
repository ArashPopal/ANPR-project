# The Fist goal is to securing our Application form unauthorized access
# First import all necessary libraries
import HomePage
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
import sqlite3
class Login_system(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Login Window")
        # --------window size--------------#
        self.geometry("1350x700+0+0")

        # ----------Variables----------------#
        self.uname = StringVar()
        self.upass = StringVar()

        # -------Images--------------------#
        self.bg_icon = ImageTk.PhotoImage(file="image/bg_pic.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="image/logo_icon.png")
        self.user_icon = ImageTk.PhotoImage(file="image/user_icon.png")
        self.pass_icon = ImageTk.PhotoImage(file="image/password icon.png")
        # -------------Design of window frame-----------#
        self.bg_lbl = Label(self, image=self.bg_icon, ).pack()
        title = Label(self, text="Login Window", font=("times new roman", 40, "bold"), background="blue",
                      foreground="white", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, )
        # ------Here we add a Login frame to add Login fields in the center------#
        login_frame = Frame(self, background="white")
        login_frame.place(x=400, y=150)
        # -----To add User Image for decoration------------#
        Label(login_frame, image=self.logo_icon, bd=0, ).grid(row=0, columnspan=2, pady=20)
        # -------Now to add Labels for user and password-------#
        # --------To add user label------------------------------#
        Label(login_frame, text="User Name", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=2, pady=10)
        # --------To add password label--------------------------#
        Label(login_frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=3, column=0, padx=2, pady=10)
        # -----------Now to add user and password Entery fields-------------#
        # -----------User Name entery---------------------------------------#
        Entry(login_frame, bd=5, textvariable=self.uname, font=("", 15)).grid(row=2, column=1, padx=20)

        # ----------password Entery---------------------------------#
        Entry(login_frame, bd=5, textvariable=self.upass, show="*",
                         font=("", 15)).grid(row=3, column=1, padx=20)

        # ---------Add a Button and apply a function to it-----------#
        Button(login_frame, text="Login", width=15, command=self.login_button_click,
                         font=("times new roman", 20, "bold"), bg="blue", fg="white").grid(row=4, column=1, pady=10)

        # ----------Add a function and apply it to btn_log Button-----#

    def login_button_click(self,event = None ):
        con = sqlite3.connect('login.db')
        cur = con.cursor()
        cur.execute("select * from Login where UserName = ? and Password = ?",
                    (self.uname.get(), self.upass.get()))
        row = cur.fetchone()
        if row is not None:
            con.commit()
            con.close()
            self.destroy()
            HomePage.Home_page()

        else:
            messagebox.showerror("Error Message", "Invalid username/password")

if __name__ == '__main__':
    LoW = Login_system()
    LoW.mainloop()




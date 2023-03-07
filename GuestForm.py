
# import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import HomePage



class Guest_Registeration(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Guest Registraion")
        # --------window size--------------#
        self.geometry("920x450+0+0")
        #-------Add variables------------------------------------------------------------------#

        self.GNational_ID = StringVar()
        self.Name = StringVar()
        self.FNAME = StringVar()
        self.LName = StringVar()
        self.GLPlate = StringVar()
        self.Reason_to_visit = StringVar()
        self.HName = StringVar()
        self.HFName = StringVar()
        self.HLName = StringVar()
        self.HouseNo = StringVar()
        self.EntryTime = StringVar()
        #================================= Frames =======================#
        MainFrame = Frame(self, width=1000, height=400, bg="white", bd=5)
        MainFrame.place(x=10, y=10)
        Guest_text_frame= Frame(MainFrame,width=900,height=50, bg="black")
        Guest_text_frame.place(x=0,y=0)
        toplable=Label(Guest_text_frame,text = "Guest Registration",font=("times new roman", 20, "bold"),bg="black",fg="white")
        toplable.place(x=300,y=10)
        Guest_input_frame=Frame(MainFrame,width=900,height=200, bg="blue")
        Guest_input_frame.place(x=0,y=60)
        Host_input_frame=Frame(MainFrame,width=900,height=100,bg="blue")
        Host_input_frame.place(x=0,y=270)
        Host_text_frame = Frame(MainFrame, width=900, height=50, bg="black")
        Host_text_frame.place(x=0, y=210)
        medell_lable=Label(Host_text_frame,text = "Host information",font=("times new roman", 20, "bold"),bg="black",fg="white")
        medell_lable.place(x=300,y=10)

        #-----------------------------End of frames-----------------------#


        #==============================To add fields and titles============#

        # _____________________________________NAME______________________________________________#
        GNationallabel = Label(Guest_input_frame, text="GNation_ID", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        GNationallabel.grid(row=0, column=0, sticky=NW,padx=5)
        GNational_ID1 = Entry(Guest_input_frame, textvariable=self.GNational_ID, bd=2, font=("", 15), width=15)
        GNational_ID1.grid(row=1, column=0,padx=5)
        # _____________________________________NAME______________________________________________#
        Namelabel = Label(Guest_input_frame, text="Name", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        Namelabel.grid(row=0, column=1, sticky=NW,padx=5)
        Name1 = Entry(Guest_input_frame, textvariable=self.Name, bd=2, font=("", 15), width=30)
        Name1.grid(row=1, column=1,padx=5)
        # _____________________________________NAME______________________________________________#
        GFNamelabel = Label(Guest_input_frame, text="FName", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        GFNamelabel.grid(row=0, column=3, sticky=NW,padx=5)
        FName1 = Entry(Guest_input_frame, textvariable=self.FNAME, bd=2, font=("", 15), width=15)
        FName1.grid(row=1, column=3,padx=5,sticky=NW)
        # _____________________________________NAME______________________________________________#
        GLNamelabel = Label(Guest_input_frame, text="LName:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        GLNamelabel.grid(row=0, column=4, sticky=NW,padx=5)
        LName1 = Entry(Guest_input_frame, textvariable=self.LName, bd=2, font=("", 15), width=15)
        LName1.grid(row=1, column=4,padx=5)
        # _____________________________________NAME______________________________________________#
        GLPLatelabel = Label(Guest_input_frame, text="LPlate:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        GLPLatelabel.grid(row=3, column=0, sticky=NW,padx=5)
        LPlate = Entry(Guest_input_frame, textvariable=self.GLPlate, bd=2, font=("", 15), width=15)
        LPlate.grid(row=4, column=0,padx=5,pady=5)
        # # _____________________________________NAME______________________________________________#
        Reasonlabel = Label(Guest_input_frame, text="Reason To Visit:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        Reasonlabel.grid(row=3, column=1, sticky=NW,padx=5)
        ReasonTo = Entry(Guest_input_frame, textvariable=self.Reason_to_visit, bd=2, font=("", 15), width=30)
        ReasonTo.grid(row=4, column=1,padx=5,pady=5)
        #---------------------- Entery Time and date-----------------------------------------------#
        EntryTimeLabel = Label(Guest_input_frame, text="Visited Time:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        EntryTimeLabel.place(x= 535,y=68)
        # EntryTimeLabel.grid(row=3, column=2, sticky=NW, padx=5)
        EntryTime = Entry(Guest_input_frame, textvariable=self.EntryTime, bd=2, font=("", 15), width=20)
        EntryTime.place(x= 535,y=108)
        # ReasonTo.grid(row=4, column=2, padx=5, pady=5)


        #------------------------ Host information------------------------------------------------#
        HNamelabel = Label(Host_input_frame, text="HName:", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        HNamelabel.grid(row=0, column=1, sticky=NW, padx=5)
        HName1 = Entry(Host_input_frame, textvariable=self.HName, bd=2, font=("", 15), width=20)
        HName1.grid(row=1,column=1,padx=5,pady=5)


        HFNamelabel = Label(Host_input_frame, text="HFName:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        HFNamelabel.grid(row=0, column=2, sticky=NW, padx=5)
        HFname1 = Entry(Host_input_frame, textvariable=self.HFName, bd=2, font=("", 15), width=20)
        HFname1.grid(row=1, column=2, padx=5, pady=5)


        HLNamelabel = Label(Host_input_frame, text="HLName:", font=("times new roman", 20, "bold"),bg="blue",fg="white" )
        HLNamelabel.grid(row=0, column=3, sticky=NW, padx=5)
        HLastname = Entry(Host_input_frame, textvariable=self.HLName, bd=2, font=("", 15), width=20)
        HLastname.grid(row=1,column=3,padx=5,pady=5)


        Houselabel = Label(Host_input_frame, text="HouseNo:", font=("times new roman", 20, "bold"), bg="blue",fg="white")
        Houselabel.grid(row=0, column=4, sticky=NW, padx=5)
        HouseNo1 = Entry(Host_input_frame, textvariable=self.HouseNo, bd=2, font=("", 15), width=15)
        HouseNo1.grid(row=1,column=4,padx=5,pady=5)
        #--------------------------------- To add a Button--------------------------------------------#

        Button(MainFrame, text="Submit", width=15, command=self.add_button_click1,
                                font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=700,y=360)
        # self.back = Button(MainFrame, text="Submit", width=15, command=self.back_to_Home,
        #                         font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=600,y=360)



    # def back_to_Home(self):


    def add_button_click1(self):

        self.con = sqlite3.connect('LPRS_system.db')
        self.cur = self.con.cursor()

        select = "select * from Registration where Name = ? and LName = ? "
        self.cur.execute(select, (self.HName.get(),self.HLName.get()))
        data = self.cur.fetchone()
        print(data, "from data")
        if data is not None:
            self.cur.execute("insert into Guests(GNational_ID,Name,FName,LName,GLPlate,ReasonToVisite,Visited_Time,HName,HFName,"
                             "HLName,HouseNo) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
                             (self.GNational_ID.get(),self.Name.get(), self.FNAME.get(), self.LName.get(),
                              self.GLPlate.get(), self.Reason_to_visit.get(),self.EntryTime.get(), self.HName.get(), self.HFName.get(),
                              self.HLName.get(),
                              self.HouseNo.get()))
            data2 = self.con.commit()
            self.con.close()
            self.destroy()
            HomePage.Home_page()
            print(data2, "-----from data")
            messagebox.showinfo("Success Message", "Contact details are added successfully")
            HomePage.Home_page()
        else:
            messagebox.showerror("Error Message", "No such person liveing here")














# Guest =Guest_Registeration()
# Guest.mainloop()
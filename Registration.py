
from tkinter import *
from tkinter import messagebox
import sqlite3




######################### Variable decleration ######################


class Reg_new_car(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Registration Form")
        # --------window size--------------#
        self.geometry("580x400+0+0")
        #-------Add variables------------------------------------------------------------------#
        self.Name = StringVar()
        self.FNAME = StringVar()
        self.LName = StringVar()
        self.Country = StringVar()
        self.State = StringVar()
        self.City = StringVar()
        self.Home_Address = StringVar()
        self.PhoneNo = StringVar()
        self.LNumber = StringVar()
        self.LPlate = StringVar()
        self.Other_Details = StringVar()



        #-----Please note to remember to do function later on----------------------------------#


        #**********************To create a Frame and add other frames in it*********************#
        BoxFrame = Frame(self, width=1000, height=400, bg="blue", bd=5)
        BoxFrame.place(x=10, y=10)

        # ------------To create a label to choose options---------------------------------------#
        NameFrame = Frame(BoxFrame, width=400, height=150, bg ="blue",bd = 5)
        NameFrame.place(x= 10, y = 10)
        #_____________________________________NAME______________________________________________#
        Namelabel = Label(NameFrame, text="Name:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Namelabel.grid(row=0, column=0,sticky = NW)
        myName = Entry(NameFrame,textvariable=self.Name, bd=2,font=("", 15),width = 15).grid(row = 1 , column = 0,padx = 0 )
        #_________________________________Father NAME_____________________________________________#
        FNAMElabel = Label(NameFrame, text="F/Name:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        FNAMElabel.grid(row = 0, column = 2, sticky = NW)
        FatherName = Entry(NameFrame,textvariable=self.FNAME, bd=2,font=("", 15),width = 15).grid(row = 1,column = 2,padx = 10)
        #-----------------------------LAST NAME-----------------------------------------------#
        LNAMElabel = Label(NameFrame, text="L/Name:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        LNAMElabel.grid(row = 0 ,column = 4 ,sticky = NW)
        LastName = Entry(NameFrame,textvariable=self.LName, bd=2,font=("", 15),width = 15).grid(row =1, column = 4)
        # ------------To create a label to choose options---------------------------------------------------#
        #==================To create Address frame and add address fields Frame=============================#
        AddressFrame = Frame(BoxFrame, bg ="blue", bd=5)
        AddressFrame.place(x=10, y=100)
        #=============================================================================================#

        #====================Country filed and label===================================================#
        Clabel = Label(AddressFrame, text="Country:",padx = 0, font=("times new roman", 20, "bold"), bg ="blue", fg="white",anchor='ne')
        Clabel.grid(row=0, column=0,sticky=NW)
        myCountry = Entry(AddressFrame,textvariable=self.Country, bd=2, font=("", 15),width = 15).grid(row=1, column=0)


        # ====================State/province filed and label===================================================#
        Statelabel = Label(AddressFrame, text="State:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Statelabel.grid(row=0, column=1, sticky=NW)
        myState = Entry(AddressFrame,textvariable=self.State, bd=2, font=("", 15),width = 15).grid(row=1, column=1)


        # ====================city filed and label===================================================#
        Citylabel = Label(AddressFrame, text="City:", font=("times new roman", 20, "bold"), bg ="blue", fg="white",anchor='ne')
        Citylabel.grid(row=0, column=3,sticky=NW)
        myCity = Entry(AddressFrame,textvariable=self.City, bd=2, font=("", 15),width = 14).grid(row=1, column=3)


        # ====================Home address filed and label===================================================#
        HomeAlabel = Label(AddressFrame, text="Home Address:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        HomeAlabel.grid(row=2, column=0)
        HomeAddress = Entry(AddressFrame,textvariable=self.Home_Address, bd=2, font=("", 15),width = 15).grid(row=3, column=0)

        # ====================Phone Number filed and label===================================================#
        Phonelabel = Label(AddressFrame, text="Phone number:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Phonelabel.grid(row=2, column=1, )
        myPhoneNO = Entry(AddressFrame,textvariable=self.PhoneNo, bd=2, font=("", 15),width = 15).grid(row=3, column=1)

        # ------------To create a label to choose options---------------------------------------------------#
        #++++++++++++++++++++++++++++++Car Detail Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        CarFrame = Frame(BoxFrame, bg ="blue", bd=5)
        CarFrame.place(x=10, y=250)


        #+++++++++++++++++++++++++++++Licence Number++++++++++++++++++++++++++++++++++++++++#
        Licencelabel = Label(CarFrame, text="LNumber:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Licencelabel.grid(row=0, column=0,sticky=NW)
        LiNumber = Entry(CarFrame,textvariable=self.LNumber, bd=2, font=("", 15),width = 15).grid(row=1, column=0,padx =0)


        # ++++++++++++++++++++++++++Licence Plate+++++++++++++++++++++++++++++++++++++++++++#
        Platelabel = Label(CarFrame, text="LPlate:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Platelabel.grid(row=0, column=1,sticky=NW)
        myLPlate = Entry(CarFrame,textvariable=self.LPlate, bd=2, font=("", 15),width = 15).grid(row=1, column=1,padx = 0)


        # +++++++++++++C+++++++++++++++Other details+++++++++++++++++++++++++++++++++++++++++#
        Olabel = Label(CarFrame, text="Other:", font=("times new roman", 20, "bold"), bg ="blue", fg="white")
        Olabel.grid(row=0, column=2, sticky = NW)
        OtherDetails = Entry(CarFrame,textvariable=self.Other_Details, bd=2, font=("", 15),width = 17).grid(row=1, column=2)


        # ==================To create A button frame and add funcions =============================#
        Submit = Frame(BoxFrame,bg ="blue", bd=5)
        Submit.place(x=10, y=325)
        # =============================================================================================#

        submitBtn = Button(Submit, text="Submit", width=15,command=self.add_button_click,
                         font=("times new roman", 15, "bold"), bg="white").grid(row=2, column=3, pady=10)

        # +++++++++++++++++++++++Add data to database button click++++++++++++++++++++++++++++++++++++++++++++++#


    def add_button_click(self):
        con = sqlite3.connect('LPRS_system.db')
        cur = con.cursor()
        cur.execute("select * FROM Registration WHERE Name = ?",(self.LPlate.get(),))
        Registration = cur.fetchone()
        if Registration is None:
            cur.execute("insert into Registration(Name,FName,LName,Country,State,City,Home_Address,PhoneNo,"
                             "LNumber,LPlate,Other_details) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (self.Name.get(),self.FNAME.get(), self.LName.get(),
                            self.Country.get(),self.State.get(),self.City.get(),self.Home_Address.get(),self.PhoneNo.get(),
                            self.LNumber.get(),self.LPlate.get(),self.Other_Details.get()))
            con.commit()
            messagebox.showinfo("Success Message", "Contact details are added successfully")
            con.close()
            self.destroy()
        else:
            messagebox.showerror("Error Message", "Contact details are already added")



        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#




#----------- If I uncomment this then it will pop up first ------------#
# Reg = Reg_new_car()
# Reg.mainloop()
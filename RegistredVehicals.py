# --In this page we create multiple frames to
from tkinter import *
from tkinter import ttk
import sqlite3
#------------------- To create a Report to show registred records ------------------------#



class Registered_vehicals(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Report")
        # --------window size--------------#
        self.geometry("1350x700+0+0")
        #------------ To create a general Frame ____________________________________#

        #----------------- DataBase connection ________________________________#

        self.conn = sqlite3.connect('LPRS_system.db')
        self.cur = self.conn.cursor()

        self.BGframe = Frame(self, width= 1300, height=700, relief='raised',bg="light blue")
        self.BGframe.pack()
        # --------------- To create a Frame to add title -----------------------------#
        Top_frame = Frame(self.BGframe, width=1300, height=70, relief='raised', bg="yellow")
        Top_frame.place(x = 0 ,y = 0)
        # ---------------- To create a Label and add Text ----------------------------#
        Label(Top_frame, text="List Of All Registered Vehicals", font=("times new roman", 40, "bold"), bg="yellow",
              fg="blue").place(x=350, y=0)
        # ----------------t create a Frame to add Treeview----------------------------#
        Tree_frame = Frame(self.BGframe, width=1000, height=620, relief='raised', bg="white")
        Tree_frame.place(x = 200, y = 80)





        # ----------------to create a TreeView --------------------------------------#

        #++++++++++++++++++++ Treeview Style +++++++++++++++++++++++++++++++++++++++++#
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        fieldbackground="white")
        style.map('Treeview',
                  background=[('selected','blue')])

        self.Tree_TV_scrol = Scrollbar(Tree_frame)
        self.Tree_TV_scrol.pack(side=RIGHT, fill=Y)
        # ==============================================================================
        #------------- To add columns -------------------------------------------------#
        self.tv = ttk.Treeview(Tree_frame, yscrollcommand=self.Tree_TV_scrol)
        self.tv['columns'] = (
        'Rank', 'Name', 'L_Name', 'F_Name', 'Country', 'State', 'City', 'Home_Address','PhoneNo', 'L_Number', 'L_Plate',
        'Other_info')


        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Rank', anchor=CENTER, width=80)
        self.tv.column('Name', anchor=CENTER, width=80)
        self.tv.column('L_Name', anchor=CENTER, width=80)

        self.tv.column('F_Name', anchor=CENTER, width=80)
        self.tv.column('Country', anchor=CENTER, width=80)
        self.tv.column('State', anchor=CENTER, width=80)

        self.tv.column('City', anchor=CENTER, width=80)
        self.tv.column('Home_Address', anchor=CENTER, width=80)
        self.tv.column('PhoneNo', anchor=CENTER, width=80)
        self.tv.column('L_Number', anchor=CENTER, width=80)

        self.tv.column('L_Plate', anchor=CENTER, width=80)
        self.tv.column('Other_info', anchor=CENTER, width=80)

        #_________________ To add Heading to the columns ___________________#

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Rank', text='Id', anchor=CENTER)
        self.tv.heading('Name', text='Name', anchor=CENTER)
        self.tv.heading('L_Name', text='L/Name', anchor=CENTER)

        self.tv.heading('F_Name', text='F/Name', anchor=CENTER)
        self.tv.heading('Country', text='Country', anchor=CENTER)
        self.tv.heading('State', text='State', anchor=CENTER)

        self.tv.heading('City', text='City', anchor=CENTER)
        self.tv.heading('Home_Address', text='Home Address', anchor=CENTER)
        self.tv.heading('PhoneNo', text='PhoneNo', anchor=CENTER)

        self.tv.heading('L_Number', text='L/number', anchor=CENTER)
        self.tv.heading('L_Plate', text='L/Plate', anchor=CENTER)
        self.tv.heading('Other_info', text='Other Info', anchor=CENTER)

        self.tv.pack()
        # ------------------Button _____________________________________#
        Button(self.BGframe, text="Refresh", width=15, command=self.populateView,
                         font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=200,y=320)

        #++++++++++++++++++ Connect treeview through database +++++++++++++++++#

    def populateView(self):
        self.cur.execute("SELECT * FROM Registration")
        record = self.cur.fetchall()
        self.count = 0
        for record in record:
            self.tv.insert(parent='', index='end', text='',
                        values=(record[0],record[1],record[2],record[3],record[4],
                                    record[5],record[6],record[7],record[8],record[9],record[10],record[11]))
        self.count +=1
        self.conn.commit()
        self.conn.close()


        # ----------- If I uncomment this then it will pop up first -----------
#Rep = Registered_vehicals()
#Rep.mainloop()

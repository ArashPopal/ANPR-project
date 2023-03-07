# --In this page we create multiple frames to
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import sqlite3


class Report_visit(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Report")
        # --------window size--------------#
        self.geometry("1350x700+0+0")
        #-----------------To create a main Frame--------------------------------------#
        self.mainframe = Frame(self,width = 1300, height=700, relief = 'raised', bg="light blue")
        self.mainframe.pack()
        # --------------- To create a Frame to add title -----------------------------#
        Top_frame = Frame(self.mainframe, width=1300, height=70, relief='raised', bg="yellow")
        Top_frame.place(x = 0 ,y = 0)
        # ---------------- To create a Label and add Text ----------------------------#
        Label(Top_frame, text="Report Of Visited Vehicles", font=("times new roman", 40, "bold"), bg="yellow",
              fg="blue").place(x=350, y=0)
        # ----------------t create a Frame to add Treeview----------------------------#

        self.Tree_frame = Frame(self.mainframe, width=1000, height=300, relief='raised', bg="white")
        self.Tree_frame.place(x = 70, y = 80)
        self.Tree_frame2 = Frame(self.mainframe, width=1000, height=300, relief='raised', bg="white")
        self.Tree_frame2.place(x=70,y=370)
        self.Tree_frame2_text=Frame(self.mainframe,width=932,height=60,relief='raised', bg="yellow")
        self.Tree_frame2_text.place(x=0,y=310)
        mylable= Label(self.Tree_frame2_text,text="Report of Guest Vehicles",font=("times new roman", 40, "bold"), bg="yellow",fg="blue")
        mylable.place(x=200,y=0)

        # ----------------to create a TreeView --------------------------------------#

        # ============= Tree Report Scroll option-------------------------------------#
        self.Tree_Report_scrol = Scrollbar(self.Tree_frame)
        self.Tree_Report_scrol.pack(side=RIGHT, fill=Y)
        # ==============================================================================
        self.report = ttk.Treeview(self.Tree_frame,yscrollcommand = self.Tree_Report_scrol)
        self.report['columns'] = ('Rank','VID', 'Name', 'L_Name','F_Name','Country','State','City','Home_Address','PhoneNo'
                         ,'L_Number','L_Plate','CarColor','Visited','Left')
        #------------- To add columns -------------------------------------------------#





        self.report.column('#0', width=0, stretch=NO)
        self.report.column('Rank', anchor=CENTER, width=40)
        self.report.column('VID', anchor=CENTER,width=40)
        self.report.column('Name', anchor=CENTER, width=80)
        self.report.column('F_Name', anchor=CENTER, width=80)

        self.report.column('L_Name', anchor=CENTER, width=80)
        self.report.column('Country', anchor=CENTER, width=80)
        self.report.column('State', anchor=CENTER, width=80)

        self.report.column('City', anchor=CENTER, width=80)
        self.report.column('Home_Address', anchor=CENTER, width=80)
        self.report.column('PhoneNo', anchor=CENTER, width=80)
        self.report.column('L_Number', anchor=CENTER, width=80)

        self.report.column('L_Plate', anchor=CENTER, width=80)
        self.report.column('CarColor', anchor=CENTER, width=80)
        self.report.column('Visited', anchor=CENTER, width=120)
        self.report.column('Left', anchor=CENTER, width=120)

        #_________________ To add Heading to the columns ___________________#

        self.report.heading('#0', text='', anchor=CENTER)
        self.report.heading('Rank', text='Id', anchor=CENTER)
        self.report.heading('VID',text='VID',anchor=CENTER)
        self.report.heading('Name', text='Name', anchor=CENTER)
        self.report.heading('F_Name', text='F/Name', anchor=CENTER)

        self.report.heading('L_Name', text='L/Name', anchor=CENTER)
        self.report.heading('Country', text='Country', anchor=CENTER)
        self.report.heading('State', text='State', anchor=CENTER)

        self.report.heading('City', text='City', anchor=CENTER)
        self.report.heading('Home_Address', text='Home Address', anchor=CENTER)
        self.report.heading('PhoneNo', text='PhoneNo', anchor=CENTER)
        self.report.heading('L_Number', text='L/number', anchor=CENTER)

        self.report.heading('L_Plate', text='L/Plate', anchor=CENTER)
        self.report.heading('CarColor', text='CarColor', anchor=CENTER)

        self.report.heading('Visited', text='Visited', anchor=CENTER)
        self.report.heading('Left', text='Left', anchor=CENTER)


        self.report.pack()

        Button(self, text="Refresh", width=15, command=self.Report(),
                         font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=1110, y=320)

        #-------------------- connect to database------------------------------#

    def Report(self):
        self.conn = sqlite3.connect('LPRS_system.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM Report")
        record = self.cur.fetchall()
        self.conn.commit()
        self.count = 0
        for record in record:
            self.report.insert(parent='', index='end', text='',
                           values=(record[0], record[1], record[2], record[3], record[4],
                                   record[5], record[6], record[7], record[8], record[9], record[10],
                                   record[11],record[12],record[13],record[14]))
        self.count += 1
        self.conn.commit()
        self.conn.close()
        # ----------- If I uncomment this then it will pop up first ------------#



        #---------------- Guest Tree or Report---------------------------------#

        self.Tree_Guest_scrol = Scrollbar(self.Tree_frame2)
        self.Tree_Guest_scrol.pack(side=RIGHT, fill=Y)
        # ==============================================================================
        self.guest = ttk.Treeview(self.Tree_frame2, yscrollcommand=self.Tree_Guest_scrol)
        self.guest['columns'] = (
        'Rank', 'GNational_ID', 'Name', 'FName', 'LName', 'GLPlate', 'ReasonToVisite','VisitedTime', 'HName', 'HFName', 'HLName'
        , 'HouseNo')
        # ------------- To add columns -------------------------------------------------#

        self.guest.column('#0', width=0, stretch=NO)
        self.guest.column('Rank', anchor=CENTER, width=40)
        self.guest.column('GNational_ID', anchor=CENTER, width=60)
        self.guest.column('Name', anchor=CENTER, width=80)
        self.guest.column('FName', anchor=CENTER, width=80)

        self.guest.column('LName', anchor=CENTER, width=80)
        self.guest.column('GLPlate', anchor=CENTER, width=80)
        self.guest.column('ReasonToVisite', anchor=CENTER, width=120)
        self.guest.column('VisitedTime', anchor=CENTER, width=100)

        self.guest.column('HName', anchor=CENTER, width=80)
        self.guest.column('HFName', anchor=CENTER, width=80)
        self.guest.column('HLName', anchor=CENTER, width=80)
        self.guest.column('HouseNo', anchor=CENTER, width=80)

        # _________________ To add Heading to the columns ___________________#

        self.guest.heading('#0', text='', anchor=CENTER)
        self.guest.heading('Rank', text='Id', anchor=CENTER)
        self.guest.heading('GNational_ID', text='GNational_ID', anchor=CENTER)
        self.guest.heading('Name', text='Name', anchor=CENTER)
        self.guest.heading('FName', text='FName', anchor=CENTER)

        self.guest.heading('LName', text='LName', anchor=CENTER)
        self.guest.heading('GLPlate', text='GLPlate', anchor=CENTER)
        self.guest.heading('ReasonToVisite', text='ReasonToVisite', anchor=CENTER)
        self.guest.heading('VisitedTime', text='Visited Time', anchor=CENTER)

        self.guest.heading('HName', text='HName', anchor=CENTER)
        self.guest.heading('HFName', text='HFName', anchor=CENTER)
        self.guest.heading('HLName', text='HLName', anchor=CENTER)
        self.guest.heading('HouseNo', text='HouseNo', anchor=CENTER)
        self.guest.pack()

        Button(self, text="Refresh", width=15, command=self.Report_guest(),
                         font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=95, y=600)


        #=========== Add connection for guest TRee==============================#
    def Report_guest(self):
        self.conn = sqlite3.connect('LPRS_system.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM Guests")
        record = self.cur.fetchall()
        self.count1 = 0
        for record in record:
            self.guest.insert(parent='', index='end', text='',
                               values=(record[0], record[1], record[2], record[3], record[4],
                                       record[5], record[6], record[7], record[8], record[9],record[10],record[11]))
        self.count1 += 1
        self.conn.commit()
        self.conn.close()

# Rep = Report_visit()
# Rep.mainloop()
# --In this page we create multiple frames to
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
#-----DATABASE------------#
import sqlite3
#------- read plate--------#
import numpy as np
import cv2
import imutils
import pytesseract
#======Other pages=======#
import Registration
import RegistredVehicals
import Reported
import GuestForm
#======Other pages=======#
from datetime import datetime


class Home_page(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # --------window title-------------#
        self.title("Home")
        # --------window size--------------#
        self.geometry("1350x700+0+0")


        # ------------To create a label to choose options------------------#
        left_frame = Frame(self, width=350, height=700, relief='raised', bg="white")
        left_frame.place(x=0, y=0)
        # left_frame.pack_propagate(0)

        Btn1 = Button(left_frame, text="Register new Vehicle", command=self.register, padx=20, bg="white",
                           border=0,
                           font=("times new roman", 24, "bold")).grid(row=0, column=0, padx=0, pady=0)
        Btn2 = Button(left_frame, text="Registered Vehicles ", command=self.View_Registered, padx=20, bg="white",
                           border=0,
                           font=("times new roman", 24, "bold")).grid(row=1, column=0, padx=0, pady=0)
        Btn3 = Button(left_frame, text="Reports", padx=20, bg="white", border=0,command = self.Report
                           ,font=("times new roman", 24, "bold")).grid(row=2, column=0, padx=0, pady=0)
        Btn3 = Button(left_frame, text="Register Guest", padx=20, bg="white", border=0, command=self.Open_guest_register
                      , font=("times new roman", 24, "bold")).grid(row=3, column=0, padx=0, pady=0)
        Btn4 = Button(left_frame, text="Incoming Vehicles", padx=20, bg="white", border=0, command = self.Open_In
                           ,font=("times new roman", 24, "bold")).grid(row=4, column=0, padx=0, pady=0)
        Btn5 = Button(left_frame, text="Leaving Vehicles", padx=20, bg="white", border=0,command=self.Open_Out
                           ,font=("times new roman", 24, "bold")).grid(row=5, column=0, padx=0, pady=0)

        # ----------To show DVR and photo and videos and recored ----------------#
        # ----------in other word this is where LPRS should work workds----------#
        self.Right_frame = Frame(self, width=1000, height=700, bg="blue")
        self.Right_frame.pack(side=tk.RIGHT)
        #self.Right_frame.pack_propagate(0)

        # ----------------Label inside the Frame--------------------------------#
        lbl1 = Label(self.Right_frame, text="Nimbus Society gate Management Using ANPRS", font=("times new roman", 30, "bold"), bg="blue",
                     fg="white").place(x=50, y=0)

    def register(self):
        Registration.Reg_new_car()

    def View_Registered(self):
        RegistredVehicals.Registered_vehicals()

    def Report(self):
        Reported.Report_visit()

    def Open_guest_register(self):
        GuestForm.Guest_Registeration()


    def Open_In(self):
        self.filename = filedialog.askopenfilename(initialdir="image2",
                                                    title="Incoming camra", filetype=(
                ("png file", "*.png"), ("jpeg file", "*.jpg"), ("all file", "*.*")))
        right_most_frame = Frame(self.Right_frame, width=1000, height=700)
        right_most_frame.place(x=10, y=100)
        self.pic_btn = ImageTk.PhotoImage(Image.open(self.filename))
        click_button = Button(right_most_frame,image= self.pic_btn,command=self.image_click,borderwidth=0 )
        click_button.place(x=0,y=0)



    def image_click(self,event = None):
        #------ drop all cv2 files here-------------------#
        image = cv2.imread(self.filename)

        image = imutils.resize(image, width=500)
        cv2.imshow('image', image)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("1 - Grayscale Conversion", gray)

        blur = cv2.GaussianBlur(gray,(3,3),0)
        # cv2.imshow("2 - Bilateral Filter", gray)

        edged = cv2.Canny(blur, 170, 200)
        # cv2.imshow("4 - Canny Edges", edged)

        # (new, cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
        NumberPlateCnt = None

        count = 0
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                NumberPlateCnt = approx
                break

        # Masking the part other than the number plate
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
        new_image = cv2.bitwise_and(image, image, mask=mask)
        cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
        cv2.imshow("Final_image", new_image)
        #-----------------Tesseract Commands-------------------------------#
        # Configuration for tesseract
        config = ('-l eng --oem 1 --psm 3')


        # Run tesseract OCR on image
        text = pytesseract.image_to_string(new_image, config=config)
        #------------------ End of Tesseract Commands---------------------#

        # Print recognized text
        print(text)

        cv2.waitKey(20)

        #-------end of code cv2----------------------------#

        #========== database connection=====================#
        #--------- OPen in _________________________________#
        conn = sqlite3.connect("LPRS_system.db")
        cur = conn.cursor()

        select = "select * from Registration where LPlate =(?) "
        cur.execute(select, (text,))
        data = cur.fetchone()
        print(data, "from data")
        if data is not None:
            conn.commit()
            cur = conn.cursor()
            insert = "insert into Report(VID,Name,FName,LName,Country,State,City,Home_Address,PhoneNo,LNumber,LPlate,CarColor) values(?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
            data1 = cur.execute(insert, (data))
            print(data1,"----data1")
            conn.commit()

            cur = conn.cursor()
            select2 = "select * from Report where LPlate =(?)"
            cur.execute(select2,(text,))
            data2 = cur.fetchone()
            print(data2,"------data2")
            conn.commit()

            if data2 is not None:
                while text in data2:
                    cur = conn.cursor()
                    update = "update Report SET TimeVisited =? WHERE LPlate = ?"
                    data3 = cur.execute(update, (datetime.now(), text))
                    print(data3, "--from data3")
                    break
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Database Updated")
                messagebox.showinfo("Success", "Gate Opened")
            else:
                messagebox.showerror("error","Not updated")

        else:
            conn.commit()
            conn.close()
            messagebox.showerror("Error", "Unexpected Visiter")
            self.destroy()
            GuestForm.Guest_Registeration()







    def Open_Out(self):
        self.filename1 = filedialog.askopenfilename(initialdir="image2",
                                                    title="Leaving Camra", filetype=(
                ("png file", "*.png"), ("jpeg file", "*.jpg"), ("all file", "*.*")))
        right_most_frame = Frame(self.Right_frame, width=1000, height=700)
        right_most_frame.place(x=10, y=100)
        self.pic_btn1 = ImageTk.PhotoImage(Image.open(self.filename1))
        click_button1 = Button(right_most_frame, image=self.pic_btn1, command=self.image_click1, borderwidth=0)
        click_button1.place(x=0, y=0)

    def image_click1(self):
        # ------ drop all cv2 files here-------------------#
        image = cv2.imread(self.filename1)
        cv2.imshow('image', image)

        image = imutils.resize(image, width=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("1 - Grayscale Conversion", gray)

        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        # cv2.imshow("2 - Bilateral Filter", gray)

        edged = cv2.Canny(gray, 170, 200)
        # cv2.imshow("4 - Canny Edges", edged)

        # (new, cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
        NumberPlateCnt = None

        count = 0
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                NumberPlateCnt = approx
                break

        # Masking the part other than the number plate
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
        new_image = cv2.bitwise_and(image, image, mask=mask)
        cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
        cv2.imshow("Final_image", new_image)
        # -----------------Tesseract Commands-------------------------------#
        # Configuration for tesseract
        config = ('-l eng --oem 1 --psm 3')

        # Run tesseract OCR on image
        text = pytesseract.image_to_string(new_image, config=config)
        # ------------------ End of Tesseract Commands---------------------#

        # Print recognized text
        print(text)

        cv2.waitKey(10)

        # -------end of code cv2----------------------------#

        # ========== database connection=====================#
        # --------- OPen in _________________________________#
        conn = sqlite3.connect("LPRS_system.db")
        cur = conn.cursor()

        select = "select * from Registration where LPlate =(?) "
        cur.execute(select, (text,))
        data = cur.fetchone()
        print(data, "from data")
        if data is not None:
            conn.commit()
            cur = conn.cursor()
            insert = "insert into Report(VID,Name,FName,LName,Country,State,City,Home_Address,PhoneNo,LNumber,LPlate,CarColor) values(?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
            data1 = cur.execute(insert, (data))
            print(data1, "----data1")
            conn.commit()

            cur = conn.cursor()
            select2 = "select * from Report where LPlate =(?)"
            cur.execute(select2, (text,))
            data2 = cur.fetchone()
            print(data2, "------data2")
            conn.commit()

            if data2 is not None:
                while text in data2:
                    cur = conn.cursor()
                    update = "update Report SET TimeLeave =? WHERE LPlate = ?"
                    data3 = cur.execute(update, (datetime.now(), text))
                    print(data3, "--from data3")
                    break
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Database Updated")
                messagebox.showinfo("Success", "Gate Opened")
            else:
                messagebox.showerror("error", "Not updated")

        else:
            messagebox.showerror("Error", "Something is wrong")





# Req = Home_page()
# Req.mainloop()

from tkinter import*
from tkinter import ttk 
import random
import time


import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.NameOfTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NumberOfTablets = StringVar()
        self.Lot = StringVar()
        self.IsuueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatienId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        
        lbtitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill='x')
        
        #==============================DATAFRAME=================================#
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        #======================== Butoons Frame ===========================================#
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #======================== Details Frame ===========================================#
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #==============================Dataframeleft =====================================#
        lblNameTablet = Label(DataframeLeft,text="Names of Tablets",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        #entry box combo box 1 Names of Tablets
        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Nice","Corona Vacacine", "Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        #entry box  2 Refence No
        lblref = Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft,textvariable=self.Ref,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        #entry box  3 Dose
        lblDose = Label(DataframeLeft,text="Dose",font=("arial",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)
        
        #entry box  4 No of Tablets
        lblNoOftablets = Label(DataframeLeft,text="No of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft,textvariable=self.NumberOfTablets,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        #entry box  5 Lot
        lbllot = Label(DataframeLeft,text="Lot:",font=("arial",12,"bold"),padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft,textvariable=self.Lot,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        #entry box  6 Issue Date
        lblissueDate = Label(DataframeLeft,text="Issue Date",font=("arial",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataframeLeft,textvariable=self.IsuueDate,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)
        
        #entry box 7 Exp Date
        lblExpDate = Label(DataframeLeft,text="Exp Date",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataframeLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        #entry box  8 Daily Dose
        lblDailyDose = Label(DataframeLeft,text="Daily Dose",font=("arial",12,"bold"),padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        #entry box 9 Side Effect
        lblSideEffect = Label(DataframeLeft,text="Side Effect:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataframeLeft,textvariable=self.SideEffect,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        #entry box 1 Further Information    2nd coloum info
        lblFurtherinfo = Label(DataframeLeft,text="Further Information",font=("arial",12,"bold"),padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo = Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        #entry box 2 Blood Pressure    2nd coloum info
        lblBloodPressure  = Label(DataframeLeft,text="Blood Pressure",font=("arial",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure = Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=("arial",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        #entry box 3 Storage Advice 2nd coloum info
        lblStorage = Label(DataframeLeft,text="Storage Advice",font=("arial",12,"bold"),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)
        
        #entry box 4 Medication 2nd coloum info
        lblMedicine = Label(DataframeLeft,text="Medication",font=("arial",12,"bold"),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataframeLeft,textvariable=self.HowToUseMedication,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)
        
        #entry box 5 Patient Id 2nd coloum info
        lblPatientId = Label(DataframeLeft,text="Patient Id",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId = Entry(DataframeLeft,textvariable=self.PatienId,font=("arial",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)
        
        #entry box 6 NHS Number 2nd coloum info
        lblNhsNumber = Label(DataframeLeft,text="NHS Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataframeLeft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        #entry box 7 Patient Name 2nd coloum info
        lblPatientname  = Label(DataframeLeft,text="Patient Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname = Entry(DataframeLeft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        txtPatientname.grid(row=6,column=3)
        
        #entry box 8 Date of Birth 2nd coloum info
        lblDateofBirth  = Label(DataframeLeft,text="Date of Birth",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth = Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("arial",12,"bold"),width=35)
        txtDateofBirth.grid(row=7,column=3)
        
        #entry box 9 Patient Address 2nd coloum info
        lblPatientAddress  = Label(DataframeLeft,text="Patient Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataframeLeft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        #==================================== Data Frame Right ============================================#
        self.txtPrescription = Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
         
        #================================= Buttons =======================================================#
        btnPrescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.iPrectioption)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData = Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.iPresriptionData)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate = Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.upadte)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete = Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.idelete)
        btnDelete.grid(row=0,column=3)
        
        btnClear = Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.clear)
        btnClear.grid(row=0,column=4)
        
        btnExit = Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=self.iexit)
        btnExit.grid(row=0,column=5)
        
        #=========================================== table ============================================#
        #===================================== Scroll Bar ============================================#
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,columns=("TabletName","Ref","Dose","NoOfTablets","Lot","IssueDate","ExpDate","DailyDose","Storage","NhsNumber",
                                                                 "Pname","Dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        # to view table 
        scroll_x= ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)
        
        # pack above table with heading
        self.hospital_table.heading("TabletName" ,text="Name Of Table")
        self.hospital_table.heading("Ref"        ,text="Reference No.")
        self.hospital_table.heading("Dose"       ,text="Dose")
        self.hospital_table.heading("NoOfTablets",text="No Of Tablets")
        self.hospital_table.heading("Lot"        ,text="Lot")
        self.hospital_table.heading("IssueDate"  ,text="Issue Date")
        self.hospital_table.heading("ExpDate"    ,text="Exp Date")
        self.hospital_table.heading("DailyDose"  ,text="Daily Dose")
        self.hospital_table.heading("Storage"    ,text="Storage")
        self.hospital_table.heading("NhsNumber"  ,text="NHS Number")
        self.hospital_table.heading("Pname"      ,text="Patient Name")
        self.hospital_table.heading("Dob"        ,text="DOB")
        self.hospital_table.heading("Address"    ,text="Address")
        
        self.hospital_table["show"]="headings"   
        
        self.hospital_table.column("TabletName",width=100) 
        self.hospital_table.column("Ref"        ,width=100)
        self.hospital_table.column("Dose"       ,width=100)
        self.hospital_table.column("NoOfTablets",width=100)
        self.hospital_table.column("Lot"        ,width=100)
        self.hospital_table.column("IssueDate"  ,width=100)
        self.hospital_table.column("ExpDate"    ,width=100)
        self.hospital_table.column("DailyDose"  ,width=100)
        self.hospital_table.column("Storage"    ,width=100)
        self.hospital_table.column("NhsNumber"  ,width=100)
        self.hospital_table.column("Pname"      ,width=100)
        self.hospital_table.column("Dob"        ,width=100)
        self.hospital_table.column("Address"    ,width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1) 
        # bind
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    #============================== Functinality Decleation ===============================#
    def iPresriptionData(self):
            if self.NameOfTablets.get()=="" or self.Ref.get() =="":
                messagebox.showerror("Error","All fields are required")
            else:
                # connect to mysql 
                conn = mysql.connector.connect(host="localhost",username="root",password="Komal5kp",database="hospital")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into hospital_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                          self.NameOfTablets.get(),
                                                                                                          self.Ref.get(), 
                                                                                                          self.Dose.get(),
                                                                                                          self.NumberOfTablets.get(), 
                                                                                                          self.Lot.get(),
                                                                                                          self.IsuueDate.get(),
                                                                                                          self.ExpDate.get(),
                                                                                                          self.DailyDose.get(),
                                                                                                          self.StorageAdvice.get(),
                                                                                                          self.nhsNumber.get(),
                                                                                                          self.PatientName.get(),
                                                                                                          self.DateOfBirth.get(),
                                                                                                          self.PatientAddress.get(),
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Komal5kp",database="hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital_data")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IsuueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        
    def upadte(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Komal5kp",database="hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital_data set NameOfTablets=%s,  Dose=%s, NumberOfTablets=%s, Lot=%s, IsuueDate=%s, ExpDate=%s, DailyDose=%s, Storage=%s, nhsNumber=%s, PatientName=%s, DateOfBirth=%s, PatientAddress=%s where Ref=%s",(
            
                                                                                                          self.NameOfTablets.get(), 
                                                                                                          self.Dose.get(),
                                                                                                          self.NumberOfTablets.get(), 
                                                                                                          self.Lot.get(),
                                                                                                          self.IsuueDate.get(),
                                                                                                          self.ExpDate.get(),
                                                                                                          self.DailyDose.get(),
                                                                                                          self.StorageAdvice.get(),
                                                                                                          self.nhsNumber.get(),
                                                                                                          self.PatientName.get(),
                                                                                                          self.DateOfBirth.get(),
                                                                                                          self.PatientAddress.get(),
                                                                                                          self.Ref.get(),
        
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Update","Record has been updated successfully")
    
    
    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.NameOfTablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.Ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberOfTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IsuueDate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Info:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Driving Using Machine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"How To Use Medication:\t\t\t"+self.HowToUseMedication.get()+"\n")
        self.txtPrescription.insert(END,"Patien Id:\t\t\t"+self.PatienId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
        
    def idelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Komal5kp",database="hospital")
        my_cursor = conn.cursor()
        query ="delete from hospital_data where Ref=%s"
        val = (self.Ref.get(),)
        my_cursor.execute(query,val)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Deleter","Record has been Deleted successfully")
        
        
    def clear(self):
        self.NameOfTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.IsuueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatienId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress("")
        self.txtPrescription.delete("1.0",END)
        
    def iexit(self):
        iexit = messagebox.askyesno("Hospital Managment System","Confirm you want to exit")
        if iexit > 0:
            root.destroy()
            return
        
        
        
          
        

root = Tk()
ob = Hospital(root)
root.mainloop()

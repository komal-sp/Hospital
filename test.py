from tkinter import *
from tkinter import messagebox

root = Tk()  
root.title("Hospital Management System")
root.geometry("1540x800+0+0")


def iPresriptionData():
            messagebox.showinfo("Success","Record has been inserted")
            
     
Buttonframe = Frame(root,bd=20,relief=RIDGE)
Buttonframe.place(x=0,y=530,width=1530,height=70)
                 
btnPrescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6,command=iPresriptionData)
btnPrescription.grid()
        
  
root.mainloop()
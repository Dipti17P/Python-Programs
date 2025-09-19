from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector

win = Tk()
win.title("Customer Entry Form")
win.geometry("600x420")

# -------------------- DB Connection Helper --------------------
def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="project"
    )

# -------------------- Utility Functions --------------------
def clsfield():
    txtcname.delete(0, END)
    txtcadd.delete(0, END)
    txtcity.delete(0, END)
    txtcmob.delete(0, END)
    
def maxrec():
    import mysql.connector
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="project"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from custmast")
    mydata = mycur.fetchall()
    mx=0
    for i in mydata:
        mx=i[0]
    mx=mx+1
    txtcno.delete(0, END)
    txtcno.insert(0, mx)
    clsfield()

def saverec():
    s1=txtcno.get()
    s2=txtcname.get()
    s3=txtcadd.get()
    s4=txtcity.get()
    s5=txtcmob.get()
    if s2.strip()=="":
        messagebox.showinfo("Warn", "Please enter your name")
        return
    if s3.strip()=="":
        messagebox.showinfo("Warn", "Please enter your address")
        return
    if s4.strip()=="":
        messagebox.showinfo("Warn", "Please enter your city")
        return
    if s5.strip()=="":
        messagebox.showinfo("Warn", "Please enter your mobile")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="project"
    )
    mycur = mydb.cursor()
    mycur.execute("INSERT INTO custmast VALUES (" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "')")
    mydb.commit()
    messagebox.showinfo("Success", "Record has been saved")
    maxrec()

def serrec():
    mcno=simpledialog.askstring("Find", "Search Record")
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="project"
    )
    clsfield()
    txtcno.delete(0, END)
    mycur=mydb.cursor()
    mycur.execute("select * from custmast where cno="+mcno)
    mydata = mycur.fetchone()
    if mydata is not None:
        txtcno.insert(0, mydata[0])
        txtcname.insert(0, mydata[1])
        txtcadd.insert(0, mydata[2])
        txtcity.insert(0, mydata[3])
        txtcmob.insert(0, mydata[4])
    else:
        messagebox.showinfo("Confirm", "No record found")
def uprec():
    s1 = txtcno.get()
    s2 = txtcname.get()
    s3 = txtcadd.get()
    s4 = txtcity.get()
    s5 = txtcmob.get()
    if s2.strip()=="":
        messagebox.showinfo("Warn", "Please enter your name")
        return
    if s3.strip()=="":
        messagebox.showinfo("Warn", "Please enter your address")
        return
    if s4.strip()=="":
        messagebox.showinfo("Warn", "Please enter your city")
        return
    if s5.strip()=="":
        messagebox.showinfo("Warn", "Please enter your mobile")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="project"
    )
    mycur = mydb.cursor()
    mycur.execute("UPDATE custmast SET cname='" + s2 + "', cadd='" + s3 + "', city='" + s4 + "', contact='" + s5 + "' WHERE cno=" + s1)
    mydb.commit()
    messagebox.showinfo("Success", "Record has been saved")
    maxrec()
    
def delrec():
    mcno = txtcno.get()
    if not mcno:
        messagebox.showwarning("Warning", "No record selected")
        return
    ans = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
    if ans:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM custmast WHERE cno=%s", (mcno,))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Record has been deleted")
        maxrec()
        
f1=("arial",15,'bold')
l1=Label(win,text="Customer Entry Name",font=f1,bg='red',fg='white')
l1.pack(fill=BOTH)

l2=Label(win,text="Customer No",font=f1)
l2.place(x=70,y=70)
txtcno=Entry(win,font=f1,bd=3)
txtcno.place(x=280,y=70)

l3=Label(win,text="Customer Name",font=f1)
l3.place(x=70,y=120)
txtcname=Entry(win,font=f1,bd=3)
txtcname.place(x=280,y=120)

l4=Label(win,text="Customer Address",font=f1)
l4.place(x=70,y=170)
txtcadd=Entry(win,font=f1,bd=3)
txtcadd.place(x=280,y=170)

l5=Label(win,text="Customer City",font=f1)
l5.place(x=70,y=220)
txtcity=Entry(win,font=f1,bd=3)
txtcity.place(x=280,y=220)

l6=Label(win,text="Customer Mobile",font=f1)
l6.place(x=70,y=270)
txtcmob=Entry(win,font=f1,bd=3)
txtcmob.place(x=280,y=270)

b1=Button(win,text="Add",font=f1,bd=3,width=6,command=maxrec)
b1.place(x=10,y=320)

b2=Button(win,text="Save",font=f1,bd=3,width=6,command=saverec)
b2.place(x=110,y=320)

b3=Button(win,text="Search",font=f1,bd=3,width=6,command=serrec)
b3.place(x=210,y=320)

b4=Button(win,text="Update",font=f1,bd=3,width=6,command=uprec)
b4.place(x=310,y=320)

b5=Button(win,text="Delete",font=f1,bd=3,width=6,command=delrec)
b5.place(x=410,y=320)

b6=Button(win,text="Exit",font=f1,bd=3,width=6,command=win.destroy)
b6.place(x=510,y=320)

win.mainloop()

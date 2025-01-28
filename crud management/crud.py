from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
#database Connectivity
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="example",
    port=3306
)
#Enter event
def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"
#select event
def getrow(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    rno.set(item['values'][0])
    stu_name.set(item['values'][1])
    Dob.set(item['values'][2])
    Gen.set(item['values'][3])
    
    
#clear button Fun()
def clear():
    rollno_entry.delete(0,END)
    name_entry.delete(0,END)
    dob_entry.delete(0,END)
    gender_combobox.set("--Select--")
#insert Button Fun()
def Insert():
    rollno = rollno_entry.get()
    name = name_entry.get()
    dob = dob_entry.get()
    gen=gender_combobox.get()

    # Input validation
    if not rollno or not name or not dob or not gen:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if not rollno.isdigit():
        messagebox.showerror("Input Error", "Roll number must be numeric!")
        return
    if gen=="--Select--":
        messagebox.showerror("Input Error", "Gender is not Selected!")
        return
    try:
        cur_obj = con.cursor()
        # Parameterized query to prevent SQL injection
        sql = "INSERT INTO stud (rno, stu_name, dob, gender) VALUES (%s, %s, %s, %s)"
        val = (rollno, name, dob, gen)
        cur_obj.execute(sql, val)
        con.commit()

        # Refresh the Treeview and show success message
        view()
        messagebox.showinfo("Success", "Record inserted successfully")
        clear()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred: {ex}")

#view Button Fun()
def view():
    for row in trv.get_children():
        trv.delete(row)  # Clear the Treeview
    cur_obj = con.cursor()
    cur_obj.execute("SELECT * FROM stud")
    res = cur_obj.fetchall()
    for i in res:
        trv.insert("", "end", values=i)
#delete Button Fun()
def delete():
    rollno=rollno_entry.get()
    name = name_entry.get()
    dob = dob_entry.get()
    gen=gender_combobox.get()
    cur_obj=con.cursor()
     # Input validation
    if not rollno or not name or not dob or not gen:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if messagebox.askyesno("confirm delete","Are you sure want to delete this"):
        sql="delete from stud where rno="+rollno
        cur_obj.execute(sql)
        con.commit()
        view()
        messagebox.showinfo("DELETED","Deleted successfully")
        clear()
    else:
        return True
#update Button Fun()
def update():
    name=stu_name.get()
    rollno=rno.get()
    dob=Dob.get()
    gen=Gen.get()
    cur_obj=con.cursor()
     # Input validation
    if not rollno or not name or not dob or not gen:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if messagebox.askyesno("confirm Update","Are you sure want to update this"):
        sql="update stud set stu_name=%s,dob=%s,gender=%s where rno=%s"
        cur_obj.execute(sql,(name,dob,gen,rollno))
        con.commit()
        view()
        messagebox.showinfo("UPDATED","Updated successfully")
        clear()
#background color
background="#06283D"
#creating main window
app=Tk()
app.title("Student data")
#app.geometry("550x500")
app.geometry("1510x800+0+0")
app.resizable(0,0)
app.anchor("center")
rno=StringVar()
stu_name=StringVar()
Dob=StringVar()
Gen=StringVar()
#creating frames
#frame1:
frame1=LabelFrame(app,text="STUDENTS DATA ENTRY",bd=7,fg="orange",font=("Arial",18,"bold"),width=200,height=250,bg=background)
frame1.pack(fill=BOTH,expand=True)
#Creatig Labels and Entries
rollno_label=Label(frame1,text="ROLL NO",fg="white",bg=background,font=("Arial",20,"bold"))
rollno_label.grid(row=1,column=1,padx=20,pady=20)
rollno_entry=Entry(frame1,textvariable=rno,font=("Arial",19,"bold"))
rollno_entry.grid(row=1,column=2,padx=10,pady=20)
rollno_entry.bind("<Return>",focus_next)
name_label=Label(frame1,text="STUDENT NAME",bd=2,fg="white",bg=background,font=("Arial",20,"bold"))
name_label.grid(row=2,column=1,padx=20,pady=5)
name_entry=Entry(frame1,textvariable=stu_name,font=("Arial",19,"bold"))
name_entry.grid(row=2,column=2,padx=10,pady=5)
name_entry.bind("<Return>",focus_next)
dob_label=Label(frame1,text="DATE OF BIRTH",fg="white",bg=background,font=("Arial",20,"bold"))
dob_label.grid(row=3,column=1,padx=20,pady=5)
dob_entry=DateEntry(frame1,textvariable=Dob,background="blue",foreground="white",headersbackground="green",headersforeground="white",selectbackground="green",selectforeground="white",weekendforeground="red",font=("Arial",20,"bold"),date_pattern="dd/mm/yyyy")
dob_entry.grid(row=3,column=2,padx=10,pady=5)
dob_entry.bind("<Return>",focus_next)
#dateEntry adding Style
gender_label=Label(frame1,text="GENDER",fg="white",bg=background,font=("Arial",20,"bold"))
gender_label.grid(row=4,column=1,padx=20,pady=5)
gender_combobox=ttk.Combobox(frame1,textvariable=Gen,values=("Male","Female"),font=("Arial",18,"bold"),state="readonly",justify=CENTER)
gender_combobox.grid(row=4,column=2,padx=10,pady=5)
gender_combobox.set("--Select--")
#creating Button
#clear Button
clr_btn=Button(frame1,text="CLEAR",bd=0,font=("Arial",12,"bold"),fg="white",activeforeground="white",bg="blue",activebackground="blue",cursor="hand2",command=clear)
clr_btn.grid(row=5,column=2,sticky=W,padx=10,pady=15)
#frame2:
frame2=Frame(app,width=100,height=10,bg=background,bd=7)
frame2.pack(fill=BOTH,expand=True)
#Insert Button
inst_btn=Button(frame2,text="INSERT",bd=0,font=("Arial",20,"bold"),height="2",width="10",fg="black",activeforeground="black",bg="yellow",activebackground="yellow",cursor="hand2",command=Insert)
inst_btn.grid(row=3,column=2,padx=10,pady=30)
#View Button
view_btn=Button(frame2,text="VIEW",bd=0,font=("Arial",20,"bold"),height="2",width="10",fg="black",activeforeground="black",bg="green",activebackground="green",cursor="hand2",command=view)
view_btn.grid(row=3,column=3,padx=10,pady=30)
#Delete Button
del_btn=Button(frame2,text="DELETE",bd=0,font=("Arial",20,"bold"),height="2",width="10",fg="black",activeforeground="black",bg="red",activebackground="red",cursor="hand2",command=delete)
del_btn.grid(row=3,column=4,padx=10,pady=30)
#Update Button
upd_btn=Button(frame2,text="UPDATE",bd=0,font=("Arial",20,"bold"),height="2",width="10",fg="black",activeforeground="black",bg="blue",activebackground="blue",cursor="hand2",command=update)
upd_btn.grid(row=3,column=5,padx=10,pady=30)
#frame3:
frame3=LabelFrame(app,text="STUDENT DATA'S",fg="orange",bg=background,bd=7,font=("Arial",18,"bold"),width=200,height=350)
frame3.pack(fill=BOTH,expand=True)
#vertical_scrollbar=Scrollbar(frame3,orient=VERTICAL)
trv=ttk.Treeview(frame3,column=(1,2,3,4),show="headings",height="8")
style = ttk.Style(app)
style.configure("Treeview",foreground="black",background="white",fieldbackground="blue",font=("Arial", 14,"bold"))
style.map("Treeview",background=[("selected","green")])
style.configure("Treeview.Heading",background="black",foreground="green", font=("Arial", 20,"bold"))
#vertical_scrollbar.pack(side=RIGHT)
trv.pack()
trv.heading(1,text="ROLLNO")
trv.heading(2,text="STUD_NAME")
trv.heading(3,text="DOB")
trv.heading(4,text="GENDER")
trv.column(1,anchor ='c')
trv.column(2,anchor ='c')
trv.column(3,anchor ='c')
trv.column(4,anchor ='c')
#trv.column(2,width=150)
trv.bind("<Double 1>",getrow)
#Run the Application
app.mainloop()
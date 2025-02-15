#Employee Management System
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from tkinter import ttk
import Empdatabse

#Logout btn Fun()
def logout():
    if(messagebox.askyesno("Confirm Logout","Are You sure Want to Logout.")):
        app.destroy()
    import custom_login
#Exit Btn Fun()
def exit_fun():
    if(messagebox.askyesno("Confirm Exit","Are You sure Want to Quit.")):
        app.destroy()
#Admin btn Fun()
def admin():
    #disable the others button
    #emp_btn.configure(state="disabled")
    #clear_btn fun()
    def clear():
        adminIdEntry.delete(0,END)
        adminNameEntry.delete(0,END)
        admingenderEntry.set("--Select--")
        adminContactEntry.delete(0,END)
        adminEmailEntry.delete(0,END)
        adminPasswordEntry.delete(0,END)
        
    #Enter event
    def focus_next(event):
        event.widget.tk_focusNext().focus()
        return "break"
    #fetch method
    def showall():
        search_combobox.set("Search_by")
        search_Entry.delete(0,END)
        for row in tabel.get_children(): # Clear the Treeview
            tabel.delete(row) 
        admin=Empdatabse.fetch()
        for i in admin:
            tabel.insert("", "end", values=i)
    #treeview select event
    def selection(event):
        clear()
        rowid=tabel.selection()
        if rowid:
            row=tabel.item(rowid)['values']
            adminIdEntry.insert(0,row[0])
            adminNameEntry.insert(0,row[1])
            admingenderEntry.set(row[2])
            adminContactEntry.insert(0,row[3])
            adminEmailEntry.insert(0,row[4])
            adminPasswordEntry.insert(0,row[5])
            
        
    #back button
    def back():
        admin_frame.place_forget()
        #emp_btn.configure(state="normal")
        

    
    #save btn fun()
    def save():
        
        Id=adminIdEntry.get()
        
        Name=adminNameEntry.get()
        
        Gender=admingenderEntry.get()
        
        Contact=adminContactEntry.get()
       
        Email=adminEmailEntry.get()
       
        Password=adminPasswordEntry.get()
        if not Id or not Name or not Contact or not Email or not Password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        if not Id.isdigit():
            messagebox.showerror("Input Error", "ID must be numeric!")
            return
        if not Contact.isdigit():
            messagebox.showerror("Input Error", "Contact must be numeric!")
            return
        if not Password.isdigit():
            messagebox.showerror("Input Error", "Password must be numeric!")
            return
        if Gender=="--Select--":
            messagebox.showerror("Input Error", "Gender is not Selected!")
            return
        elif Empdatabse.id_exist(Id):
            messagebox.showerror("Error", "Id is Already Exist!")
            
        else:
            messagebox.showinfo("Save","Successfully Saved!")
            Empdatabse.insert(Id,Name,Gender,Contact,Email,Password)
            clear()
            showall()
    def update_fun():
        Id=adminIdEntry.get()
        
        Name=adminNameEntry.get()
        
        Gender=admingenderEntry.get()
        
        Contact=adminContactEntry.get()
       
        Email=adminEmailEntry.get()
       
        Password=adminPasswordEntry.get()
        if not Id or not Name or not Contact or not Email or not Password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        if not Id.isdigit():
            messagebox.showerror("Input Error", "ID must be numeric!")
            return
        if not Contact.isdigit():
            messagebox.showerror("Input Error", "Contact must be numeric!")
            return
        if not Password.isdigit():
            messagebox.showerror("Input Error", "Password must be numeric!")
            return
        if Gender=="--Select--":
            messagebox.showerror("Input Error", "Gender is not Selected!")
            return            
        else:
            messagebox.showinfo("UPDATE","Successfully Updated!")
            Empdatabse.update(Id,Name,Gender,Contact,Email,Password)
            clear()
            showall()
    def delete_fun():
        Id=adminIdEntry.get()
        
        Name=adminNameEntry.get()
        
        Gender=admingenderEntry.get()
        
        Contact=adminContactEntry.get()
       
        Email=adminEmailEntry.get()
       
        Password=adminPasswordEntry.get()
        if not Id or not Name or not Contact or not Email or not Password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        if not Id.isdigit():
            messagebox.showerror("Input Error", "ID must be numeric!")
            return
        if not Contact.isdigit():
            messagebox.showerror("Input Error", "Contact must be numeric!")
            return
        if not Password.isdigit():
            messagebox.showerror("Input Error", "Password must be numeric!")
            return
        if Gender=="--Select--":
            messagebox.showerror("Input Error", "Gender is not Selected!")
            return            
        else:
            messagebox.showinfo("DELETE","Successfully Deleted!")
            Empdatabse.delete(Id)
            clear()
            showall()

   
    def search_fun():
        search_var = search_Entry.get().strip()  # Remove leading/trailing spaces
        searchbox = search_combobox.get().strip()
        if not search_var:
            messagebox.showwarning("Input Error", "Enter a value to search")
            return

        if searchbox.lower() == "search_by":  # Ensure correct selection
            messagebox.showerror("Input Error", "Please select a valid search option")
            return
        #Ensure column names match the database exactly
        column_mapping = {
            "Id": "admin_id",
            "Name": "name",
            "Gender":"gender",
            "Contact No": "contact_no",
            "Email": "email"
            }
        searchbox = column_mapping.get(searchbox, searchbox.lower())  # Convert to correct column
        allowed_columns = column_mapping.values()  # Ensuring only valid columns
        if searchbox not in allowed_columns:
            messagebox.showerror("Input Error", f"Invalid search category: {searchbox}")
            return
        # Fetch data from the database
        searched_data = Empdatabse.search(searchbox, search_var)
        # Debugging: Print the query to check correctness
        #print(f"Searching in column: {searchbox}, with value: {search_var}")

        # Clear existing records from the table
        for row in tabel.get_children():
            tabel.delete(row)

        if not searched_data:
            messagebox.showinfo("Search Result", "No matching records found")
            return
        # Insert new search results
        for record in searched_data:
            tabel.insert("", "end", values=record)

            
        
        
            
    admin_frame=CTkFrame(app,width=1300,height=670)
    admin_frame.place(x=180,y=80)
    #admin background Image
    adminbg_image=CTkImage(Image.open("adminbg.png"),size=(1300,670))
    adminbg_imageLabel=CTkLabel(admin_frame,image=adminbg_image,text=" ")
    adminbg_imageLabel.place(x=0,y=0)
    backImage=CTkImage(Image.open("backward.png"),size=(50,50))
    back_btn=CTkButton(admin_frame,image=backImage,command=back,text=" ",width=50,border_width=3,fg_color="#010721",bg_color="#010721",hover_color="#010721",border_color="",corner_radius=10,cursor="hand2")
    back_btn.place(x=5,y=5)
    adminLabel=CTkLabel(admin_frame,text="Admin Detials",font=("Arial",30,"bold"),text_color="white",fg_color="#010721",bg_color="#010721")
    adminLabel.place(x=500,y=10)
    #Admin data Frame
    admindataFrame=CTkFrame(admin_frame,bg_color="#010721",fg_color="#010721")
    admindataFrame.place(x=30,y=110)
    #Admin Labels And Entry
    adminIdLabel=CTkLabel(admindataFrame,text="Id",bg_color="#010721",text_color="white",font=("Arial",35))
    adminIdLabel.grid(row=1,column=1)
    adminIdEntry=CTkEntry(admindataFrame,width=200,height=50,border_width=3,border_color="#080100",corner_radius=8,bg_color="#010721",font=("Arial",20,"bold"))
    adminIdEntry.grid(row=1,column=2,padx=10)
    adminIdEntry.bind("<Return>",focus_next)

    
    adminNameLabel=CTkLabel(admindataFrame,text="Name",bg_color="#010721",text_color="white",font=("Arial",35))
    adminNameLabel.grid(row=2,column=1)
    adminNameEntry=CTkEntry(admindataFrame,width=250,height=50,border_width=3,border_color="#080100",corner_radius=8,bg_color="#010721",font=("Arial",20,"bold"))
    adminNameEntry.grid(row=2,column=2,padx=10,pady=5)
    adminNameEntry.bind("<Return>",focus_next)
    
    admingenderLabel=CTkLabel(admindataFrame,text="Gender",bg_color="#010721",text_color="white",font=("Arial",35))
    admingenderLabel.grid(row=3,column=1)
    admingenderEntry=CTkComboBox(admindataFrame,state="readonly",font=("Arial",25),width=200,values=("Male","Female"),bg_color="#010721")
    admingenderEntry.grid(row=3,column=2,padx=10,pady=5)
    admingenderEntry.set("--Select--")
    admingenderEntry.bind("<Return>",focus_next)

    adminContactLabel=CTkLabel(admindataFrame,text="Contact No",bg_color="#010721",text_color="white",font=("Arial",35))
    adminContactLabel.grid(row=4,column=1)
    adminContactEntry=CTkEntry(admindataFrame,width=250,height=50,border_width=3,border_color="#080100",corner_radius=8,bg_color="#010721",font=("Arial",15,"bold"))
    adminContactEntry.grid(row=4,column=2,padx=10,pady=5)
    adminContactEntry.bind("<Return>",focus_next)

    adminEmailLabel=CTkLabel(admindataFrame,text="Email",bg_color="#010721",text_color="white",font=("Arial",35))
    adminEmailLabel.grid(row=5,column=1)
    adminEmailEntry=CTkEntry(admindataFrame,width=250,height=50,border_width=3,border_color="#080100",corner_radius=8,bg_color="#010721",font=("Arial",15))
    adminEmailEntry.grid(row=5,column=2,padx=10,pady=5)
    adminEmailEntry.bind("<Return>",focus_next)

    adminPasswordLabel=CTkLabel(admindataFrame,text="Password",bg_color="#010721",text_color="white",font=("Arial",35))
    adminPasswordLabel.grid(row=6,column=1)
    adminPasswordEntry=CTkEntry(admindataFrame,width=250,height=50,border_width=3,border_color="#080100",corner_radius=8,show="*",bg_color="#010721",font=("Arial",20))
    adminPasswordEntry.grid(row=6,column=2,padx=10,pady=5)

    #clear Btn
    clear_btn=CTkButton(admindataFrame,text="Clear",font=("Arial",20),width=64,text_color="#645143",fg_color="black",bg_color="#080100",border_width=4,border_color="#800080",corner_radius=12,hover_color="grey",cursor="hand2",command=clear)
    clear_btn.grid(row=7,column=2,padx=10,pady=10,sticky=W)

    #save Btn
    saveImage=CTkImage(Image.open("save.png"),size=(50,50))
    save_btn=CTkButton(admin_frame,image=saveImage,command=save,text=" ",width=70,border_width=3,fg_color="#000d20",bg_color="#000d20",hover_color="#000d20",border_color="#000d20",corner_radius=10,cursor="hand2")
    save_btn.place(x=200,y=550)

    #update Btn
    updateImage=CTkImage(Image.open("update.png"),size=(50,50))
    update_btn=CTkButton(admin_frame,image=updateImage,command=update_fun,text=" ",width=70,border_width=3,fg_color="#000d20",bg_color="#000d20",hover_color="#000d20",border_color="#000d20",corner_radius=10,cursor="hand2")
    update_btn.place(x=290,y=550)

    #delete Btn
    deleteImage=CTkImage(Image.open("delete.png"),size=(50,50))
    delete_btn=CTkButton(admin_frame,image=deleteImage,command=delete_fun,text=" ",width=70,border_width=3,fg_color="#000d20",bg_color="#000d20",hover_color="#000d20",border_color="#000d20",corner_radius=10,cursor="hand2")
    delete_btn.place(x=370,y=550)

    #Tabel Frame
    tabel_frame=CTkFrame(admin_frame,bg_color="#010721",fg_color="#010721")
    tabel_frame.place(x=520,y=100)

    #search by
    search_option=["Id","Name","Gender","Contact No","Email"]
    search_combobox=CTkComboBox(tabel_frame,state="readonly",values=search_option,width=150,height=40,corner_radius=8,bg_color="#010721",font=("Arial",15,"bold"))
    search_combobox.grid(row=0,column=0,pady=20)
    search_combobox.set("Search_by")

    #search Entry
    search_Entry=CTkEntry(tabel_frame,width=200,height=40,corner_radius=8,bg_color="#010721",font=("Arial",15,"bold"))
    search_Entry.grid(row=0,column=1,pady=20)

    #search Button
    search_Btn=CTkButton(tabel_frame,text="Search",command=search_fun,width=100,height=40,font=("Arial",15,"bold"))
    search_Btn.grid(row=0,column=2,pady=20)

    #ShowAll Button
    searchAll_Btn=CTkButton(tabel_frame,text="Show All",command=showall,width=100,height=40,font=("Arial",15,"bold"))
    searchAll_Btn.grid(row=0,column=3,pady=20)

    #Treeview

    tabel=ttk.Treeview(tabel_frame,column=(1,2,3,4,5,6),height=13)
    tabel.grid(row=1,column=0,columnspan=4,pady=20)
    tabel.config(show="headings")
    style=ttk.Style(tabel_frame)
    style.configure("Treeview.Heading", font=("Arial", 18,"bold"))
    style.configure("Treeview",rowheight=30,foreground="white",background="#010721",fieldbackground="#010721",font=("Arial", 18,"bold"))
    style.map("Treeview",background=[("selected","green")])
    tabel.heading(1,text="Id")
    tabel.heading(2,text="Name")
    tabel.heading(3,text="Gender")
    tabel.heading(4,text="Contact No")
    tabel.heading(5,text="Email")
    tabel.heading(6,text="Password")
    tabel.column(1,width=90)
    tabel.column(2,width=200)
    tabel.column(3,width=120)
    tabel.column(4,width=150)
    tabel.column(5,width=230)
    tabel.column(6,width=150)
    tabel.column(1,anchor ='c')
    tabel.column(2,anchor ='c')
    tabel.column(3,anchor ='c')
    tabel.column(4,anchor ='c')
    tabel.column(5,anchor ='c')
    tabel.column(6,anchor ='c')
    tabel.bind("<ButtonRelease>",selection)


    
    
#creating the main Window
app=CTk()
app.title("Employee Management System")
app.geometry("1510x800+0+0")
#Emp Bg Image
image=CTkImage(Image.open("empbg.jpg"),size=(1510,800))
imageLabel=CTkLabel(app,image=image,text=" ")
imageLabel.place(x=0,y=0)

#Employee Mangement System Label
bannerLabel=CTkLabel(app,text="EMPLOYEE MANAGEMENT SYSTEM",font=("Times New Roman",40,"bold"),text_color="white",bg_color="#000d20",fg_color="#000d20")
bannerLabel.place(x=330,y=20)
#Welcome Admin Label
AdminLabel=CTkLabel(app,text="Welcome Admin",font=("Times New Roman",40,"bold"),text_color="white",bg_color="#000d20",fg_color="#000d20")
AdminLabel.place(x=730,y=540)


#Meanu Frame
meanuFrame=CTkFrame(app,bg_color="#000d20",fg_color="#000d20")
meanuFrame.place(x=10,y=80)
#admin Btn Image
adminimage=CTkImage(Image.open("adminImg.png"),size=(100,70))
admin_btn=CTkButton(meanuFrame,image=adminimage,command=admin,text="",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
admin_btn.grid(row=1,column=1)
#Employee Btn Image
EmpImage=CTkImage(Image.open("Emp.png"),size=(100,70))
emp_btn=CTkButton(meanuFrame,image=EmpImage,text="",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
emp_btn.grid(row=2,column=1,pady=20)
#Job Department Btn Image
JobImage=CTkImage(Image.open("jobdtp.png"),size=(100,70))
jobdtp_btn=CTkButton(meanuFrame,image=JobImage,text=" ",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
jobdtp_btn.grid(row=3,column=1,pady=10)

#Employee Qualification Btn Image
QualImage=CTkImage(Image.open("qualification.png"),size=(100,70))
qualification_btn=CTkButton(meanuFrame,image=QualImage,text=" ",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
qualification_btn.grid(row=4,column=1,pady=10)

#Employee salary Btn Image
salaryImage=CTkImage(Image.open("salary.png"),size=(100,70))
salary_btn=CTkButton(meanuFrame,image=salaryImage,text=" ",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
salary_btn.grid(row=5,column=1,pady=10)

#Employee PayRoll Btn Image
PayrollImage=CTkImage(Image.open("payroll.png"),size=(100,70))
payroll_btn=CTkButton(meanuFrame,image=PayrollImage,text=" ",width=100,border_width=2,fg_color="#000d20",bg_color="#000d20",hover_color="#ffffff",border_color="white",corner_radius=10,cursor="hand2")
payroll_btn.grid(row=6,column=1,pady=10)

#Exit Btn Image
ExitImage=CTkImage(Image.open("exit.png"),size=(100,50))
Exit_btn=CTkButton(meanuFrame,image=ExitImage,text=" ",command=exit_fun,width=70,border_width=3,fg_color="#000d20",bg_color="#000d20",hover_color="white",border_color="red",corner_radius=10,cursor="hand2")
Exit_btn.grid(row=7,column=1,pady=10)
#Logout Btn Image
Logout_btn=CTkButton(app,text="LOGOUT ",font=("Arial",23),command=logout,text_color="white",width=20,border_width=5,fg_color="#000d20",bg_color="#000d20",hover_color="grey",border_color="blue",corner_radius=10,cursor="hand2")
Logout_btn.place(x=1340,y=20)


#Run the Application
app.mainloop()

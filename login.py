from tkinter import *
from tkinter import messagebox

#clear fun()
def hide():
    openeye_img.config(file="eye.png")
    password_entry.config(show="*")
    eye_btn.config(command=show)
def show():
    openeye_img.config(file="view.png")
    password_entry.config(show="")
    eye_btn.config(command=hide)    

def clear():
    name_var.set("")
    password_var.set("")
#login fun()
def login():
    name=name_var.get()
    password=password_var.get()
    if(name=="admin"and password=="1234"):
        messagebox.showinfo("welcome","sussesfully login..")
    else:
        messagebox.showerror("Error","Inavild User Name or Password") 
background="#06283D"
#creating main Window
app=Tk()
app.title("Login page")
app.geometry("550x350")
app.config(bg=background)
app.anchor("center")

#creating Labels and Entries
user_name=Label(app,text="Name",fg="white",bg=background,font=("Arial",15,"bold"))
name_var=StringVar()
user_name.grid(row=1,column=4)
user_password=Label(app,text="Password",fg="white",bg=background,font=("Arial",15,"bold"))
password_var=StringVar()
user_password.grid(row=2,column=4)

name_entry=Entry(app,textvariable=name_var,font=("Arial",10,"bold"))
name_entry.grid(row=1,column=5)
password_entry=Entry(app,textvariable=password_var,font=("Arial",10,"bold"))
password_entry.grid(row=2,column=5)
#user image and lock image
loginImg=PhotoImage(file="user-profile.png")
loginImg_label=Label(app,image=loginImg,fg="white",bg=background,text="USER LOGIN",font=("Arial",15,"bold"),compound="top")
loginImg_label.grid(row=0,column=5)
userImg=PhotoImage(file="user.png")
userImg_label=Label(app,image=userImg,bg=background)
userImg_label.grid(row=1,column=3)

lockImg=PhotoImage(file="locked.png")
lockImg_label=Label(app,image=lockImg,bg=background)
lockImg_label.grid(row=2,column=3)
#Button
#Login Button
login_btn=Button(app,text="Login",command=login,fg="white",bg="blue",activeforeground="white",activebackground="blue",cursor="hand2")
login_btn.grid(row=3,column=5,sticky=E,pady=10)
#clear Button
clear_btn=Button(app,text="Clear",command=clear,fg="white",bg="blue",activeforeground="white",activebackground="blue",cursor="hand2")
clear_btn.grid(row=3,column=5,sticky=W,pady=10)
#Eye Button
openeye_img=PhotoImage(file="view.png")
eye_btn=Button(app,image=openeye_img,command=hide,bg=background,activebackground=background,bd=0,cursor="hand2")
eye_btn.grid(row=2,column=6)
#Run the application
app.mainloop()
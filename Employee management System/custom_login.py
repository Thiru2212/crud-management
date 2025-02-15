from customtkinter import *
from PIL import Image
from tkinter import messagebox


#Defining Function
#Clear Btn Fun()
def clear():
    name_entry.delete(0,END)
    password_entry.delete(0,END)
#Login Btn Fun()
def login():
    name=name_var.get()
    password=password_var.get()
    if not name or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if(name=="admin"and password=="1234"):
        messagebox.showinfo("welcome","successfully login..")
        app1.destroy()
        import Emp
    else:
        messagebox.showerror("Error","Inavild User Name or Password")
#Enter event
def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"    
#creating main window
app1=CTk()
app1.title("login page")
app1.geometry("1510x800+0+0")
app1.anchor("center")
#Bg Image
image=CTkImage(Image.open("Imbg.jpg"),size=(1510,800))
imageLabel=CTkLabel(app1,image=image,text=" ")
imageLabel.place(x=0,y=0)
"""Empimage=CTkImage(Image.open("Emplogo.jpg"),size=(200,130))
EmpimageLabel=CTkLabel(app1,image=Empimage,text=" ")
EmpimageLabel.place(x=360,y=60)"""

#Login page Frame

LoginFrame=CTkFrame(app1,width=400,height=290,bg_color="#080100",fg_color="#080100",corner_radius=20,border_width=4,border_color="white")
LoginFrame.place(x=600,y=100)


#creating Labels and Entries

loginLabel=CTkLabel(LoginFrame,text="Login Page",bg_color="#080100",text_color="#645143",font=("Times New Roman",40,"bold"))
loginLabel.place(x=110,y=10)
user_name=CTkLabel(LoginFrame,text="Name",bg_color="#080100",text_color="#645143",font=("Arial",35))
name_var=StringVar()
user_name.place(x=20,y=90)
user_password=CTkLabel(LoginFrame,text="Password",bg_color="#080100",text_color="#645143",font=("Arial",35))
password_var=StringVar()
user_password.place(x=20,y=160)

name_entry=CTkEntry(LoginFrame,textvariable=name_var,text_color="#080100",fg_color="grey",bg_color="black",font=("Arial",30),border_width=3,border_color="white",width=200,corner_radius=8)
name_entry.place(x=180,y=90)
name_entry.bind("<Return>",focus_next)
password_entry=CTkEntry(LoginFrame,textvariable=password_var,text_color="#080100",fg_color="grey",show="*",bg_color="black",font=("Arial",30),border_width=3,border_color="white",width=200,corner_radius=8)
password_entry.place(x=180,y=160)
#creating CTkButtons
#login button
login_btn=CTkButton(LoginFrame,text="Login",font=("Arial",20),width=64,text_color="#645143",fg_color="black",bg_color="#080100",border_width=4,border_color="#800080",corner_radius=12,hover_color="grey",cursor="hand2",command=login)
login_btn.place(x=290,y=220)
#clear button
clear_btn=CTkButton(LoginFrame,text="Clear",font=("Arial",20),width=64,text_color="#645143",fg_color="black",bg_color="#080100",border_width=4,border_color="#800080",corner_radius=12,hover_color="grey",cursor="hand2",command=clear)
clear_btn.place(x=190,y=220)
app1.mainloop()

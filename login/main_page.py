
import tkinter as tk
import mysql.connector as sql
import edits

try:
    connection = sql.connect(user="root",password="",host="localhost")
    cursor = connection.cursor()
    cursor.execute("create database login")
    connection.commit()
    connection = sql.connect(user="root",password="",host="localhost",database="login")
    cursor = connection.cursor()
    cursor.execute("create table user_data(user_name varchar(500),password varchar(500),age int,gender varchar(500));")
except Exception as e:
    print(e)

def show_password():
    global user_password_E,show_password_btn
    user_password_E.config(show="")
    show_password_btn.config(text="hide password",command=hide_password)

def hide_password():
    global user_password_E,show_password_btn
    user_password_E.config(show="*")
    show_password_btn.config(text="show password",command=show_password)
    pass

window = tk.Tk()
window.geometry("500x500")
window.resizable(False,False)
window.title("login page")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

option_menu = tk.Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(label="option",menu=option_menu)
option_menu.add_command(label="delete account")# command=delete_account ==> make command
option_menu.add_command(label="rename")# command=rename_account ==> make command
option_menu.add_command(label="change password")# command=change_password ==> make command
option_menu.add_command(label="change age")# command=change_age ==> make command
option_menu.add_command(label="change gender")# command=change_gender ==> make command


user_name_L = tk.Label(window,
                       text="user name:",
                       font=("Arial",15))
user_name_L.place(x=200,y=100,anchor="e")

user_name_E = tk.Entry(window,
                       width=18,
                       font=("Arial",15),
                       foreground="#098082",
                       justify="center")
user_name_E.place(x=350,y=100,anchor="center")

user_password_L = tk.Label(window,
                           text="user password:",
                           font=("Arial",15))
user_password_L.place(x=200,y=140,anchor="e")

user_password_E = tk.Entry(window,
                           width=18,
                           font=("Arial",15),
                           foreground="#098082",
                           justify="center",
                           show="*")
user_password_E.place(x=350,y=140,anchor="center")

show_password_btn = tk.Button(window,
                              text="show password",
                              font=("Arial",13),
                              width=18,
                              background="#FFFFFF",
                              command=show_password)
show_password_btn.place(x=350,y=180,anchor="center")

user_age_L = tk.Label(window,
                      text="user age:",
                      font=("Arial",15))
user_age_L.place(x=200,y=230,anchor="e")

user_age_S = tk.Scale(window,
                      from_=10,
                      to=100,
                      length=160,
                      orient="horizontal")
user_age_S.place(x=350,y=225,anchor="center")

gender_L = tk.Label(window,
                    text="user gender:",
                    font=("Arial",15))
gender_L.place(x=200,y=270,anchor="e")

user_gender = tk.StringVar(value=False)
check_btn_male = tk.Checkbutton(window,
                                text="male",
                                font=("Arial",15),
                                onvalue="male",
                                variable=user_gender)
check_btn_male.place(x=270,y=270,anchor="center")

check_btn_female = tk.Checkbutton(window,
                                  text="female",
                                  font=("Arial",15),
                                  onvalue="female",
                                  variable=user_gender)
check_btn_female.place(x=370,y=270,anchor="center")

login_btn = tk.Button(window,
                      text="login",
                      font=("Arial",15),
                      background="#36BB24",
                      foreground="#FFFFFF",
                      activebackground="#2B931D",
                      activeforeground="#DDDDDD")
login_btn.place(x=310,y=370,anchor="center",width=90,height=70)

signup_btn = tk.Button(window,
                      text="signup",
                      font=("Arial",15),
                      background="#246DBB",
                      foreground="#FFFFFF",
                      activebackground="#1E5897",
                      activeforeground="#DDDDDD")
signup_btn.place(x=200,y=370,anchor="center",width=90,height=70)

exit_btn = tk.Button(window,
                     text="Exit",
                     font=("Arial",16),
                     background="#B12F2F",
                     foreground="#FFFFFF",
                     activebackground="#961F1F",
                     activeforeground="#FFFFFF",
                     command=window.destroy)
exit_btn.place(x=450,y=450,anchor="center",height=70,width=70)

window.mainloop()
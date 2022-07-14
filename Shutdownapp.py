from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -1")


def shutdown():
    os.system("shutdown/s /t 1")


st = Tk()
st.title('ShutDown')
st.geometry('500x500')
st.config(bg='olive')
r_button = Button(st, text='Restart', font=('TAHOMA', 17, 'underline'), relief=RAISED, cursor='plus',
                  activebackground='orange', command=restart)
r_button.place(x=150, y=50, height=50, width=200)

r_button = Button(st, text='Restart Time', font=('TAHOMA', 17, 'underline'), relief=RAISED, cursor='plus',
                  activebackground='orange', command=restart_time)
r_button.place(x=150, y=150, height=50, width=200)

r_button = Button(st, text='Log-Out', font=('TAHOMA', 17, 'underline'), relief=RAISED, cursor='plus',
                  activebackground='orange', command=logout)
r_button.place(x=150, y=250, height=50, width=200)

r_button = Button(st, text='ShutDown', font=('TAHOMA', 17, 'underline'), relief=RAISED, cursor='plus',
                  activebackground='orange', command=shutdown)
r_button.place(x=150, y=350, height=50, width=200)

st.mainloop()

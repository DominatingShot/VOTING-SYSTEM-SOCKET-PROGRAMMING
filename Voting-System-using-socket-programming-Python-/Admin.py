import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from PIL import ImageTk, Image
from registerVoter import *
from admFunc import *

# Function to display the Admin home page
def AdminHome(root, frame1, frame3):
    root.title("Admin")
    
    # Clear existing widgets in frame1
    for widget in frame1.winfo_children():
        widget.destroy()

    # Button to navigate back to the Admin home page
    Button(frame3, text="Admin", command=lambda: AdminHome(root, frame1, frame3)).grid(row=1, column=0)
    frame3.pack(side=TOP)

    # Header and spacing
    Label(frame1, text="Admin", font=('Helvetica', 25, 'bold')).grid(row=0, column=1)
    Label(frame1, text="").grid(row=1, column=0)

    # Buttons for various admin actions
    runServer = Button(frame1, text="Run Server", width=15, command=lambda: sb_p.Popen('python3 Voting-System-using-socket-programming-Python-/Server.py', shell=True))
    registerVoter = Button(frame1, text="Register Voter", width=15, command=lambda: regV.Register(root, frame1))
    showVotes = Button(frame1, text="Show Votes", width=15, command=lambda: adFunc.showVotes(root, frame1))
    reset = Button(frame1, text="Reset All", width=15, command=lambda: adFunc.resetAll(root, frame1))

    # Add spacing between buttons
    Label(frame1, text="").grid(row=2, column=0)
    Label(frame1, text="").grid(row=4, column=0)
    Label(frame1, text="").grid(row=6, column=0)
    Label(frame1, text="").grid(row=8, column=0)

    # Place buttons in the grid
    runServer.grid(row=3, column=1, columnspan=2)
    registerVoter.grid(row=5, column=1, columnspan=2)
    showVotes.grid(row=7, column=1, columnspan=2)
    reset.grid(row=9, column=1, columnspan=2)

    # Pack the frame and start the Tkinter event loop
    frame1.pack()
    root.mainloop()

# Function to check admin credentials and navigate to the Admin home page
def log_admin(root, frame1, admin_ID, password):
    if admin_ID == "admin" and password == "admin":
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect", width=500)
        msg.grid(row=6, column=0, columnspan=5)

# Function to display the Admin login page
def AdmLogin(root, frame1):
    root.title("Admin Login")
    
    # Clear existing widgets in frame1
    for widget in frame1.winfo_children():
        widget.destroy()

    # Header and spacing
    Label(frame1, text="Admin Login", font=('Helvetica', 18, 'bold')).grid(row=0, column=2, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    # Labels and entry widgets for Admin ID and Password
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT).grid(row=2, column=0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT).grid(row=3, column=0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable=admin_ID)
    e1.grid(row=2, column=2)
    e2 = Entry(frame1, textvariable=password, show='*')
    e2.grid(row=3, column=2)

    # Button for Admin login
    sub = Button(frame1, text="Login", width=10, command=lambda: log_admin(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="").grid(row=4, column=0)
    sub.grid(row=5, column=3, columnspan=2)

    # Pack the frame and start the Tkinter event loop
    frame1.pack()
    root.mainloop()

# Entry point for the application
if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    frame3 = Frame(root)
    
    # Start with the Admin home page
    AdminHome(root, frame1, frame3)

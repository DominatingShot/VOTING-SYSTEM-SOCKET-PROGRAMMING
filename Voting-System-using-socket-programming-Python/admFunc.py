import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from pathlib import Path
from PIL import ImageTk, Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")
    path = Path('/mnt/c/Users/aksha/Desktop/NETWORK ASSIGNMENT/Voting-System-using-socket-programming-Python-/img')
    bjpLogo = ImageTk.PhotoImage(Image.open(path / 'bjp.png').resize((35, 35)))
    bjpImg = Label(frame1, image=bjpLogo)
    bjpImg.grid(row=2, column=0)

    congLogo = ImageTk.PhotoImage(Image.open(path / 'cong.jpg').resize((25, 38)))
    congImg = Label(frame1, image=congLogo)
    congImg.grid(row=3, column=0)

    aapLogo = ImageTk.PhotoImage(Image.open(path / 'aap.png').resize((45, 30)))
    aapImg = Label(frame1, image=aapLogo)
    aapImg.grid(row=4, column=0)

    ssLogo = ImageTk.PhotoImage(Image.open(path / 'ss.png').resize((40, 35)))
    ssImg = Label(frame1, image=ssLogo)
    ssImg.grid(row=5, column=0)

    notaLogo = ImageTk.PhotoImage(Image.open(path / 'nota.jpg').resize((35, 25)))
    notaImg = Label(frame1, image=notaLogo)
    notaImg.grid(row=6, column=0)


    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)

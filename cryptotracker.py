import tkinter as tk
import tkinter.messagebox as messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk
from DatabaseMgmt.databaseMgmt import DatabaseMgmt
from Logic.calc import Calc 

class Budgetplan(ctk.CTk):
    DM = DatabaseMgmt()
    CB = Calc()

    def __init__(self):
        super().__init__()

        self.title('Cryptotracker')
        self.geometry('1200x600')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frames = []
        self.createMainFrame()
        
    def createMainFrame(self):
        column = ['Coin', 'Betrag', 'Menge', 'Durch. Kaufpreis', 'Jetziger Preis', 'Gewinn/Verlust']
        self.entryCoinIDMapping = {}
        self.entryTransactionIDMapping = {}
        
        self.mainFrame = ctk.CTkFrame(master=self)
        self.mainFrame.place(x=0, y=0, relwidth=1, relheight=1)

        leftFrame = ctk.CTkFrame(master=self.mainFrame, corner_radius=0)
        leftFrame.place(x=10, y=20, anchor='nw', relheight=0.8)
        leftFrame.configure(width=200)

        labelTitle = ctk.CTkLabel(master=leftFrame, text='Cryptotracker', font=("Roboto" ,24))
        labelTitle.place(relx=0.5, y=20, anchor='center')

        btnAddTransaction = ctk.CTkButton(master=leftFrame, text="Neue Zahlung", command=self.TransactionWindow)
        btnAddTransaction.place(relx=0.5, y=100, anchor='center')
        btnAddTransaction.configure(width=100, height=30)

        btnAddCoin = ctk.CTkButton(master=leftFrame, text="Neuer Coin")
        btnAddCoin.place(relx=0.5, y=150, anchor='center')
        btnAddCoin.configure(width=100, height=30)

        self.rightFrame = ctk.CTkFrame(master=self.mainFrame)
        self.rightFrame.place(x=220, y=20, anchor='nw', relwidth=0.7, relheight=0.8)

        self.tableCoins = ttk.Treeview(master=self.rightFrame)
        self.tableCoins["columns"] = column
        
        for col in column:
            self.tableCoins.column(col, width=150)
            self.tableCoins.heading(col, text=col.capitalize())
        self.tableCoins["show"] = "headings"
        self.tableCoins.pack(pady=20)

        self.frames.append(self.mainFrame)

    def TransactionWindow(self):
        for frame in self.frames:
            frame.destroy()
        
        frameTransaction = ctk.CTkFrame(self)
        frameTransaction.place(x=10, y=20, anchor='nw', relheight=0.8)
        self.frames.append(frameTransaction)

        label = ctk.CTkLabel(master=frameTransaction, text="Neue Transaktion", font=("Roboto" ,24))
        label.place(x=20)


# run app
app = Budgetplan()
app.mainloop()
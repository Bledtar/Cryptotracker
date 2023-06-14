import tkinter as tk
import tkinter.messagebox as messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk
from DatabaseMgmt.databaseMgmt import DatabaseMgmt
from Logic.calc import Calc 

class Cointracker(ctk.CTk):
    DM = DatabaseMgmt()
    CB = Calc()

    def back(self):
        if len(self.frames) > 1:
            self.frames[-1].pack_forget()  # Hide the current frame
            self.frames.pop()  # Remove the current frame from the list
        if self.frames:
            self.frames[-1].place()



    def __init__(self):
        super().__init__()

        self.title('Cryptotracker')
        self.geometry('1300x600')

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

        btnAddCoin = ctk.CTkButton(master=leftFrame, text="Neuer Coin", command=self.CoinWindow)
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

    def CoinWindow(self):
        for frame in self.frames:
            frame.destroy()
        
        column = ['Coin']

        frameCoin = ctk.CTkFrame(self)
        frameCoin.pack(fill='both', anchor='center', padx=100)
        self.frames.append(frameCoin)

        label = ctk.CTkLabel(master=frameCoin, text="Neuer Coin", font=("Roboto" ,24))
        label.grid(pady=10)

        self.entryCategory = ctk.CTkEntry(master=frameCoin, placeholder_text="Coin")
        self.entryCategory.grid(pady=10)

        self.btnSaveCoin = ctk.CTkButton(master=frameCoin, text="Speichern")
        self.btnSaveCoin.grid(pady=10)

        self.tableCoins = ttk.Treeview(master=frameCoin)
        self.tableCoins["columns"] = column

        for col in column:
            self.tableCoins.column(col, width=150)
            self.tableCoins.heading(col, text=col.capitalize())
        self.tableCoins["show"] = "headings"
        self.tableCoins.grid(pady=10)

        self.btnDeleteCoin = ctk.CTkButton(master=frameCoin, text="Löschen")
        self.btnDeleteCoin.grid(pady=10)

        self.btnBack = ctk.CTkButton(master=frameCoin, text="Zurück", command=self.back)
        self.btnBack.grid(pady=10)

# run app
app = Cointracker()
app.mainloop()
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
        self.geometry('800x800')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frames = []
        self.createMainFrame()
        
    def createMainFrame(self):
        column = ['Coin', 'Menge', 'Durch. Kaufpreis', 'Jetziger Preis', 'Gewinn/Verlust']
        self.entryBudgetIDMapping = {}
        self.entryCategoryIDMapping = {}
        
        mainFrame = ctk.CTkFrame(master=self)
        mainFrame.place()

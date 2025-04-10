
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mariadb, sys

class Datenbank():#Class
    def __init__(self):
        self.artikelnummer = None
        self.Lieferant = None
        self.Artikelname = None
        self.Preis = None
        self.Lagerbestand = None
        self.sqleingabe = None
        self.anrede = None

#Datenbank
try:#connect
    conn = mariadb.connect(
        user = "LNRD",
        password = "SWEDswed11",
        host = "localhost",
        port = 3306,
        database = "schlumpfshop3")
 
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PLatform: {e}")
    sys.exit(1)



cur = conn.cursor()
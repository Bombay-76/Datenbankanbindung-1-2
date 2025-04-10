#Grafik
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#Datenbank
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

#Grafischeoberfläche
root = tk.Tk()
root.title("DatenBank")
w = 600
h = 500

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (w/2)

root.geometry('%dx%d+%d+%d' % (w,h,x,y))

root = tk.Tk()
root.title("Beispiel")

eingabe_var = tk.StringVar()

entry = tk.Entry(root, textvariable=eingabe_var)
entry.pack(pady=10)

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
#get cursor
cur = conn.cursor()
#"SELECT artikel.Artikelname, artikel.Preis_Netto, artikel.Lagerbestand, lieferant.Lieferantenname FROM artikel INNER JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant;"
cur.execute(
    "SELECT * FROM anrede WHERE anrede = 'divers';"
    )
#insert into andrede (andrede.Anrede) values ("arschnase")

ttk.Label(root, text = "artieklnummer: {Datenbank.artikelnummer} \t Lieferant: {Datenbank.Lieferant} \t Artikelname: {Datenbank.Artikelname} \t Preis: {Datenbank.Preis} \t Lagerbestand: {Datenbank.Lagerbestand} \t Lieferant: {Datenbank.Lieferant}").pack()

for (Datenbank.anrede) in cur:
    ttk.Label(root, text= f"{Datenbank.anrede}").pack()

root.mainloop()
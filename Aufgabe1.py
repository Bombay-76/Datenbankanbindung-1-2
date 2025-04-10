#Aufgabe3*
#Grafik
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#Datenbank
import mariadb, sys

class Datenbank():#Class
    def __init__(self):
        self.tel = "0"
        self.vorname = ""
        self.nachname = ""
        self.eingabe = None
        self.anrede = None
        self.alter = "0"

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

#AnredeListe
alter_liste = []

#Funktion spreichern
def anrede_speichern():
    Datenbank.eingabe = entry.get()
    if Datenbank.eingabe.strip() == None:
        messagebox.showwarning("Bitte ein alter eingeben.")
        return
    
#speichern
    alter_liste.append(Datenbank.eingabe)
    
    try:
        cur.execute(f"SELECT vorname, nachname, geburtstag, TIMESTAMPDIFF(YEAR, geburtstag, CURDATE()) AS alter FROM kunden WHERE TIMESTAMPDIFF(YEAR, geburtstag, CURDATE()) < {Datenbank.eingabe};", (Datenbank.eingabe,))
        conn.commit()
        messagebox.showinfo("sehr schön", f"Anrede '{Datenbank.anrede},")
        entry.delete(0, tk.END)
    except mariadb.Error as e:
        messagebox.showerror("Datenbankfehler", f"Fehler beim Speichern: {e}")

#grafik
root = tk.Tk()
root.title("Anrede speichern")
root.geometry("400x200")

#lb
label = tk.Label(root, text="Bitte Alter eingeben:")
label.pack(pady=10)

#tb
entry = tk.Entry(root)
entry.pack(pady=5)

#bn
button = tk.Button(root, text="Speichern", command=anrede_speichern)
button.pack(pady=10)

root.mainloop()
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

# Anrede-Liste (zum Zwischenspeichern)
anrede_liste = []

# Funktion spreichern
def anrede_speichern():
    eingabe = entry.get()
    if eingabe.strip() == "":
        messagebox.showwarning("Fehler", "Bitte eine Anrede eingeben.")
        return

#speichern
    anrede_liste.append(eingabe)

    try:
        cur.execute("INSERT INTO anrede (anrede) VALUES (?)", (eingabe,))
        conn.commit()
        messagebox.showinfo("Erfolg", f"Anrede '{eingabe}' gespeichert.")
        entry.delete(0, tk.END)
    except mariadb.Error as e:
        messagebox.showerror("Datenbankfehler", f"Fehler beim Speichern: {e}")

#grafik
root = tk.Tk()
root.title("Anrede speichern")
root.geometry("400x200")

#lb
label = tk.Label(root, text="Bitte Anrede eingeben:")
label.pack(pady=10)

#tb
entry = tk.Entry(root)
entry.pack(pady=5)

#bn
button = tk.Button(root, text="Speichern", command=anrede_speichern)
button.pack(pady=10)

root.mainloop()
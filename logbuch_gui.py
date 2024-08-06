import tkinter as tk
from tkinter import messagebox
import logbuch_db

def add_entry():
    eintrag = entry_text.get("1.0", "end").strip()
    if eintrag:
        logbuch_db.add_entry(eintrag)
        entry_text.delete("1.0", "end")
        show_entries()
    else:
        messagebox.showwarning("Warnung", "Der Eintrag darf nicht leer sein.")

def show_entries():
    entries = logbuch_db.get_entries()
    log_list.delete(0, tk.END)
    for row in entries:
        log_list.insert(tk.END, f"{row[0]}: {row[1]}")

# GUI erstellen
root = tk.Tk()
root.title("Logbuch")

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)
entry_text = tk.Text(entry_frame, height=4, width=50)
entry_text.pack(side="left", padx=5)
add_button = tk.Button(entry_frame, text="Eintrag hinzufügen", command=add_entry)
add_button.pack(side="right", padx=5)

log_list = tk.Listbox(root, width=60)
log_list.pack(pady=10)

logbuch_db.init_db()
show_entries()
root.mainloop()

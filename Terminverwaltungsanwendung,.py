from tkinter import *
import time
from pymongo import MongoClient

def mark_done(event_item):
    event_text = event_item.split(":")[1].strip()
    collection.delete_one({"event": event_text})
    events_listbox.delete(events_listbox.curselection())

def update_events_list():
    events_listbox.delete(0, END)
    for event_data in collection.find():
        events_listbox.insert(END, f"{event_data['time']}: {event_data['event']}")

# Verbindung zur MongoDB-Datenbank herstellen
client = MongoClient("mongodb://localhost:27017/")
db = client["termine"]
collection = db["events"]

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

def update_date():
    current_date = time.strftime('%A, %d.%m.%Y')
    date_label.config(text=current_date)
    date_label.after(86400000, update_date)

def add_event():
    event = event_entry.get()
    time = time_entry.get()
    events_listbox.insert(END, f"{time}: {event}")
    event_entry.delete(0, END)
    time_entry.delete(0, END)
    
    # Termin in die MongoDB-Datenbank einfügen
    event_data = {"time": time, "event": event}
    collection.insert_one(event_data)

# GUI Setup
window = Tk()
window.title('Terminverwaltung')
window.geometry('600x400')

# Digital Clock
clock_label = Label(window, text="", font=('Arial', 30))
clock_label.pack(pady=10)
update_time()

date_label = Label(window, text="", font=('Arial', 18))
date_label.pack()
update_date()

# Event Entry
event_label = Label(window, text="Termin:")
event_label.pack()
event_entry = Entry(window, font=('Arial', 14))
event_entry.pack()

time_label = Label(window, text="Uhrzeit (HH:MM):")
time_label.pack()
time_entry = Entry(window, font=('Arial', 14))
time_entry.pack()

add_button = Button(window, text="Termin hinzufügen", command=add_event)
add_button.pack(pady=10)

# Event List
events_listbox = Listbox(window, font=('Arial', 14), height=8, width=40)
events_listbox.pack(pady=20)

mark_done_button = Button(window, text="Mark as Done", command=lambda: mark_done(events_listbox.get(ACTIVE)))
mark_done_button.pack()

update_events_list()

window.mainloop()

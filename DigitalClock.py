from tkinter import *
import time

def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    myLabel.config(text=current_time)
    myLabel.after(1000, update_time)

def update_date():
    current_date = time.strftime('%A, %d.%m.%Y')
    myLabel2.config(text=current_date)
    myLabel2.after(86400000, update_date)  # Aktualisiere alle 24 Stunden

window = Tk()
window.title('Digital Clock')
window.geometry('600x400')
window.configure(bg='black')  # Hintergrundfarbe einstellen

myLabel = Label(window, text="", font=('Arial', 60), fg='white', bg='black')
myLabel.pack(pady=50)  # Abstand nach oben und unten

myLabel2 = Label(window, text="", font=("Arial", 24), fg='black', bg='yellow')
myLabel2.pack()

update_time()
update_date()

window.mainloop()

from re import T
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk

#Galvenā loga izveide
logs = Tk()
logs.geometry("350x400")
logs.title("Instrumentu noma")
logs.configure(background = "#FFE1E9")

logo_frame = tk.Frame(logs)
logo_frame.grid(row=1, column=0, columnspan=10, padx=60, pady=5)
logo_image = Image.open("pink.png")
resized_logo = logo_image.resize((200,200))
logo = ImageTk.PhotoImage(resized_logo)
logo_label = ttk.Label(logo_frame, image=logo)
logo_label.grid(row=1, column=1, columnspan=10, padx=10, pady=5 )

btn=Button(logs, text="Pasūtījums", bd='5', command = lambda: pasutijums()) 
btn1=Button(logs, text="Aizvērt", bd='5', command=logs.destroy)
btn.grid(row=5, column=1, padx=60, pady=30)
btn1.grid(row=5, column=2, padx=0, pady=30)

def pasutijums():
    logs1 = Toplevel()
    logs1.geometry("350x400")
    logs1.title("Pasūtījums")
    logs1.configure(background = "#FFE1E9")

    ttk.Label(logs1, text=("Izvēlēties darbinieku:")).grid(column=4, row=1, pady=5, padx=5)
    ttk.Label(logs1, text=("Izvēlies instrumentu:")).grid(column=4, row=2, pady=5, padx=5)
    ttk.Label(logs1, text=("Norādi cenu:")).grid(column=4, row=3, pady=5, padx=5)
    ttk.Label(logs1, text=("Norādi dienas:")).grid(column=4, row=4, pady=5, padx=5)

    vardsuzvards=tk.StringVar()
    instruments=tk.StringVar()
    cena=tk.StringVar()
    dienas=tk.StringVar()

    darbinieki =ttk.Combobox(logs1, textvariable=vardsuzvards)
    instrumenti=ttk.Combobox(logs1, textvariable=instruments)
    cena_i=ttk.Combobox(logs1, textvariable=cena)
    dienas_i=ttk.Entry(logs1, textvariable=dienas)

    darbinieki['values']=('Kārlis Bērziņš','Pēteris Zāle', 'Asafs Alpe', 'Markuss Liepiņš' )
    instrumenti['values']=('Urbis', 'Slīpmašīna', 'Zāģis')
    cena_i['values']=('50', '20', '40')
    
    darbinieki.grid(column=6, row=1, pady=5)
    instrumenti.grid(column=6, row=2, pady=5)
    cena_i.grid(column=6, row=3, pady=5)
    dienas_i.grid(column=6, row=4, pady=5)
    







logs.mainloop()
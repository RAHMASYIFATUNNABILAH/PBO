import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())

    L = round(2 * p * l) + (2 * p * t) + (2 * l * t)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())

    v = round(p * l * t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label(frame, text="Rahma syifatun / 221511013 / R4")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Panjang
panjang= Label(frame, text="Panjang :")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar= Label(frame, text="Lebar :")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi= Label(frame, text="Tinggi :")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=2, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
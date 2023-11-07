import tkinter as tk
from math import pi

def hitung_luas():
    try:
        radius = float(entryRadius.get())
        height = float(entryHeight.get())
        s = (radius * 2 + height * 2) ** 0.5
        luas = pi * radius * (radius + 5)
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, f'Luas: (luas:.2f) satuan persgi')

    except ValueError:
        textLuas.delete('1.0', tk.END)
        textLuas.insert(tk.END, 'Masukkan angka yang valid')

def hitung_volume():
    try:
        radius = float(entryRadius.get())
        height = float(entryHeight.get())
        volume = (1/3) * pi * radius ** 2 * height
        textvolume.delete('1.0', tk.END)
        textvolume.insert(tk.END, f'Volume: (volume:.2f) satuan kubik')

    except ValueError:
        textvolume.delete('1.0', tk.END)
        textvolume.insert(tk.END, 'Masukkan angka yang valid')

app = tk.Tk()
app.title("Kalkulator Kerucut")
app.geometry('300x300')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

labelRadius = tk.Label(frame, text="Jari-Jari: ", font=('Arial', 12))
labelRadius.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entryRadius = tk.Entry(frame, font=('Arial', 12))
entryRadius.grid(row=0, column=1)

labelHeight = tk.Label(frame, text="Tinggi; ", font=('Arial', 12))
labelHeight.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entryHeight = tk.Entry(frame, font=('Arial', 12))
entryHeight.grid(row=1, column=1)

luasButton = tk.Button(frame, text="Hitung Luas", command=hitung_luas, font=('Arial', 12))
luasButton.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

volumeButton = tk.Button(frame, text="Hitung Volume", command=hitung_volume,  font=('Arial', 12))
volumeButton.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

textLuas = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textLuas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

textvolume = tk.Text(frame, height=2, width=30, font=('Arial', 12))
textvolume.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
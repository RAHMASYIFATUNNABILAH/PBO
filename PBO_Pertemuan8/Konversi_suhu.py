import tkinter as tk
from tkinter import ttk

class Suhu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Judul Aplikasi
        self.title = ttk.Label(self, text="Aplikasi Suhu")
        self.title.pack(padx=10, pady=10)

        # Label Celcius
        self.label_celcius = ttk.Label(self, text="Celcius")
        self.label_celcius.pack()

        # Entry Celcius
        self.entry_celcius = ttk.Entry(self)
        self.entry_celcius.pack()

        # Label Fahrenheit
        self.label_fahrenheit = ttk.Label(self, text="Fahrenheit")
        self.label_fahrenheit.pack()

        # Label Reamur
        self.label_reamur = ttk.Label(self, text="Reamur")
        self.label_reamur.pack()

        # Label Kelvin
        self.label_kelvin = ttk.Label(self, text="Kelvin")
        self.label_kelvin.pack()

        # Button Konversi
        self.button_konversi = ttk.Button(self, text="Konversi", command=self.on_click)
        self.button_konversi.pack()

        # Label Hasil Konversi
        self.label_hasil_konversi = ttk.Label(self)
        self.label_hasil_konversi.pack()

    def on_click(self):
        # Ambil nilai dari entry Celcius
        celcius = float(self.entry_celcius.get())

        # Konversi ke Fahrenheit
        fahrenheit = (celcius * 9/5) + 32

        # Konversi ke Reamur
        reamur = (celcius * 4/5)

        # Konversi ke Kelvin
        kelvin = celcius + 273.15

        # Set nilai hasil konversi
        self.label_hasil_konversi.config(text="Fahrenheit: {0}\nReamur: {1}\nKelvin: {2}".format(fahrenheit, reamur, kelvin))

root = tk.Tk()
suhu = Suhu(root)
root.mainloop()

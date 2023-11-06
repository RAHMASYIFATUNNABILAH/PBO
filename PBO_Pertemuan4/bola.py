import tkinter as tk
import math

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())
        luas_permukaan = 4 * math.pi * jari_jari **2
        volume = (4/3) * math.pi * jari_jari**3

        label_hasil.config(text=f"Luas Permukaa: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan tidak valid.Pastikan Anda memasukkan angka.")

#Membuat Windows
root = tk.Tk()
root.title("Kalkulator Bola")

#Membuat Label
label_jari_jari = tk.Label(root, text="Jari-jari Bola:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

#Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.pack()

#Label menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()
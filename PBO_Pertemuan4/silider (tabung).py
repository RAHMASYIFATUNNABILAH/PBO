import tkinter as tk
import math

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        volume = math.pi * jari_jari**2 * tinggi

        label_hasil.config(text=f"Luas Permukaa: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan tidak valid.Pastikan Anda memasukkan angka.")

#Membuat Windows
root = tk.Tk()
root.title("Kalkulator Tabung")

#Membuat Label
label_jari_jari = tk.Label(root, text="Jari-jari:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

label_tinggi = tk.Label(root, text=" Tinggi:")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

#Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.pack()

#Label menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

root.mainloop()

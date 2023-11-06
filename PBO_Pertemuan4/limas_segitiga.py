import tkinter as tk
import math

def hitung():
    try:
        alas = float(entry_alas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        
        luas_permukaan = (alas * tinggi_limas) + (3 * alas * tinggi_alas)
        volume = (1/3) * alas * tinggi_alas * tinggi_limas

        label_hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan tidak valid.Pastikan Anda memasukkan angka.")

#Membuat windows
root = tk.Tk()
root.title("Kalkulator Limas Segitiga")

#Membuat label dan input untuk panjang alas, lebar alas, tinggi limas, dan tinggi segitiga
label_alas = tk.Label(root, text="Alas Segitiga:")
label_alas.pack()
entry_alas = tk.Entry(root)
entry_alas.pack()

label_tinggi_alas = tk.Label(root, text="Tinggi Alas Segitiga:")
label_tinggi_alas.pack()
entry_tinggi_alas = tk.Entry(root)
entry_tinggi_alas.pack()

label_tinggi_limas = tk.Label(root, text="Tinggi Limas")
label_tinggi_limas.pack()
entry_tinggi_limas= tk.Entry(root)
entry_tinggi_limas.pack()

#Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung",command=hitung)
btn_hitung.pack()

#Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

#Menjalankan Aplikasi
root.mainloop()
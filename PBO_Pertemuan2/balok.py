import tkinter as tk

def hitung():
    try:
        panjang = float(entry_panjang.get())
        lebar  = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())

        luas_permukaan = ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
        volume = panjang * lebar * tinggi

        label_hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan tidak valid.Pastikan Anda memasukkan angka.")

#Membuat windows
root = tk.Tk()
root.title("Kalkulator Balok")

#Membuat label dan input untuk panjang alas, lebar alas, tinggi limas, dan tinggi segitiga
label_panjang = tk.Label(root, text="Panjang:")
label_panjang.pack()
entry_panjang = tk.Entry(root)
entry_panjang.pack()

label_lebar = tk.Label(root, text="Lebar:")
label_lebar.pack()
entry_lebar = tk.Entry(root)
entry_lebar.pack()

label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

#Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung",command=hitung)
btn_hitung.pack()

#Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

#Menjalankan Aplikasi
root.mainloop()
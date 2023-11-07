import tkinter as tk

def hitung():
    try:
        panjang_alas =float(entry_panjang_alas.get())
        lebar_alas = float(entry_lebar_alas.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())

        luas_permukaan = (panjang_alas * lebar_alas) + (panjang_alas * tinggi_segitiga * 2) + (lebar_alas * tinggi_segitiga * 2)
        volume = (panjang_alas * lebar_alas * tinggi_limas) / 3

        label_hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        label_hasil.config(text="Masukkan tidak valid.Pastikan Anda memasukkan angka.")

#Membuat windows
root = tk.Tk()
root.title("Kalkulator Limas Segiempat")

#Membuat label dan input untuk panjang alas, lebar alas, tinggi limas, dan tinggi segitiga
label_panjang_alas = tk.Label(root, text="Panjang Alas:")
label_panjang_alas.pack()
entry_panjang_alas = tk.Entry(root)
entry_panjang_alas.pack()

label_lebar_alas = tk.Label(root, text="Lebar Alas:")
label_lebar_alas.pack()
entry_lebar_alas = tk.Entry(root)
entry_lebar_alas.pack()

label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(root)
entry_tinggi_limas.pack()

label_tinggi_segitiga = tk.Label(root, text="Tinggi Segitiga Alas")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga= tk.Entry(root)
entry_tinggi_segitiga.pack()

#Tombol untuk menghitung
btn_hitung = tk.Button(root, text="Hitung",command=hitung)
btn_hitung.pack()

#Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack()

#Menjalankan Apl
root.mainloop()
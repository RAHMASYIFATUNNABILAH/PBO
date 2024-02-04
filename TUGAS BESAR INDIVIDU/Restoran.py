import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Data makanan dan minuman + tarifnya
menu = {
    'Ikan Bakar': 35000,
    'Ayam Bakar': 25000,
    'Ayam Goreng': 30000,
    'Nasi Goreng': 25000,
    'Soto Ayam': 23000,
    'Es Milktea': 20000,
    'Es Teh': 7000,
    'Es Teller': 10000,
    'Es Kopi Expresso': 12000,
    'Air Mineral': 3000
}

# Opsi pilihan ongkir
opsi_ongkir = {
    'Losarang': 7000,
    'Gabus': 10000,
    'Eretan': 5000
}

class AplikasiPemesanan(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Selamat Datang di Aplikasi Pemesanan Makanan")
        self.configure(bg='lightgreen')

        # Inisialisasi variabel nama_pemesan
        self.nama_pemesan = tk.StringVar()

        # Label dan text box untuk input nama pemesan
        tk.Label(self, text="Silakan isi nama Anda di bawah ini untuk memesan makanan:").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="Nama Pemesan:").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.nama_pemesan).grid(row=1, column=1)

        # Combobox untuk memilih makanan
        tk.Label(self, text="Pilih Makanan:").grid(row=2, column=0)
        self.combobox_makanan = ttk.Combobox(self, values=list(menu.keys()))
        self.combobox_makanan.grid(row=2, column=1)

        # Combobox untuk memilih minuman
        tk.Label(self, text="Pilih Minuman:").grid(row=3, column=0)
        self.combobox_minuman = ttk.Combobox(self, values=list(menu.keys()))
        self.combobox_minuman.grid(row=3, column=1)

        # Combobox untuk memilih opsi ongkir
        tk.Label(self, text="Pilih Ongkir:").grid(row=4, column=0)
        self.combobox_ongkir = ttk.Combobox(self, values=list(opsi_ongkir.keys()))
        self.combobox_ongkir.grid(row=4, column=1)

        # Button untuk menambahkan pesanan
        tk.Button(self, text="Pesan Sekarang", command=self.tambah_pesanan).grid(row=5, columnspan=2, pady=10)

        # Tabel untuk menampilkan pesanan
        self.tree = ttk.Treeview(self, columns=("Nama Pemesan", "Makanan", "Harga Makanan", "Minuman", "Harga Minuman", "Ongkir", "Total Harga"), show="headings")
        self.tree.grid(row=6, column=0, columnspan=2, padx=10)

        self.tree.heading("Nama Pemesan", text="Nama Pemesan")
        self.tree.heading("Makanan", text="Makanan")
        self.tree.heading("Harga Makanan", text="Harga Makanan")
        self.tree.heading("Minuman", text="Minuman")
        self.tree.heading("Harga Minuman", text="Harga Minuman")
        self.tree.heading("Ongkir", text="Ongkir")
        self.tree.heading("Total Harga", text="Total Harga")

        # Data order pelanggan
        self.order_pelanggan = {}

        # Menyesuaikan lebar kolom tabel
        for col in ("Nama Pemesan", "Makanan", "Harga Makanan", "Minuman", "Harga Minuman", "Ongkir", "Total Harga"):
            self.tree.column(col, width=90)

        # Menyesuaikan opsi makanan dan minuman untuk Combobox
        self.combobox_makanan['values'] = [makanan for makanan in menu.keys() if makanan not in ['Es Milktea', 'Es Teh', 'Air Mineral']]
        self.combobox_minuman['values'] = [minuman for minuman in menu.keys() if minuman in ['Es Milktea', 'Es Teh', 'Air Mineral']]
        self.combobox_ongkir['values'] = list(opsi_ongkir.keys())

    def tambah_pesanan(self):
        nama_pemesan = self.nama_pemesan.get()
        makanan = self.combobox_makanan.get()
        minuman = self.combobox_minuman.get()
        ongkir = self.combobox_ongkir.get()

        if not nama_pemesan:
            messagebox.showerror("Kesalahan", "Mohon lengkapi data pemesan.") 
            return

        if makanan in menu and minuman in menu and ongkir in opsi_ongkir:
            qty_makanan = 1  # Misalnya, default jumlah pesanan makanan adalah 1
            qty_minuman = 1  # Misalnya, default jumlah pesanan minuman adalah 1

            # Menghitung total harga pesanan
            total_harga = menu[makanan] + menu[minuman] + opsi_ongkir[ongkir]

            # Cek apakah pesanan dari nama_pemesan sudah ada di tabel
            item_id = None
            for child in self.tree.get_children():
                if nama_pemesan == self.tree.item(child, 'values')[0]:
                    item_id = child
                    break

            # Jika pesanan belum ada, tambahkan baris baru
            if item_id is None:
                self.tree.insert("", "end", values=(nama_pemesan, makanan, menu[makanan], minuman, menu[minuman], opsi_ongkir[ongkir], total_harga))
            else:
                # Jika pesanan sudah ada, update jumlah pesanan
               existing_qty = int(self.tree.item(item_id, 'values')[4])  
            existing_total_harga = int(self.tree.item(item_id, 'values')[6])  
            self.tree.item(item_id, values=(nama_pemesan, makanan, menu[makanan], minuman, menu[minuman], opsi_ongkir[ongkir], existing_qty + 1, existing_total_harga + total_harga))

if __name__== "__main__":
    app = AplikasiPemesanan()
    app.mainloop()
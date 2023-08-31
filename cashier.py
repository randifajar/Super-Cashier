# Super Cashier - Randi Fajar Wicaksono
"""
Class dan Function untuk menjalankan fitur cashier yang ada
"""

from tabulate import tabulate
from input import validate_name, validate_harga, validate_jumlah


class Transaction:
    # Membuat Class Transzction
    def __init__(self):
        # Mendefinisikan dictionary items untuk menampung item belanja
        self.items = {}

    def check_order(self):
        # Cek apakah ada item di dictionary items
        if len(self.items) > 0:
            self.print_items()
            print(f"\n========== ========== ========== ========== ==========\n")
        else:
            print(f"Belum ada item yang dimasukkan")
            print(f"\n========== ========== ========== ========== ==========\n")

    def print_items(self):
        # Menampilkan semua item di dictionary items
        temp = []
        list_items = []
        list_nama = []
        list_jumlah = []
        list_harga = []
        list_total = []

        for key, value in self.items.items():
            temp = [key, value]
            list_items.append(temp)

        for i in range(len(list_items)):
            list_nama.append(list_items[i][0])
            list_jumlah.append(list_items[i][1][0])
            list_harga.append(list_items[i][1][1])
            list_total.append(list_items[i][1][2])

        data = {}
        data["Nama"] = list_nama
        data["Jumlah"] = list_jumlah
        data["Harga"] = list_harga
        data["Total"] = list_total

        print(tabulate(data, headers=['Nama', 'Jumlah', 'Harga', 'Total']))

    def add_item(self):
        # Fungsi untuk menambah item di dictionary items
        nama_item = validate_name(
            self.items, cek_list=False, text="Masukkan Nama Item")
        jumlah_item = validate_jumlah(text="Masukkan Jumlah Item")
        harga_per_item = validate_harga(text="Masukkan Harga Item")
        self.items[nama_item] = [jumlah_item,
                                 harga_per_item, jumlah_item * harga_per_item]

    def update_item_name(self):
        # Fungsi untuk meng-update nama item di dictionary items
        nama_item = validate_name(
            self.items, cek_list=True, text="Masukkan Nama Item")
        update_nama_item = validate_name(
            self.add_item, cek_list=False, text="Masukkan Nama Item Baru")
        self.items[update_nama_item] = self.items.pop(nama_item)

    def update_item_qty(self):
        # Fungsi untuk meng-update jumlah item di dictionary items
        nama_item = validate_name(
            self.items, cek_list=True, text="Masukkan Nama Item")
        update_jumlah_item = validate_jumlah(text="Masukkan Jumlah Item Baru")
        self.items[nama_item][0] = update_jumlah_item
        self.items[nama_item][2] = update_jumlah_item * \
            self.items[nama_item][1]

    def update_item_price(self):
        # Fungsi untuk meng-update harga item di dictionary items
        nama_item = validate_name(
            self.items, cek_list=True, text="Masukkan Nama Item")
        update_harga_item = validate_harga(text="Masukkan Harga Item Baru")
        self.items[nama_item][1] = update_harga_item
        self.items[nama_item][2] = update_harga_item * self.items[nama_item][0]

    def delete_item(self):
        # Fungsi untuk menghapus satu item di dictionary items
        nama_item = validate_name(
            self.items, cek_list=True, text="Masukkan Nama Item")
        self.items.pop(nama_item)

    def reset_transaction(self):
        # Fungsi untuk mereset atau menghapus semua item di dictionary items
        self.items.clear()

    def total_price(self):
        # Fungsi untuk menghitung dan menampilkan total belanja, diskon, dan total bayar
        discount = 0
        total = 0

        # Menghitung total belanja
        for keys, _ in self.items.items():
            total += int(self.items[keys][2])

        print(f"Total Belanja: Rp {total}")
        print(f"\n========== ========== ========== ========== ==========\n")

        # Menghitung diskon
        if total > 500000:
            discount = int(total * 0.1)
            print(
                f"Anda mendapatkan diskon sebesar 10%\nkarena belanja diatas Rp 500.000")
        elif total > 300000:
            discount = int(total * 0.08)
            print(
                f"Anda mendapatkan diskon sebesar 8%\nkarena belanja sebesar Rp 300.000")
        elif total > 200000:
            discount = int(total * 0.05)
            print(
                f"Anda mendapatkan diskon sebesar 5%\nkarena belanja sebesar Rp 200.000")
        else:
            print(f"Belanja di atas Rp 200.000 untuk mendapatkan diskon")

        # Menampilkan dan menghitung total bayar
        print(f"\n========== ========== ========== ========== ==========\n")
        print(f"Diskon yang diperoleh: Rp {discount}")
        print(f"\n========== ========== ========== ========== ==========\n")
        print(f"Total Bayar: Rp {total - discount} <--------------------")
        print(f"\n========== ========== ========== ========== ==========\n")

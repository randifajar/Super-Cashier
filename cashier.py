from tabulate import tabulate


class Transaction:
    def __init__(self):
        self.items = {}

    def check_order(self):
        if len(self.items) > 0:
            self.print_items()
            print(f"\n========== ========== ========== ========== ==========\n")
        else:
            print(f"Belum ada item yang dimasukkan")
            print(f"\n========== ========== ========== ========== ==========\n")

    def print_items(self):
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
        nama_item = input("Nama item: ")
        jumlah_item = int(input("Jumlah item: "))
        harga_per_item = int(input("Harga per item: "))
        self.items[nama_item] = [jumlah_item,
                                 harga_per_item, jumlah_item * harga_per_item]

    def update_item_name(self):
        nama_item = input("Nama item yang ingin diganti: ")
        update_nama_item = input("Nama item baru: ")
        self.items[update_nama_item] = self.items.pop(nama_item)

    def update_item_qty(self):
        nama_item = input("Nama item yang ingin diganti: ")
        update_jumlah_item = int(input("Jumlah item baru: "))
        self.items[nama_item][0] = update_jumlah_item
        self.items[nama_item][2] = update_jumlah_item * \
            self.items[nama_item][1]

    def update_item_price(self):
        nama_item = input("Nama item yang ingin diganti: ")
        update_harga_item = int(input("Harga per item baru: "))
        self.items[nama_item][1] = update_harga_item
        self.items[nama_item][2] = update_harga_item * self.items[nama_item][0]

    def delete_item(self):
        nama_item = input("Nama item yang ingin dihapus: ")
        self.items.pop(nama_item)

    def reset_transaction(self):
        self.items.clear()

    def total_price(self):
        hitung_total = True
        discount = 0
        total = 0

        for keys, _ in self.items.items():
            total += int(self.items[keys][2])

        print(f"Total Belanja: {total}")
        print(f"\n========== ========== ========== ========== ==========\n")

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

        print(f"\n========== ========== ========== ========== ==========\n")
        print(f"Diskon yang diperoleh: {discount}")
        print(f"\n========== ========== ========== ========== ==========\n")
        print(f"Total Bayar: {total - discount}")
        print(f"\n========== ========== ========== ========== ==========\n")
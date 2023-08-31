# Super Cashier - Randi Fajar Wicaksono
"""
Python Project Super Cashier.
Tampilan awal untuk menampilkan menu utama dan sub-menu.

Fitur Menu Utama:
    1. Buat Transaksi
    2. Keluar Program

Fitur Sub-Menu:
    1. Tambah Item
    2. Update Nama Item
    3. Update Jumlah Item
    4. Update Harga Item
    5. Hapus Satu Item
    6. Hapus Semua Item
    7. Hitung Total Bayar
    8. Kembali ke Menu Utama
"""

import os
import cashier


def menu():
    error = False
    # Menampilkan menu utama pada console
    while True:
        # Membersihkan console dan menampilkan menu
        os.system('cls')
        print(f"========== ========== ========== ========== ==========\n")
        print(f"                    Super Cashier")
        print(f"\n========== ========== ========== ========== ==========\n")
        if error == True:
            print("Pilihan tidak ada pada menu")
            print(f"\n========== ========== ========== ========== ==========\n")
            error = False
        print(f"1. Buat Transaksi")
        print(f"0. Keluar")
        print(f"\n========== ========== ========== ========== ==========\n")

        try:
            # Input pilihan user
            pilihan = int(input("Masukkan Pilihan: "))

            if type(pilihan) != int:
                raise ValueError
            else:
                # Case sesuai pilihan user
                match pilihan:
                    case 1:
                        trnsct_123 = cashier.Transaction()
                        submenu(trnsct_123)
                    case 0:
                        print("See You")
                        print(
                            f"\n========== ========== ========== ========== ==========\n")
                        exit()
                    case _:
                        raise ValueError
        except ValueError:
            error = True


def submenu(trnsct_123):
    # Menampilkan sub-menu pada console
    error = False
    case_7 = False
    while True:
        # Membersihkan console dan menampilkan menu
        os.system('cls')
        print(f"========== ========== ========== ========== ==========\n")
        print(f"                    Super Cashier")
        print(f"\n========== ========== ========== ========== ==========\n")
        if error == True:
            print("Pilihan tidak ada pada menu")
            print(f"\n========== ========== ========== ========== ==========\n")
            error = False
        trnsct_123.check_order()
        if case_7 == True:
            trnsct_123.total_price()
            case_7 = False
        print(f"1. Tambah Item")
        print(f"2. Update Nama Item")
        print(f"3. Update Jumlah Item")
        print(f"4. Update Harga Item")
        print(f"5. Hapus Satu Item")
        print(f"6. Hapus Semua Item")
        print(f"7. Hitung Total Bayar")
        print(f"0. Kembali")
        print(f"\n========== ========== ========== ========== ==========\n")

        try:
            # Input pilihan user
            pilihan = int(input("Masukkan Pilihan: "))

            if type(pilihan) != int:
                raise ValueError
            else:
                # Case sesuai pilihan user
                match pilihan:
                    case 1:
                        trnsct_123.add_item()
                    case 2:
                        trnsct_123.update_item_name()
                    case 3:
                        trnsct_123.update_item_qty()
                    case 4:
                        trnsct_123.update_item_price()
                    case 5:
                        trnsct_123.delete_item()
                    case 6:
                        trnsct_123.reset_transaction()
                    case 7:
                        case_7 = True
                    case 0:
                        menu()
                    case _:
                        raise ValueError
        except ValueError:
            error = True


if __name__ == "__main__":
    os.system('cls')
    menu()

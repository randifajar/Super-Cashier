# Super Cashier - Randi Fajar Wicaksono
"""
Class dan Function untuk input dan validasi input dari user
"""


def check_name(items, nama_item):
    # Mencari nama atau keys dari user pada dictionary items
    cek = False
    for keys in items.keys():
        if keys == nama_item:
            cek = True
            break
    return cek


def validate_name(items, cek_list, text):
    # Fungsi untuk input dan validasi nama
    while True:
        try:
            nama_item = input(f"{text}: ")
            if not nama_item:
                raise ValueError
            elif cek_list == True:
                if check_name(items, nama_item) == False:
                    raise KeyError
        except ValueError:
            print(f"Nama tidak boleh kosong\n")
        except KeyError:
            print(f"Nama tidak ditemukan\n")
        else:
            break
    return nama_item


def validate_jumlah(text):
    # Fungsi untuk input dan validasi jumlah
    while True:
        try:
            jumlah_item = int(input(f"{text}: "))
            if not jumlah_item:
                raise ValueError
            elif type(jumlah_item) != int:
                raise ValueError
            elif jumlah_item <= 0:
                raise TypeError
        except ValueError:
            print(f"Jumlah hanya berisi angka dan tidak boleh kosong\n")
        except TypeError:
            print(f"Jumlah tidak boleh kurang dari 1\n")
        else:
            break
    return jumlah_item


def validate_harga(text):
    # Fungsi untuk input dan validasi harga
    while True:
        try:
            harga_per_item = int(input(f"{text}: Rp "))
            if not harga_per_item:
                raise ValueError
            elif type(harga_per_item) != int:
                raise ValueError
            elif harga_per_item <= 0:
                raise TypeError
        except ValueError:
            print(f"Harga hanya berisi angka dan tidak boleh kosong\n")
        except TypeError:
            print(f"Harga tidak boleh kurang dari 1\n")
        else:
            break
    return harga_per_item


def validate_delete(nama_item):
    while True:
        try:
            val = input(
                f"Apakah anda yakin ingin menghapus {nama_item}? (y/n): ")
            if not val:
                raise ValueError
            elif val != "y":
                if val != "n":
                    raise ValueError
        except ValueError:
            print(f"Input hanya 'y' atau 'n' dan tidak boleh kosong\n")
        else:
            break
    return val

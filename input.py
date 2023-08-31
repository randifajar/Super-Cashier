def check_name(items, nama_item):
    cek = False
    for keys in items.keys():
        if keys == nama_item:
            cek = True
            break
    return cek


def validate_name(items, cek_list, text):
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
    while True:
        try:
            harga_per_item = int(input(f"{text}: "))
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

# Project Python Super Cashier

## Latar Belakang
Andi adalah seorang pemilik supermarket besar yang memiliki rencana untuk melakukan perbaikan proses bisnis. Andi membutuhkan sebuah sistem kasir yang self-service. Sehingga customer bisa membeli barang dari supermarket tersebut dari mana saja tanpa harus datang ke supermarket.

## Tujuan
Merancang dan membangun sebuah sistem kasir self-service untuk supermarket Andi untuk mempermudah transaksi pembelian melalui sisem.

## Kebutuhan
Adapun fitur atau kebutuhan yang diperlukan untuk sistem kasir ini adalah:
  1. Membuat ID transaksi.
  2. Memasukkan nama item, jumlah item, dan harga barang.
  3. Memperbarui nama item.
  4. Memperbarui jumlah item.
  5. Menghapus item.
  6. Membatalkan (me-reset) semua item.
  7. Mengecek item.
  8. Menghitung total belanja.
  9. Menghitung diskon.

## Flowchart
![Flowchart](https://github.com/randifajar/Super-Cashier/assets/46032161/fff48e7d-8df7-476b-bfd7-6f3b7eaa1e63)

### Penjelasan Alur Program
  1. Customer masuk ke dalam sistem kasir dan akan ditampilkan menu utama pada sistem
  2. Customer memasukkan nama, jumlah, dan harga item dan menyimpannya.
  3. Customer dapat mengecek daftar item yang sudah dimasukkan di atas menu.
  4. Customer dapat mengubah nama, jumlah, dan harga item jika ingin mengubah data pesanan.
  5. Customer dapat menghapus satu atau lebih item.
  6. Customer dapat membatalkan semua pesanan dan kembali ke menu utama.
  7. Sistem akan menghitung total belanja.
  8. Sistem akan menghitung diskon berdasarkan total belanja yang telah dihitung.
  9. Jika total belanja lebih dari Rp 500.000, maka akan mendapatkan diskon sebesar 10%.
  10. Jika total belanja lebih dari Rp 300.000, maka akan mendapatkan diskon sebesar 8%.
  11. Jika total belanja lebih dari Rp 200.000, maka akan mendapatkan diskon sebesar 5%.
  12. Sistem akan menghitung total bayar yang didapat dari total belanja dikurang diskon.
  13. Sistem akan menampilkan total belanja, diskon, dan total bayar.

## Penjelasan Kode Program
  * `menu()` : Function yang berguna menampilkan menu utama dan switch case yang dipilih user.
  * `submenu()` : FUnction yang berguna menampilkan sub-menu dan menampilkan switch case yang dipilih user.
  * `Transaction()` : Class yang berguna menyimpan seluruh Function untuk menjalankan proses transaksi pada sistem kasir.
  * `check_order()` : Function yang berguna mengecek apakah ada items yang tersimpan.
  * `print_items()` : Function yang berguna menampilkan daftar items yang tersimpan.
  * `add_item()` : Function yang berguna menambahkan dan menyimpan item.
  * `update_item_name()` : Function yang berguna memperbarui nama item.
  * `update_item_qty()` : Function yang berguna memperbarui jumlah item.
  * `update_item_price()` : Function yang berguna memperbarui harga item.
  * `delete_item()` : Function yang berguna menghapus satu atau lebih item.
  * `reset_transaction()` : Function yang berguna menghapus semua atau me-reset item.
  * `total_price()` : Function yang berguna menghitung dan menampilkan total belanja, diskon, dan total bayar.
  * `check_name()` : Function yang berguna mengecek apakah ada data nama yang diimputkan user yang tersimpan.
  * `validate_name()` : Function yang berguna sebagai tempat input dan validasi data nama dari user.
  * `validate_jumlah()` : Function yang berguna sebagai tempat input dan validasi data jumlah dari user.
  * `validate_harga()` : Function yang berguna sebagai tempat input dan validasi data harga dari user.
  * `validate_delete()` : Function yang berguna sebagai tempat validasi apakah user yakin ingin menghapus item atau tidak.
  
## Test Case
Gambar di bawah merupakan tampilan menu utama sistem.

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/e69fb281-03d2-4b2f-92bd-146092a25949)

Gambar di bawah merupakan tempilan sub-menu sistem yang dapat diakses ketika user memilih '1' pada menu utama.

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/2d29dbf6-96e7-40e7-b0df-d33b1082b2de)

### Test Case 1
Customer ingin menambahkan dua item baru, di mana item yang ingin ditambahkan adalah:
  * Nama Item: Ayam Goreng, Jumlah: 2, Harga: 20000
  * Nama Item: Pasta Gigi, Jumlah: 3, Harga: 15000
  * Nama Item: Es Teh, Jumlah: 10, Harga: 3000
  * Nama Item: Tahu, Jumlah: 10, Harga: 1000

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/ed9da17a-e977-4dc5-b56e-b14277ac3a9c)

Daftar item setelah semua item ditambahkan:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/692cf13d-4b77-4637-83af-004d243e534e)

### Test Case 2
Customer ingin mengubah beberapat item, di mana item yang ingin diubah adalah:
  * Mengubah Nama Item: Tahu menjadi Gorengan
    
    ![image](https://github.com/randifajar/Super-Cashier/assets/46032161/ab1261a9-e538-4470-bf41-ca7509ee44a7)
    
  * Mengubah Jumlah: 2 pada Nama Item: Ayam Goreng menjadi 5

    ![image](https://github.com/randifajar/Super-Cashier/assets/46032161/cdb7be50-7f7f-4353-892b-1c4077fbfc97)
    
  * Mengubah Harga: 3000 pada Nama Item: Es Teh menjadi 4000

    ![image](https://github.com/randifajar/Super-Cashier/assets/46032161/5a61ec3b-a1f8-40db-8a98-21f88c4a97d7)

Daftar item setelah beberapa item diubah:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/fd60bb30-34a4-4221-aac9-374704359033)

### Test Case 3
Customer tidak jadi memesan Es Teh dan ingin menghapusnya:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/f3a22b89-b045-404f-a257-39ba83e82ecc)

Daftar item setelah item Es Teh dihapus:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/7f4ecd1d-3d2b-41d4-a105-a703c8240a52)

### Test Case 4
Customer membatalkan pesanannya dan ingin menghapus semua itemnya:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/a5a5202d-3c0e-447d-bedc-68ff628912e9)

Daftar item setelah semua item di-reset:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/a83742a1-38b8-45c6-9421-b4c22b1aa8e4)

### Test Case 5
Customer telah menambahkan item sesuai keinginannya, di mana daftar item yang ingin dia beli:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/1c5af8c9-e999-42a0-97b0-8395f3a8b81e)

Customer ingin menghitung total belanja dan total bayar:

![image](https://github.com/randifajar/Super-Cashier/assets/46032161/a6129e67-af77-4aef-88ca-3813a1e21d09)

## Kesimpulan
Sistem kasir self-service ini dibuat untuk membantu dan mengelola supermarket milik Andi. Dengan sistem kasir ini, customer dapat memilih dan mengelola pesanannya sendiri tanpa harus datang ke supermarket. Fitur yang dapat digunakan adalah menambahkan item, mengubah nama item, mengubah jumlah item, mengubah harga item, menghapus item, mereset pesanan, dan menghitung total belanja. Di dalam sistem ini juga terdapat validasi input dari customer, sehingga memperkecil kemungkinan kesalahan input dari user. Pada saat menghapus atau mereset item, customer akan mendapatkan pertanyaan validasi sebelum menghapus item, yang ditujukan agar ketika customer salah menginputkan item, customer dapat membatalkan proses hapus atau reset. Sehingga membuat customer dapat berbelanja di supermarket milik Andi dengan mudah, cepat, efektif, dan efisien.

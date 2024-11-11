# Program untuk menampilkan substring berdasarkan indeks yang dimasukkan

# Meminta input dari pengguna
kata = input("Masukkan sebuah kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Menampilkan substing berdasarkan indeks
# Perhatikan bahwa indeks akhir bersifat eksklusif, artinya karakter di indeks_akhir tidak termasuk
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil
print(f"Substring dari indeks {indeks_awal} hingga {indeks_akhir} adalah: '{substring}'")


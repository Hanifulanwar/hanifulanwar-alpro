# Program untuk menghitung jumlah huruf vokal dalam kalimat

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Menentukan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal
jumlah_vokal = 0
for char in kalimat:
    if char in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat tersebut adalah: {jumlah_vokal}")


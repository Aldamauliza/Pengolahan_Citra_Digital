# Fungsi untuk menghitung floor dari akar kuadrat n
def FloorAkar(n):
    i = 1  # Inisialisasi variabel i
    while i * i < n:
        i += 1  # Mencari nilai yang mendekati akar n
    if n % i == 0:
        print(i)  # Jika i secara bulat adalah akar n
    else:
        print(i - 1)  # Jika i di-floor

# Input bilangan integer positif n
n = int(input("Masukkan bilangan integer positif n: "))

# Memanggil fungsi FloorAkar
FloorAkar(n)

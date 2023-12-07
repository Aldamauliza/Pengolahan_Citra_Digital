# Fungsi untuk mencari jarak terdekat antara dua elemen dalam array A
def mencari_jarak_terdekat(A):
    n = len(A)  # Menghitung panjang array A
    dmin = float('inf')  # Menginisialisasi jarak terdekat dengan nilai tak terhingga

    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return 0  # Jika ada elemen yang sama, jarak terdekat adalah 0
            elif abs(A[i] - A[j]) < dmin:
                dmin = abs(A[i] - A[j])  # Memperbarui jarak terdekat jika lebih kecil

    return dmin

# Input array A
n = int(input("Masukkan panjang array A: "))
A = []

for i in range(n):
    elemen = int(input(f"Masukkan elemen ke-{i}: "))
    A.append(elemen)

# Memanggil fungsi mencari_jarak_terdekat
hasil = mencari_jarak_terdekat(A)

# Menampilkan hasil jarak terdekat
print(f"Jarak terdekat antara dua elemen dalam array A adalah: {hasil}")



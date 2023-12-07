# Mendefinisikan array R, G, dan B
R = [100, 20, 30, 40]
G = [20, 30, 80, 200]
B = [50, 60, 70, 200]

# Membuat array kosong untuk Grayscale
Grayscale = []

# Melakukan konversi ke Grayscale untuk setiap pixel
for i in range(len(R)):
    grayscale_value = int(0.299 * R[i] + 0.587 * G[i] + 0.114 * B[i])
    Grayscale.append(grayscale_value)

# Hasil Grayscale
print("Citra Grayscale:", Grayscale)
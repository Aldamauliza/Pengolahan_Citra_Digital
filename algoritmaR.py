# Nilai resistansi yang telah diberikan
R1 = (2/5) * 16
R2 = 3/7
R3 = 3

# Menghitung invers dari masing-masing resistor
inv_R1 = 1 / R1
inv_R2 = 1 / R2
inv_R3 = 1/ (1 / R3)

# Menjumlahkan invers dari ketiga resistor
inv_total = inv_R1 + inv_R2 + inv_R3

# Menghitung invers dari hasil penjumlahan
R_total = 1 / inv_total

# Menampilkan hasil resistansi total (R)
print("Nilai resistansi total (R) adalah:", R_total)

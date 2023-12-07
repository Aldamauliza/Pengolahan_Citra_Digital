# Membaca input skor dari pengguna
skor = int(input("Masukkan skor mahasiswa: "))

# Mengevaluasi skor dan menentukan nilai huruf
if skor > 90:
    nilai_huruf = "A"
elif skor >= 86:
    nilai_huruf = "A-"
elif skor >= 81:
    nilai_huruf = "B+"
elif skor >= 76:
    nilai_huruf = "B"
elif skor >= 71:
    nilai_huruf = "B-"
elif skor >= 66:
    nilai_huruf = "C+"
elif skor >= 61:
    nilai_huruf = "C"
elif skor >= 56:
    nilai_huruf = "C-"
elif skor >= 46:
    nilai_huruf = "D"
else:
    nilai_huruf = "E"

# Menampilkan nilai huruf
print("Nilai huruf mahasiswa:", nilai_huruf)

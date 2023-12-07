# Membaca input dari pengguna
gaji_pokok = float(input("Masukkan gaji pokok karyawan: "))
jumlah_anak = int(input("Masukkan jumlah anak: "))
masa_kerja = int(input("Masukkan masa kerja (tahun): "))
masuk_kerja = int(input("Masukkan jumlah hari masuk kerja: "))

# Menghitung tunjangan istri/suami
tunjangan_istri_suami = 0.10 * gaji_pokok

# Menghitung tunjangan anak
tunjangan_anak = 0.05 * gaji_pokok
total_tunjangan_anak = tunjangan_anak * jumlah_anak

# Menghitung THR
thr = 5000 * masa_kerja

# Menghitung total pendapatan sebelum potongan pajak
total_pendapatan_sebelum_pajak = gaji_pokok + tunjangan_istri_suami + total_tunjangan_anak + thr + (3000 * masuk_kerja)

# Menghitung potongan pajak
pajak = 0.15 * (gaji_pokok + tunjangan_istri_suami + total_tunjangan_anak)

# Menghitung bantuan transport
bantuan_transport = 3000 * masuk_kerja

# Menghitung total pendapatan setelah potongan pajak
total_pendapatan_setelah_pajak = total_pendapatan_sebelum_pajak - pajak

# Mengurangkan biaya polis asuransi
total_pendapatan_setelah_asuransi = total_pendapatan_setelah_pajak - 20000

# Menampilkan total pendapatan bulanan setelah semua potongan dan tunjangan
print("Total pendapatan bulanan karyawan:", total_pendapatan_setelah_asuransi)

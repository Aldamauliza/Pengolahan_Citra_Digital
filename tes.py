print ("Nilai Final Pengolahan Citra")
T = int(input("Masukkan Nilai Tugas: "))
Q = int(input("Masukkan Nilai Quis: "))
M = int(input("Masukkan Nilai MidTest: "))
U = int(input("Masukkan Nilai UAS: "))

Nilai_Final = ((T * 0.2) + (Q * 0.2) + (M * 0.3) + (U * 0.3))

if Nilai_Final >= 80:
    print("A")
elif Nilai_Final >= 70 and Nilai_Final < 80:
    print("B")
elif Nilai_Final >= 55 and Nilai_Final < 70:
    print("C")
elif Nilai_Final >= 40 and Nilai_Final < 55:
    print("D")
else:
    print("E")

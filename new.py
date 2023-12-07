import itertools

# Jarak antar titik yang sudah diketahui
jarak = {
    ('A', 'B'): 5,
    ('A', 'C'): 8,
    ('A', 'D'): 13,
    ('A', 'E'): 2,
    ('A', 'F'): 10,
    ('B', 'A'): 5,
    ('B', 'C'): 9,
    ('B', 'D'): 5,
    ('B', 'E'): 20,
    ('B', 'F'): 11,
    ('C', 'A'): 8,
    ('C', 'B'): 9,
    ('C', 'D'): 12,
    ('C', 'E'): 4,
    ('C', 'F'): 25,
    ('D', 'A'): 13,
    ('D', 'B'): 5,
    ('D', 'C'): 12,
    ('D', 'E'): 17,
    ('D', 'F'): 13,
    ('E', 'A'): 2,
    ('E', 'B'): 20,
    ('E', 'C'): 4,
    ('E', 'D'): 17,
    ('E', 'F'): 9,
    ('F', 'A'): 10,
    ('F', 'B'): 11,
    ('F', 'C'): 25,
    ('F', 'D'): 13,
    ('F', 'E'): 9
}

titik_awal = 'A'
titik_akhir = 'A'
titik_terpendek = []
jarak_terpendek = float('inf')

# Generate semua kemungkinan jalur
titik = ['B', 'C', 'D', 'E', 'F']
kemungkinan_jalur = itertools.permutations(titik)

for jalur in kemungkinan_jalur:
    jalur = (titik_awal,) + jalur + (titik_awal,)
    jarak_jalur = 0

    for i in range(len(jalur) - 1):
        pasangan = (jalur[i], jalur[i + 1])
        if pasangan in jarak:
            jarak_jalur += jarak[pasangan]
        else:
            break

    if jarak_jalur < jarak_terpendek:
        jarak_terpendek = jarak_jalur
        titik_terpendek = jalur

if jarak_terpendek < float('inf'):
    print(f"Jalur terpendek dari {titik_awal} ke {titik_akhir} adalah: {' -> '.join(titik_terpendek)}")
    print(f"Jarak terpendek adalah: {jarak_terpendek}")
else:
    print(f"Tidak ada jalur yang tersedia untuk kembali ke {titik_awal}")
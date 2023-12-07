import itertools

nama_kota = []

def jarak(graph, path):
    total_bobot = 0
    n = len(graph)

    for i in range(n):
        total_bobot += graph[path[i]][path[(i + 1) % n]]

    return total_bobot

def exhaustive_search(graph):
    n = len(graph)
    min_bobot = float('inf')
    min_jarak = None

    all_permutations = itertools.permutations(range(n))

    for path in all_permutations:
        bobot = jarak(graph, path)
        if bobot < min_bobot:
            min_bobot = bobot
            min_jarak = path

    return min_jarak, min_bobot

def input_graph():
    global nama_kota
    n = int(input("Masukkan jumlah kota: "))
    graph = []

    # Membuat daftar karakter 'abcd...' untuk penamaan kota
    nama_kota = [chr(ord('a') + i) for i in range(n)]

    print("Masukkan jarak antar kota:")
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Jarak dari kota ke dirinya sendiri adalah 0
            else:
                jarak_kota = int(input(f"Jarak dari kota {nama_kota[i]}-{nama_kota[j]}: "))
                row.append(jarak_kota)

        graph.append(row)

    return graph

# Input matriks jarak dari pengguna
graph = input_graph()

if graph is not None:
    min_jarak, min_bobot = exhaustive_search(graph)
    print("Jarak terdekat:", [nama_kota[idx] for idx in min_jarak])
    print("Bobot:", min_bobot)

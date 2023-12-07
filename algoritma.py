
import itertools

def jarak(graph, path):
    total_bobot = 0
    n = len(graph)
    
    for i in range(n - 1):
        total_bobot += graph[path[i]][path[i + 1]]
    
    total_bobot += graph[path[-1]][path[0]]  
    return total_bobot

def exhaustive_search(graph):
    n = len(graph)
    min_bobot = float('inf')
    min_path = None
    
    all_permutations = itertools.permutations(range(n))
    
    for path in all_permutations:
        bobot = jarak(graph, path)
        if bobot < min_bobot:
            min_bobot = bobot
            min_path = path
    
    return min_path, min_bobot

def input_graph():
    n = int(input("Masukkan jumlah kota: "))
    graph = []

    print("Masukkan jarak antara kota-kota (diisi dengan angka):")
    for i in range(n):
        row = input().split()
        if len(row) != n:
            print("Jumlah angka yang dimasukkan harus sama dengan jumlah kota.")
            return None
        row = [int(x) for x in row]
        graph.append(row)

    return graph

# Input matriks jarak dari pengguna
graph = input_graph()

if graph is not None:
    min_path, min_bobot = exhaustive_search(graph)
    print("Optimal TSP Path:", min_path)
    print("Optimal TSP bobot:", min_bobot)

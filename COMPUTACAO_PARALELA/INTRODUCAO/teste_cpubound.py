import time, statistics

def tarefa_cpu(carga):
    """Soma aritmética inteira - resultado verificável. """
    return sum(range(carga))

cargas = [500_000] * 20

tempos = []
for _ in range(5):
    t0 = time.perf_counter()
    resultado_seq = [tarefa_cpu(c) for c in cargas]
    tempos.append(time.perf_counter() - t0)

mediana_seq = statistics.median(tempos)
print(f"Mediana sequencial: {mediana_seq:.4f} segundos")
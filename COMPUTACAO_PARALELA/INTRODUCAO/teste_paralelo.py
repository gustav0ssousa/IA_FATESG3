from concurrent.futures import ProcessPoolExecutor
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

tempos_par = []
for _ in range(5):
    t0 = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        resultado_par = list(executor.map(tarefa_cpu, cargas))
    tempos_par.append(time.perf_counter() - t0)

mediana_par = statistics.median(tempos_par)

#Validação Obrigatória
assert resultado_seq == resultado_par, "Resultados divergem!"
print(f"Mediana paralela: {mediana_par:.4f} segundos")
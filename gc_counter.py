from collections import Counter

# Abrir arquivo FASTA e ler todas as linhas que NÃO são cabeçalho (linhas que não começam com ">")
with open("GCF_000005845.2_ASM584v2_genomic.fna") as f:
    seq = ""
    for line in f:
        if not line.startswith(">"):
            seq += line.strip().upper()

# Contar cada letra/nucleotídeo
counts = Counter(seq)
total = sum(counts.values())

# Calcular GC
gc = counts.get("G", 0) + counts.get("C", 0)
gc_percent = (gc / total) * 100 if total else 0

print(f"Tamanho total: {total} bases")
print(f"A: {counts.get('A',0)} ({(counts.get('A',0)/total)*100:.2f}%)")
print(f"T: {counts.get('T',0)} ({(counts.get('T',0)/total)*100:.2f}%)")
print(f"G: {counts.get('G',0)} ({(counts.get('G',0)/total)*100:.2f}%)")
print(f"C: {counts.get('C',0)} ({(counts.get('C',0)/total)*100:.2f}%)")
print(f"GC%: {gc_percent:.2f}%")

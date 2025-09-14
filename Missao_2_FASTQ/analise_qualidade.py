#!/usr/bin/env python3
"""
analise_qualidade.py
Simples análise de qualidade de FASTQ (gzip).
Uso:
  python3 analise_qualidade.py arquivo.fastq.gz [--phred 33] [--max-reads N] [--detailed] [--plot]

Explicação:
- --phred: offset (33 ou 64). Default 33 (mais comum).
- --max-reads: processa no máximo N leituras (útil para testar sem processar o arquivo inteiro).
- --detailed: calcula medianas (usa mais memória).
- --plot: tenta gerar PNGs (requer matplotlib instalado).
"""
import gzip
import argparse
from collections import Counter
import statistics
import csv
import os
import sys

def processar_fastq(path, phred=33, max_reads=None, detailed=False):
    total_reads = 0
    total_bases = 0

    per_base_sums = []    # soma das qualidades por posição (se detailed=False)
    per_base_counts = []  # contagem de valores por posição (para média)
    per_base_vals = []    # lista de listas com valores por posição (se detailed=True)
    per_pos_bases = []    # lista de Counter() para composição por posição

    per_read_mean_quals = []  # média de qualidade por leitura (amostra)

    with gzip.open(path, "rt") as f:
        while True:
            header = f.readline()
            if not header:
                break
            seq = f.readline().strip()
            plus = f.readline()
            qual = f.readline().strip()

            if not qual:
                break

            total_reads += 1
            total_bases += len(seq)

            # garantir estrutura para o comprimento atual
            L = len(qual)
            while len(per_base_sums) < L:
                per_base_sums.append(0)
                per_base_counts.append(0)
                per_pos_bases.append(Counter())
                if detailed:
                    per_base_vals.append([])

            # converter qual chars para scores
            scores = [ord(c) - phred for c in qual]

            # atualizar per-position
            for i, s in enumerate(scores):
                per_base_sums[i] += s
                per_base_counts[i] += 1
                if detailed:
                    per_base_vals[i].append(s)

            # composição de bases por posição
            for i, b in enumerate(seq.upper()):
                per_pos_bases[i].update(b)

            # média da leitura
            per_read_mean_quals.append(statistics.mean(scores))

            # controle de número de reads processadas (opcional)
            if max_reads and total_reads >= max_reads:
                break

    # calcular estatísticas por posição
    positions = list(range(1, len(per_base_sums) + 1))
    per_base_mean = [ (per_base_sums[i] / per_base_counts[i]) if per_base_counts[i] else 0 for i in range(len(per_base_sums)) ]

    per_base_median = []
    per_base_stdev = []
    if detailed:
        for vals in per_base_vals:
            if len(vals) > 0:
                per_base_median.append(statistics.median(vals))
                per_base_stdev.append(statistics.pstdev(vals))
            else:
                per_base_median.append(0)
                per_base_stdev.append(0)

    # composição em percentuais por posição (A/T/G/C/N/others)
    comp_pct = []
    for ctr in per_pos_bases:
        total = sum(ctr.values())
        if total == 0:
            comp_pct.append({})
            continue
        comp_pct.append({base: (count/total)*100 for base, count in ctr.items()})

    summary = {
        "total_reads": total_reads,
        "total_bases": total_bases,
        "mean_read_length": (total_bases/total_reads if total_reads else 0),
        "per_base_mean": per_base_mean,
        "per_base_median": per_base_median if detailed else None,
        "per_base_stdev": per_base_stdev if detailed else None,
        "comp_pct": comp_pct,
        "per_read_mean_quals_sample": per_read_mean_quals[:1000]  # primeiros 1000 para olhar distribuição
    }
    return summary

def salvar_csvs(summary, prefix):
    # per-base quality means
    with open(prefix + "_per_base_quality.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        header = ["position", "mean_quality"]
        if summary["per_base_median"] is not None:
            header += ["median_quality", "stdev_quality"]
        writer.writerow(header)
        for i, mean in enumerate(summary["per_base_mean"], start=1):
            row = [i, mean]
            if summary["per_base_median"] is not None:
                row += [summary["per_base_median"][i-1], summary["per_base_stdev"][i-1]]
            writer.writerow(row)

    # per-base composition
    with open(prefix + "_per_base_composition.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # collect all possible bases present
        bases = set()
        for d in summary["comp_pct"]:
            bases.update(d.keys())
        bases = sorted(list(bases))
        writer.writerow(["position"] + bases)
        for i, d in enumerate(summary["comp_pct"], start=1):
            row = [i] + [ round(d.get(b, 0), 3) for b in bases ]
            writer.writerow(row)

    # per-read mean quals (sample)
    with open(prefix + "_per_read_mean_quals_sample.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["read_index", "mean_quality"])
        for idx, val in enumerate(summary["per_read_mean_quals_sample"], start=1):
            writer.writerow([idx, val])

def gerar_plots(prefix):
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        print("matplotlib não disponível. Instale com: pip3 install matplotlib")
        return

    # per-base mean quality plot
    import csv
    xs = []
    ys = []
    with open(prefix + "_per_base_quality.csv") as f:
        r = csv.reader(f)
        hdr = next(r)
        for row in r:
            xs.append(int(row[0]))
            ys.append(float(row[1]))
    plt.figure(figsize=(10,4))
    plt.plot(xs, ys)
    plt.xlabel("Posição (base)")
    plt.ylabel("Qualidade média (Phred)")
    plt.title("Qualidade média por posição")
    plt.tight_layout()
    plt.savefig(prefix + "_per_base_quality.png")
    plt.close()
    print("Plot salvo:", prefix + "_per_base_quality.png")

def main():
    parser = argparse.ArgumentParser(description="Análise simples de qualidade FASTQ")
    parser.add_argument("fastq", help="arquivo.fastq.gz")
    parser.add_argument("--phred", type=int, default=33, choices=[33,64], help="offset Phred (33 padrão)")
    parser.add_argument("--max-reads", type=int, default=None, help="limitar o número de reads processadas")
    parser.add_argument("--detailed", action="store_true", help="calcular mediana/desvio (usa mais memória)")
    parser.add_argument("--plot", action="store_true", help="gerar plots PNG (requer matplotlib)")
    args = parser.parse_args()

    if not os.path.exists(args.fastq):
        print("Arquivo não encontrado:", args.fastq)
        sys.exit(1)

    print("Processando:", args.fastq)
    print("Phred offset:", args.phred)
    if args.max_reads:
        print("Máx reads:", args.max_reads)
    print("Detailed:", args.detailed)

    summary = processar_fastq(args.fastq, phred=args.phred, max_reads=args.max_reads, detailed=args.detailed)

    prefix = os.path.splitext(os.path.basename(args.fastq))[0]
    salvar_csvs(summary, prefix)

    print("\nResumo:")
    print("Total de reads:", summary["total_reads"])
    print("Total de bases:", summary["total_bases"])
    print("Tamanho médio das reads:", summary["mean_read_length"])

    if args.plot:
        gerar_plots(prefix)

if __name__ == "__main__":
    main()

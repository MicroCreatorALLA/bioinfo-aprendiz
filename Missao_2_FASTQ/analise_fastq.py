import gzip
import sys

def analisar_fastq(arquivo_fastq, num_headers=5):
    total_reads = 0
    total_bases = 0
    headers_exemplo = []

    # abre o arquivo compactado em modo leitura texto
    with gzip.open(arquivo_fastq, "rt") as f:
        for i, linha in enumerate(f):
            if i % 4 == 0:  # cabeçalho da leitura
                total_reads += 1
                if len(headers_exemplo) < num_headers:
                    headers_exemplo.append(linha.strip())
            elif i % 4 == 1:  # sequência da leitura
                total_bases += len(linha.strip())

    tamanho_medio = total_bases / total_reads if total_reads > 0 else 0

    print(f"📊 Estatísticas do arquivo: {arquivo_fastq}")
    print(f"Total de leituras: {total_reads:,}")
    print(f"Tamanho médio das reads: {tamanho_medio:.2f} bases")
    print("\n🔎 Exemplos de cabeçalhos:")
    for h in headers_exemplo:
        print("  ", h)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 analise_fastq.py <arquivo.fastq.gz>")
        sys.exit(1)

    arquivo = sys.argv[1]
    analisar_fastq(arquivo)

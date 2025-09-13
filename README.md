# Missão 1 – GC% Hunter

Este projeto é parte da minha jornada de aprendizado em Bioinformática.

## Objetivo
- Ler um arquivo FASTA de genoma de *Escherichia coli*.
- Calcular a contagem total de bases (A, T, G, C).
- Calcular a porcentagem de GC.

## Como usar
1. Baixe o arquivo FASTA:
wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/Escherichia_coli/reference/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz
gunzip GCF_000005845.2_ASM584v2_genomic.fna.gz

Copiar código
2. Execute o script Python:
python3 gc_counter.py

## Saída esperada
O script mostrará:
- Tamanho total do genoma
- Quantidade e porcentagem de A, T, G, C
- GC%

Exemplo:
Tamanho total: 4639675 bases
A: 1223456 (26.35%)
T: 1234567 (26.58%)
G: 1098765 (23.69%)
C: 1078887 (23.37%)
GC%: 47.06%

## Autor
Arthur – Aprendiz de Bioinformática
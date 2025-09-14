# 📂 Missão 1: GC Hunter

Esta pasta contém scripts e arquivos da **Missão 1**, cujo objetivo é explorar arquivos FASTA e calcular o conteúdo GC (guanina + citosina) de sequências genômicas.

---

## 🗂 Estrutura da pasta

gc_counter.py # Script Python para calcular conteúdo GC de arquivos FASTA
GCF_000005845.2_ASM584v2_genomic.fna # Exemplo de genoma em formato FASTA
README.md # Este arquivo
---

## ⚡ Script e instruções

### 1️⃣ gc_counter.py
**Objetivo:**  
- Calcular a porcentagem de GC em um genoma ou sequências FASTA individuais  
- Contar o número total de nucleotídeos  
- Exibir resultados de forma clara

**Como rodar:**

```bash
python3 gc_counter.py GCF_000005845.2_ASM584v2_genomic.fna
O que esperar:

Tamanho total da sequência

Número de cada nucleotídeo (A, T, G, C)

Percentual de GC

📊 Exemplos de saída
Tamanho total da sequência: 4,639,221 bp
A: 1,085,000
T: 1,091,000
G: 1,214,000
C: 1,249,000
Conteúdo GC: 53.7%

🔍 Conceitos aprendidos

Estrutura de arquivos FASTA

Manipulação de sequências biológicas em Python

Cálculo de proporção de nucleotídeos

Noções básicas de bioinformática aplicadas a genomas completos

📘 Próximos passos

Missão 2: Exploração de arquivos FASTQ e análise de qualidade (veja ../Missao_2_FASTQ/README.md)

Missão 3: Alinhamento de leituras contra referência

---
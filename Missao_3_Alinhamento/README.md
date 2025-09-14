# 📂 Missão 3: Alinhamento de Leituras (RNA-Seq)

Esta pasta contém scripts e arquivos para a **Missão 3**, cujo objetivo é alinhar leituras de RNA-Seq contra um genoma de referência e gerar arquivos prontos para análise downstream.

---

## 🗂 Estrutura da pasta

GCF_000005845.2_ASM584v2_genomic.fna # Genoma de referência (FASTA)
SRR390728_1.fastq.gz # Read 1 do dataset RNA-Seq
SRR390728_2.fastq.gz # Read 2 do dataset RNA-Seq
alinhamento.sam # Alinhamento inicial (SAM)
alinhamento.bam # Alinhamento convertido em BAM
alinhamento_sorted.bam # BAM ordenado
alinhamento_sorted.bam.bai # Índice do BAM
README.md # Este arquivo

---

## ⚡ Passo a Passo

### 1️⃣ Indexar o genoma de referência

```bash
bwa index GCF_000005845.2_ASM584v2_genomic.fna

2️⃣ Alinhar as reads (paired-end)
bwa mem GCF_000005845.2_ASM584v2_genomic.fna SRR390728_1.fastq.gz SRR390728_2.fastq.gz > alinhamento.sam

3️⃣ Converter SAM → BAM e ordenar
samtools view -bS alinhamento.sam > alinhamento.bam
samtools sort alinhamento.bam -o alinhamento_sorted.bam
samtools index alinhamento_sorted.bam

4️⃣ Conferir estatísticas do alinhamento
samtools flagstat alinhamento_sorted.bam

Total de reads

Reads mapeadas

Reads pareadas corretamente

Qualidade geral do alinhamento

📊 Conceitos aprendidos

Alinhamento de reads contra referência (BWA/Bowtie2)

Arquivos SAM/BAM e manipulação com SAMtools

Indexação de genoma e arquivos BAM

Interpretação de estatísticas de alinhamento

Preparação para análises downstream (contagem de genes, chamadas de variantes)

📘 Próximos passos

Missão 4: Chamada de variantes (SNPs/INDELs)

Missão 5: Análise de expressão gênica (RNA-Seq pipeline completo)

Missão 6: Visualização e integração em Python
---

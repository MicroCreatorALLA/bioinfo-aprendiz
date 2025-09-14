# 📂 Missão 4: Chamada de Variantes (SNPs/INDELs)

Esta pasta contém scripts e arquivos para a **Missão 4**, cujo objetivo é detectar variantes genômicas (SNPs e INDELs) a partir de leituras alinhadas (BAM) e gerar arquivos VCF prontos para análise downstream.

---

## 🗂 Estrutura da pasta
GCF_000005845.2_ASM584v2_genomic.fna # Genoma de referência (FASTA)
alinhamento_sorted.bam # Alinhamento das reads (BAM)
alinhamento_sorted.bam.bai # Índice do BAM
README.md # Este arquivo

---

## ⚡ Passo a Passo

### 1️⃣ Gerar arquivo BCF (intermediário)
```bash
bcftools mpileup -f GCF_000005845.2_ASM584v2_genomic.fna alinhamento_sorted.bam -Ou -o variantes.bcf
-f → genoma de referência

-Ou → saída em BCF não comprimido (intermediário)

-o → arquivo de saída

2️⃣ Chamar variantes (SNPs e INDELs)
bcftools call -mv -Ov -o variantes.vcf variantes.bcf
-mv → chama SNPs e INDELs

-Ov → saída em VCF legível

-o → arquivo final

3️⃣ Filtragem de variantes confiáveis
bcftools filter -i 'QUAL>30 && DP>10' variantes.vcf -o variantes_filtradas.vcf

QUAL>30 → qualidade mínima da variante

DP>10 → profundidade mínima de cobertura

4️⃣ Conferir resultados
bcftools view variantes_filtradas.vcf | head -n 20
CHROM → cromossomo

POS → posição da variante

REF → base de referência

ALT → base alternativa (variante)

QUAL → qualidade da chamada

INFO → informações adicionais

📊 Conceitos aprendidos

Como gerar arquivos VCF a partir de BAM

Diferença entre SNPs e INDELs

Filtragem de variantes baseada em qualidade e profundidade

Preparação de dados para análises downstream:

Anotação funcional

Comparação de genomas

Estudos populacionais

📘 Próximos passos

Missão 5: Análise de expressão gênica usando RNA-Seq (contagem de genes)

Missão 6: Visualização e integração em Python (matplotlib, seaborn, pandas)
---

# 📂 Missão 2: FASTQ & Análise de Qualidade

Esta pasta contém scripts e dados da **Missão 2**, cujo objetivo é explorar arquivos FASTQ de RNA-Seq e realizar uma análise de qualidade detalhada das leituras.

---

## 🗂 Estrutura da pasta

SRR390728_1.fastq.gz # Read 1 do dataset RNA-Seq
SRR390728_2.fastq.gz # Read 2 do dataset RNA-Seq
analise_fastq.py # Conta leituras, mostra tamanho médio e cabeçalhos
analise_qualidade.py # Análise de qualidade por posição, composição de bases, CSVs e gráficos
README.md # Este arquivo

---

## ⚡ Scripts e instruções

### 1️⃣ analise_fastq.py
**Objetivo:**  
- Contar o número total de leituras  
- Mostrar tamanho médio das sequências  
- Exibir alguns cabeçalhos das reads

**Como rodar:**
```bash
python3 analise_fastq.py SRR390728_1.fastq.gz
O que esperar:

Total de leituras

Tamanho médio das reads

5 primeiros cabeçalhos (para inspeção rápida)

2️⃣ analise_qualidade.py

Objetivo:

Calcular a qualidade média por posição (Phred scores)

Observar a composição de bases por posição (A/T/G/C/N)

Gerar relatórios em CSV

(Opcional) Criar gráficos PNG com a qualidade por posição

Como rodar (modo rápido, apenas média):
python3 analise_qualidade.py SRR390728_1.fastq.gz --phred 33 --max-reads 200000

Como rodar em modo detalhado (mediana, desvio, usa mais memória):
python3 analise_qualidade.py SRR390728_1.fastq.gz --phred 33 --detailed --max-reads 50000

Como gerar gráficos PNG:

Instale o matplotlib se ainda não tiver:pip3 install matplotlib

Rode o script com:python3 analise_qualidade.py SRR390728_1.fastq.gz --phred 33 --max-reads 100000 --plot

Resultados gerados

*_per_base_quality.csv → Qualidade média por posição

*_per_base_composition.csv → Composição de bases por posição

*_per_read_mean_quals_sample.csv → Distribuição das médias por leitura (amostra)

*_per_base_quality.png → Gráfico da qualidade por posição (se --plot usado)
🔍 Como interpretar

Qualidade média por posição: valores >30 são ótimos; 20–30 aceitáveis; <20 atenção

Composição por posição: deve haver equilíbrio de bases; viés pode indicar problema no library prep

Distribuição das médias: muitas leituras com qualidade baixa → possível problema no sequenciamento

🎓 Conceitos aprendidos

Estrutura e interpretação de arquivos FASTQ

Phred score e conversão ASCII → qualidade

Manipulação eficiente de grandes arquivos em Python

Exportação de dados para CSV e gráficos

Como documentar scripts e resultados para análise reproducível

---

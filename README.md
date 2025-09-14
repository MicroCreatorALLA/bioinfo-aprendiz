# 🧬 Missões de Bioinformática

Este repositório documenta minha **jornada de aprendizado em Bioinformática**, guiada por missões práticas e progressivas — do básico até a maestria.  
A ideia é aprender fazendo, construindo scripts, analisando dados reais de sequenciamento e entendendo os conceitos de forma aplicada.

---

## 🚀 Estrutura do Repositório
missoes_bioinfo/
│
├── Missao_1_GCcounter/
│ └── gc_counter.py # Script Python para calcular o conteúdo GC de um genoma FASTA
│
├── Missao_2_FASTQ/
│ ├── SRR390728_1.fastq.gz # Dados reais de RNA-Seq (read 1)
│ ├── SRR390728_2.fastq.gz # Dados reais de RNA-Seq (read 2)
│ ├── analise_fastq.py # Script simples: conta reads e mostra exemplos de cabeçalhos
│ └── analise_qualidade.py # Script avançado: análise de qualidade estilo FastQC (qualidade média, composição, gráficos)
│
└── README.md # Você está aqui!

---

## 🎯 Missões Concluídas

### 📌 Missão 1: GC Counter
- **Objetivo:** Aprender a manipular arquivos FASTA e contar o conteúdo GC (proporção de guanina+citosina).  
- **Conceitos aprendidos:**
  - Estrutura de arquivos **FASTA**.
  - Manipulação de strings biológicas em Python.
  - Cálculo de proporções nucleotídicas.

### 📌 Missão 2: Exploração de FASTQ
- **Objetivo:** Entender arquivos **FASTQ** e fazer análises básicas de qualidade.  
- **Ferramentas criadas:**
  - `analise_fastq.py`: conta número de leituras, tamanho médio, mostra cabeçalhos.  
  - `analise_qualidade.py`: análise detalhada estilo FastQC (qualidade média por posição, composição de bases, exporta CSV e gráficos).  
- **Conceitos aprendidos:**
  - Estrutura de arquivos **FASTQ** (sequência + qualidade Phred).
  - Como converter caracteres ASCII em scores de qualidade.
  - Noção de **qualidade de sequenciamento** (Phred scores).
  - Uso de Python para bioinformática aplicada (manipulação eficiente de grandes arquivos).
  - Criação de relatórios CSV e visualizações gráficas.

---

## 🔮 Próximas Missões

- Missão 3: Alinhamento de leituras contra um genoma de referência (BWA + SAMtools).
- Missão 4: Chamada de variantes (SNPs/INDELs).
- Missão 5: Análise de expressão gênica (RNA-Seq pipeline).
- Missão 6: Visualização e integração em Python (matplotlib, pandas, seaborn).

---

## 📘 Objetivo Final

Ao final desta jornada, terei desenvolvido:
- Um **pipeline completo** de bioinformática.
- Scripts autorais em Python.
- Entendimento profundo dos **formatos de dados biológicos** (FASTA, FASTQ, SAM/BAM, VCF).
- Base sólida para pesquisa acadêmica e atuação profissional na área.

---

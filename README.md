# 🧬 Missões de Bioinformática

Este repositório documenta minha **jornada prática de aprendizado em Bioinformática**, desde conceitos básicos até análises reais de dados de sequenciamento.  
A ideia é aprender fazendo, construindo scripts em Python, analisando dados reais de FASTA e FASTQ, e aplicando conhecimentos teóricos em tarefas concretas.

---

## 🎯 Objetivos das Missões

### 📌 Missão 1: GC Counter
- **O que fizemos:**  
  - Ler arquivos FASTA, calcular conteúdo GC (guanina + citosina) do genoma.  
- **O que aprendi:**  
  - Estrutura de arquivos FASTA  
  - Manipulação de strings em Python  
  - Cálculos de proporção de nucleotídeos  

### 📌 Missão 2: FASTQ & Análise de Qualidade
- **O que fizemos:**  
  - Baixar dados reais de sequenciamento RNA-Seq (SRR390728)  
  - Criar scripts Python para explorar os dados:
    - `analise_fastq.py` → contagem de reads, tamanho médio, exemplos de cabeçalhos  
    - `analise_qualidade.py` → qualidade por posição, composição de bases, geração de CSVs e gráficos  
- **O que aprendi:**  
  - Estrutura de arquivos FASTQ (sequência + qualidade Phred)  
  - Conversão de caracteres ASCII em scores de qualidade  
  - Noções de qualidade de sequenciamento (Phred score)  
  - Como manipular arquivos grandes eficientemente em Python  
  - Criação de relatórios e gráficos para interpretação de dados  

---

## 🔮 Próximas Missões

- **Missão 3:** Alinhamento de leituras com referência (BWA, Bowtie2, SAMtools)  
- **Missão 4:** Chamada de variantes (SNPs/INDELs)  
- **Missão 5:** Análise de expressão gênica (RNA-Seq pipeline completo)  
- **Missão 6:** Visualização e integração em Python (matplotlib, seaborn, pandas)

---

## 📘 Objetivo Final do Projeto

Ao final deste repositório, terei:
- Um **pipeline completo de bioinformática** para análise de dados de sequenciamento  
- Scripts próprios em Python para análise e manipulação de FASTA e FASTQ  
- Conhecimento profundo dos **formatos de dados biológicos**: FASTA, FASTQ, SAM/BAM, VCF  
- Habilidades aplicáveis em **pesquisa acadêmica e mercado de bioinformática**

---

## ⚡ Dicas de Uso

1. **Não subir arquivos FASTQ grandes no GitHub**; mantenha apenas scripts e resumos.  
2. Scripts Python são independentes — você pode rodar `analise_fastq.py` ou `analise_qualidade.py` em qualquer arquivo FASTQ compactado (`.fastq.gz`).  
3. Os CSVs e gráficos gerados ajudam a interpretar qualidade e composição das leituras.

---

## ✅ Conclusão

Este repositório não é só código — é uma **documentação viva da minha evolução em bioinformática**. Cada missão ensina conceitos práticos, cria ferramentas úteis e registra o aprendizado passo a passo.

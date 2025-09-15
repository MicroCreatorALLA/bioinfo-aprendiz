# Missão 7 – Análise de Genes Diferencialmente Expressos (DGE)

## Objetivo
Identificar genes cuja expressão difere entre duas condições simuladas. Visualizar resultados através de gráficos de **volcano plot** e **heatmap**.

## Procedimentos realizados
1. Criação de ambiente virtual `.venv` e instalação das dependências:
   - pandas, numpy, matplotlib, seaborn, scipy
2. Carregamento dos dados de contagem da Missão 5 (`contagem_genes.txt`)
3. Simulação de duas condições (A e B) com pequenas diferenças nas contagens
4. Cálculo do **log2 Fold Change (log2FC)**
5. Teste estatístico **t-test** entre Condição A e Condição B
6. Geração de gráficos:
   - `volcano_plot.png` → mostra genes com maiores diferenças de expressão
   - `heatmap_dge.png` → visualiza os 20 genes mais diferencialmente expressos

## Resultados
- Todos os scripts rodaram corretamente
- Gráficos gerados e salvos na pasta da missão
- DGE simulada com interpretação básica do volcano plot e heatmap

## Aprendizado
- Introdução à análise de genes diferencialmente expressos
- Uso de bibliotecas Python para análise de dados biológicos
- Visualizações avançadas de dados de RNA-seq
- Integração de estatística e bioinformática

# Missão 6 – Análise Avançada de Expressão Gênica

## Objetivo
Nesta missão, aprofundamos a análise dos dados de expressão gênica da Missão 5, aplicando técnicas de **normalização**, **análise de componentes principais (PCA)** e **visualização de genes mais variáveis** com **heatmaps**. O objetivo é entender padrões de expressão e explorar os dados de forma gráfica e estatística.

## Passo a passo realizado

### 1. Preparação do ambiente
- Criamos a pasta `Missao_6_AnaliseAvancada`.
- Criamos o ambiente virtual `.venv` e instalamos os pacotes necessários:
  - `pandas` → manipulação de tabelas
  - `matplotlib` → gráficos
  - `seaborn` → gráficos estatísticos
  - `scikit-learn` → PCA e análises avançadas

### 2. Script `analise_avancada.py`
- **Leitura dos dados**: carregamos `contagem_genes.txt` gerado pelo `featureCounts`.
- **Identificação da coluna de contagem**: renomeamos a coluna do BAM para `counts`.
- **Normalização CPM (Counts Per Million)**: ajusta as contagens para comparação entre amostras.
- **PCA**:
  - Redução de dimensionalidade das amostras.
  - Permite identificar padrões globais de expressão.
  - Criamos um gráfico `PCA_amostras.png` mostrando a projeção das amostras.
- **Heatmap dos genes mais variáveis**:
  - Selecionamos os 20 genes com maior variabilidade.
  - Geramos o gráfico `heatmap_genes.png`, destacando diferenças de expressão.

### 3. Arquivos gerados
- `analise_avancada.py` → script de análise
- `PCA_amostras.png` → gráfico PCA das amostras
- `heatmap_genes.png` → heatmap dos genes mais variáveis

### 4. Aprendizados em bioinformática
- Como carregar e manipular tabelas de contagem com `pandas`.
- Conceito de **normalização de contagens** (CPM) para comparações entre amostras.
- Uso de **PCA** para explorar variações globais nos dados.
- Criação de **heatmaps** para visualizar genes diferencialmente expressos.
- Como estruturar scripts e ambientes virtuais para análises reproduzíveis.

### 5. Próximos passos
- Aplicar métodos estatísticos de detecção de genes diferencialmente expressos.
- Comparar múltiplas condições ou amostras biológicas.
- Integrar essas análises em pipelines automatizados para estudos futuros.

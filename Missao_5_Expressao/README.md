Missão 5 – Expressão Gênica
Objetivo

Nesta missão, o objetivo foi analisar a expressão gênica de uma amostra sequenciada, utilizando o arquivo de alinhamento BAM obtido na Missão 3, e quantificar o número de reads associados a cada gene usando uma anotação genômica (GTF). Ao final, os dados foram analisados em Python para extrair estatísticas e gerar visualizações.

Arquivos principais

GCF_000005845.2_ASM584v2_genomic.gtf – arquivo de anotação genômica.

alinhamento_sorted.bam – arquivo de alinhamento das leituras (da Missão 3).

contagem_genes.txt – saída do featureCounts com o número de reads por gene.

contagem_genes.txt.summary – resumo do processo do featureCounts.

analise_contagem.py – script Python para análise da tabela de contagens e visualização.

histograma_contagens.png – histograma gerado pelo Python mostrando a distribuição das contagens.

Passo a passo realizado
1. Preparação da anotação

Baixamos o arquivo GTF com as informações de genes e exons do genoma de interesse.

2. Quantificação de expressão

Rodamos o featureCounts para contar reads alinhadas por gene:
Missão 5 – Expressão Gênica
Objetivo

Nesta missão, o objetivo foi analisar a expressão gênica de uma amostra sequenciada, utilizando o arquivo de alinhamento BAM obtido na Missão 3, e quantificar o número de reads associados a cada gene usando uma anotação genômica (GTF). Ao final, os dados foram analisados em Python para extrair estatísticas e gerar visualizações.

Arquivos principais

GCF_000005845.2_ASM584v2_genomic.gtf – arquivo de anotação genômica.

alinhamento_sorted.bam – arquivo de alinhamento das leituras (da Missão 3).

contagem_genes.txt – saída do featureCounts com o número de reads por gene.

contagem_genes.txt.summary – resumo do processo do featureCounts.

analise_contagem.py – script Python para análise da tabela de contagens e visualização.

histograma_contagens.png – histograma gerado pelo Python mostrando a distribuição das contagens.

Passo a passo realizado
1. Preparação da anotação

Baixamos o arquivo GTF com as informações de genes e exons do genoma de interesse.

2. Quantificação de expressão

Rodamos o featureCounts para contar reads alinhadas por gene:
featureCounts -a GCF_000005845.2_ASM584v2_genomic.gtf \
              -o contagem_genes.txt \
              -T 2 \
              alinhamento_sorted.bam

-a → arquivo de anotação (GTF)

-o → arquivo de saída

-T → número de threads

O BAM usado foi o alinhado na Missão 3

O resultado gerou o arquivo contagem_genes.txt com os genes e contagens correspondentes.

3. Análise dos dados em Python

Criamos o ambiente virtual para instalar pacotes isolados:
python3 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib

O script analise_contagem.py realizou:

Leitura do arquivo de contagens com pandas.

Renomeação da coluna longa do BAM para counts.

Exibição das primeiras linhas da tabela.

Resumo das colunas e tipos de dados.

Estatísticas básicas das contagens (média, mínimo, máximo, etc.).

Geração de um histograma (histograma_contagens.png) mostrando a distribuição de contagens por gene.

Exemplo de saída:
=== Primeiras linhas da tabela ===
   Geneid        Chr  Start  ... Strand Length  counts
0   b4413  NC_000913.3  16952  ...     +     59      0
1   b4762  NC_000913.3  75516  ...     -     93      0
...
=== Estatísticas básicas das contagens ===
count    215.000000
mean       5.632558
std       12.453215
min        0.000000
25%        0.000000
50%        0.000000
75%        2.000000
max       85.000000
Name: counts, dtype: float64

Aprendizado

Nesta missão você aprendeu a:

Utilizar featureCounts para quantificação de expressão gênica.

Trabalhar com arquivos BAM e GTF.

Manipular dados tabulares com pandas.

Criar histogramas de distribuição de contagens com matplotlib.

Criar e utilizar ambientes virtuais para gerenciar dependências Python.

Automatizar análises de bioinformática com scripts organizados.

Próximo passo

Com a Missão 5 concluída, os dados de expressão estão prontos para análises mais avançadas, como normalização de contagens, detecção de genes diferencialmente expressos ou análises de pathway em futuras missões.
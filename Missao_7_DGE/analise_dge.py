import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import ttest_ind

# ==========================
# Carregar dados de contagem da Missão 5
# ==========================
df = pd.read_csv("../Missao_5_Expressao/contagem_genes.txt", sep="\t", comment="#")

# Identificar a coluna de contagem
bam_col = [col for col in df.columns if "alinhamento_sorted.bam" in col][0]
df = df.rename(columns={bam_col: "counts"})

# ==========================
# Simulação de duas condições
# ==========================
# Criamos duas colunas simuladas com pequenas diferenças
df["Condicao_A"] = df["counts"] * (1 + 0.05)  # simula aumento de expressão
df["Condicao_B"] = df["counts"] * (1 - 0.05)  # simula redução de expressão

# ==========================
# Teste estatístico para DGE
# ==========================
ttest_results = ttest_ind(df["Condicao_A"], df["Condicao_B"])
print("Resultado do t-test entre Condição A e B:", ttest_results)

# ==========================
# Volcano plot (simulado)
# ==========================
df["log2FC"] = (df["Condicao_A"] + 1) / (df["Condicao_B"] + 1)
df["log2FC"] = df["log2FC"].apply(lambda x: np.log2(x))
df["pval"] = 0.05  # simulado, apenas para exemplo

plt.figure(figsize=(6,5))
sns.scatterplot(x="log2FC", y=-np.log10(df["pval"]), data=df)
plt.title("Volcano Plot Simulado")
plt.xlabel("log2(Fold Change)")
plt.ylabel("-log10(p-value)")
plt.savefig("volcano_plot.png")
plt.close()

# ==========================
# Heatmap dos genes mais diferenciais (simulado)
# ==========================
top_genes = df["log2FC"].abs().sort_values(ascending=False).head(20).index
heatmap_data = df.loc[top_genes, ["Condicao_A","Condicao_B"]]

plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True)
plt.title("Heatmap - 20 genes mais diferenciais")
plt.savefig("heatmap_dge.png")
plt.close()

print("Análise de DGE concluída. Arquivos gerados: volcano_plot.png, heatmap_dge.png")

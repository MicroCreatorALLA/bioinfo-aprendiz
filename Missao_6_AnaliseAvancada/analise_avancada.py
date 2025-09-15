import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# ==========================
# Carregar os dados da Missão 5
# ==========================
df = pd.read_csv("../Missao_5_Expressao/contagem_genes.txt", sep="\t", comment="#")

# Identificar a coluna de contagens
bam_col = [col for col in df.columns if "alinhamento_sorted.bam" in col][0]
df = df.rename(columns={bam_col: "counts"})

# Mostrar primeiras linhas
print("=== Primeiras linhas ===")
print(df.head())

# ==========================
# Normalização simples (CPM)
# ==========================
# CPM = Counts per Million
total_counts = df["counts"].sum()
df["CPM"] = df["counts"] / total_counts * 1e6

print("\n=== Estatísticas da normalização CPM ===")
print(df["CPM"].describe())

# ==========================
# PCA (Principal Component Analysis)
# ==========================
# Para PCA, precisamos de pelo menos duas amostras, mas vamos demonstrar
# criando um dataframe de contagens simuladas com pequenas variações
# para visualização
df_pca = pd.DataFrame({
    "Sample_1": df["CPM"],
    "Sample_2": df["CPM"] * (1 + 0.05),  # simula pequena variação
    "Sample_3": df["CPM"] * (1 - 0.03)
})

# Ajustar PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_pca.T)  # Transposta para amostras x genes

# Plot PCA
plt.figure(figsize=(6,5))
plt.scatter(pca_result[:,0], pca_result[:,1])
plt.title("PCA das amostras (simulado)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("PCA_amostras.png")
plt.close()

# ==========================
# Heatmap dos genes mais variáveis
# ==========================
# Selecionar os 20 genes mais variáveis
top_genes = df_pca.var(axis=1).sort_values(ascending=False).head(20).index
heatmap_data = df_pca.loc[top_genes]

plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, cmap="viridis", annot=True)
plt.title("Heatmap - 20 genes mais variáveis (simulado)")
plt.savefig("heatmap_genes.png")
plt.close()

print("\n=== Análise avançada concluída ===")
print("Arquivos gerados: PCA_amostras.png, heatmap_genes.png")

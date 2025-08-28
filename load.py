# Required libraries
from datasets import load_dataset
import pandas as pd

csv_url = (
    "https://huggingface.co/datasets/AIBIC/MLOmics/resolve/main/"
    "Main_Dataset/Classification_datasets/GS-BRCA/Aligned/BRCA_mRNA_aligned.csv"
)
df_mRNA = pd.read_csv(csv_url)
print(df_mRNA)

# Save locally
df_mRNA.to_csv("/Users/tracyxue/Documents/genomap/data/BRCA_mRNA_aligned.csv", index=False)

print("Saved file as BRCA_mRNA_aligned.csv")

# Repeat for other files as needed:
# - Cancer_miRNA_Feature.csv
# - Cancer_mRNA_Feature.csv
# - Cancer_CNV_Feature.csv
# - Cancer_Methy_Feature.csv
# - Cancer_survival.csv
# just replace file name accordingly.

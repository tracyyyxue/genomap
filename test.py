def main():
    import pandas as pd # Please install pandas and matplotlib before you run this example
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy
    import genomap as gp
    from datasets import load_dataset    

    csv_url = (
        "https://huggingface.co/datasets/AIBIC/MLOmics/resolve/main/"
        "Main_Dataset/Classification_datasets/GS-BRCA/Aligned/BRCA_mRNA_aligned.csv"
    )
    df_mRNA = pd.read_csv(csv_url)
    print(df_mRNA.head())


if __name__=='__main__':
    main()
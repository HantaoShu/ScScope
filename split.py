import glob
import os
import pandas as pd
import numpy as np
import scanpy.api as sc

for i, file in enumerate(glob.glob("*.csv")):
    data = pd.read_csv(file, header=0, index_col=0)
    matrix = data.values
    gene_exp = sc.AnnData(matrix)
    sc.pp.normalize_per_cell(gene_exp)
    gene_exp = gene_exp.X
    os.chdir('./batches/')
    np.save('batch_{}.npy'.format(i), gene_exp)
    os.chdir('../')


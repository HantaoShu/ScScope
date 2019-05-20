import numpy as np
import pandas as pd
import h5py
import scipy.sparse as sp_sparse
import random


filtered_matrix_h5 = '1M_neurons_filtered_gene_bc_matrices_h5.h5'
sample_size = 30000

f = h5py.File(filtered_matrix_h5, 'r')
matrix = sp_sparse.csc_matrix((f['mm10']['data'], f['mm10']['indices'], f['mm10']['indptr']),
                              shape=f['mm10']['shape'])
matrix = matrix.T

num_cells = matrix.shape[0]
sample_true = [True] * sample_size
sample_excl = [False] * (num_cells - sample_size)
sample_bools = sample_true.extend(sample_excl)
random.shuffle(sample_bools)
idx = np.nonzero(sample_bools)[0]

matrix_sample = matrix[idx, :]

pd.DataFrame(matrix_sample).to_csv('30000cells.csv', chunksize=1000)

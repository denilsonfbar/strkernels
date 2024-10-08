
import pandas as pd

def read_fasta_to_dataframe(fasta_file):
    data = []
    with open(fasta_file, 'r') as file:
        sequence_id = None
        sequence = []
        
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id is not None:
                    data.append([sequence_id, ''.join(sequence)])
                sequence_id = line[1:]
                sequence = []
            else:
                sequence.append(line)
        
        if sequence_id is not None:
            data.append([sequence_id, ''.join(sequence)])
    
    df = pd.DataFrame(data, columns=['seqid', 'sequence'])
    return df


from os import path
amp_seqs_file_path = path.join('data', 'Bhadra-et-al-2018', 'train_AMP_3268.fasta')
amp_df = read_fasta_to_dataframe(amp_seqs_file_path)
amp_df['label'] = 1
amp_df

amp_seqs_file_path = path.join('data', 'Bhadra-et-al-2018', 'train_nonAMP_9777.fasta')
non_amp_df = read_fasta_to_dataframe(amp_seqs_file_path)
non_amp_df['label'] = -1
non_amp_df

data_df = pd.concat([amp_df, non_amp_df], axis=0)
data_df


random_seed = 1708  # for reproducing

sampled_amp_df = amp_df.sample(n=len(amp_df) // 10, random_state=random_seed)
sampled_amp_df

sampled_non_amp_df = non_amp_df.sample(n=len(non_amp_df) // 10, random_state=random_seed)
sampled_non_amp_df

sampled_data_df = pd.concat([sampled_amp_df, sampled_non_amp_df], axis=0)
sampled_data_df


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(sampled_data_df['sequence'].values, 
                                                    sampled_data_df['label'].values, 
                                                    stratify=sampled_data_df['label'], 
                                                    random_state=random_seed)
print('Train sequences:',len(X_train))
print('Test sequences:',len(X_test))

from sys import path as sys_path
sys_path.append('..')
from strkernels import SubsequenceStringKernel

# create a kernel
subsequence_kernel = SubsequenceStringKernel(maxlen=1, ssk_lambda=1)

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, matthews_corrcoef

# create a support vector classifier with the kernel
clf = SVC(kernel=subsequence_kernel)

# set parameters for grid search
param_grid = {

#    1
#    'kernel__maxlen': [4, 5, 6],
#    'kernel__ssk_lambda': [0.01, 0.05, 0.1, 0.5, 1.0, 1.5, 2.0],

    'kernel__maxlen': [4, 5, 6],
    'kernel__ssk_lambda': [1.1, 1.2, 1.3, 1.4],
}

mcc_scorer = make_scorer(matthews_corrcoef)

# create the GridSearchCV object
grid_search = GridSearchCV(estimator=clf, 
                           param_grid=param_grid, 
                           scoring=mcc_scorer, 
                           cv=10,
                           n_jobs=-1, 
                           verbose=3)

# fit the model to the training data
grid_search.fit(X_train, y_train)

results = grid_search.cv_results_
df_results = pd.DataFrame(results)
df_results.to_csv('grid_search_results.tsv', sep='\t', index=False)

import polars as pl
import numpy as np
import pandas as pd

def convert(listStr):
    return listStr.replace('[', '').replace(']', '').replace(',', '').replace('\n', '').split(' ')

def combine():

    submission_final = pl.read_csv('~/CIS_4496_Project/data/submission/submission1.csv')

    for i in range(2, 56):
        submission_final = submission_final.vstack(pl.read_csv('~/CIS_4496_Project/data/submission/submission' + str(i) + '.csv'))
    submission_final = submission_final.unique(subset='customer_id', maintain_order=True)

    prediction = pl.Series('prediction', [convert(submission_final.get_column('prediction')[0])])
    for listStr in submission_final.get_column('prediction')[1:]:
        prediction = prediction.append(pl.Series([convert(listStr)]))

    submission_final = submission_final.drop('prediction').hstack([prediction])
    
    
    
    # fix ... in long lists
#     df_ct_final = df_ct_final.to_pandas()
    
#     df_t = pd.read_csv('~/CIS_4496_Project/data/raw/transactions_train.csv')
    
#     for c, alist in zip(df_ct_final['customer_id'], df_ct_final['articles']):    
#         if ('...' in alist):
# #             print(c)
#             df_ct_final = df_ct_final.drop(df_ct_final[df_ct_final['customer_id'] == c].index).reset_index(drop=True)
#             df_ct_final.loc[len(df_ct_final)] = [c, list(df_t[df_t['customer_id'] == c]['article_id'])]

    return submission_final

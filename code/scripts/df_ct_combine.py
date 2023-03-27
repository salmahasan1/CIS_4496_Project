import polars as pl
import numpy as np
import pandas as pd

def convert(listStr):
    return listStr.replace('[', '').replace(']', '').replace(',', '').replace('\n', '').split(' ')

def combine():

    df_ct_final = pl.read_csv('~/CIS_4496_Project/data/df_ct/df_ct1.csv')

    for i in range(2, 48):
        df_ct_final = df_ct_final.vstack(pl.read_csv('~/CIS_4496_Project/data/df_ct/df_ct' + str(i) + '.csv'))
    df_ct_final = df_ct_final.unique(subset='customer_id', maintain_order=True)

    articles = pl.Series('articles', [convert(df_ct_final.get_column('articles')[0])])
    for listStr in df_ct_final.get_column('articles')[1:]:
        articles = articles.append(pl.Series([convert(listStr)]))

    df_ct_final = df_ct_final.drop('articles').hstack([articles])
    
    
    
    # fix ... in long lists
    df_ct_final = df_ct_final.to_pandas()
    
    df_t = pd.read_csv('~/CIS_4496_Project/data/raw/transactions_train.csv')
    
    for c, alist in zip(df_ct_final['customer_id'], df_ct_final['articles']):    
        if ('...' in alist):
            print(c)
            df_ct_final = df_ct_final.drop(df_ct_final[df_ct_final['customer_id'] == c].index).reset_index(drop=True)
            df_ct_final.loc[len(df_ct_final)] = [c, list(df_t[df_t['customer_id'] == c]['article_id'])]

    return df_ct_final
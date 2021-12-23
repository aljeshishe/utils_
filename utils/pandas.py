import pandas as pd
import utils

print('pandas')

VERSIONS = {'dtale': '==1.61.1'}
def reorder_columns(self, *columns):
    # remove columns and add them from the begining
    new_columns = list(columns) + [item for item in self.columns if item not in columns]
    return self[new_columns]


def d(df):
    dtale_ = utils.imp.install_import('dtale', VERSIONS['dtale'])
    dtale_.show(df).open_browser()


def i(df, count=5):
    print(f'{len(df)} rows')
    display(df.head(count))


def drop_from(query_df, df):
    before = len(df)
    print('Going to drop')
    query_df.i()
    df = df.drop(query_df.index)
    after = len(df)
    print(f'Before:{before} after:{after}')
    return df


def patch():
    print('patching pandas')
    pd.core.frame.DataFrame.reorder_columns = reorder_columns
    pd.core.frame.DataFrame.d = d
    pd.core.frame.DataFrame.i = i
    pd.core.frame.DataFrame.drop_from = drop_from


def download(url, headers={}):
    import requests
    print(url)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def preprocess(data):
    return sorted(data, key=lambda item: item['loan_id'])



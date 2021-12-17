import pandas as pd
import utils

print('pandas')

VERSIONS = {'dtale': '==1.61.1'}
def reorder_columns(self, *columns):
    # remove columns and add them from the begining
    new_columns = list(columns) + [item for item in self.columns if item not in columns]
    return self[new_columns]

def show(df, count=5, dtale=False):
    dtale_ = utils.imp.install_import('dtale', VERSIONS['dtale'])
    if dtale:
        dtale_.show(df).open_browser()
    else:
        print(f'{len(df)} rows')
        display(df.head(count))


def patch():
    print('patching pandas')
    pd.core.frame.DataFrame.reorder_columns = reorder_columns
    pd.core.frame.DataFrame.show = show


def download(url, headers={}):
    import requests
    print(url)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def preprocess(data):
    return sorted(data, key=lambda item: item['loan_id'])



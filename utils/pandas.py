import pandas as pd
from datetime import datetime
import json
from pathlib import Path
import common

print('imported')
VERSIONS = {'dtale': '==1.61.1'}
def reorder_columns(self, *columns):
    # remove columns and add them from the begining
    new_columns = list(columns) + [item for item in self.columns if item not in columns]
    return self[new_columns]

def d(df, count=5, dtale=False):
    dtale_ = common.install_import('dtale', VERSIONS['dtale'])
    if dtale:
        dtale_.show(df).open_browser()
    else:
        print(f'{len(df)} rows')
        display(df.head(count))


def patch():
    pd.core.frame.DataFrame.reorder_columns = reorder_columns


def download(url, headers={}):
    import requests
    print(url)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def preprocess(data):
    return sorted(data, key=lambda item: item['loan_id'])


def save(data, prefix=''):
    timestamp = datetime.now().strftime('%y%d%m_%H%M%S')
    with Path(f'{prefix}_{timestamp}.json').open('w', encoding='utf-8') as fp:
        json.dump(data, fp=fp, indent=4, ensure_ascii=False)


def load(filename):
    with Path(filename).open('r', encoding='utf-8') as fp:
        return json.load(fp=fp)


def query(loans, keys):
    results = []

    for loan in loans:
        result = {}
        for new_key_name, key in keys.items():
            # print(key)
            d = loan
            for key_part in key.split('.'):
                # print(key_part)
                d = d[key_part]
            # print(key, d)
            result[new_key_name] = d
        results.append(result)
    return results
# query(load_loans[:2], {'_info.id': 'id', '_info.amount': 'amount'})
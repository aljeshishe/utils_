import json
from pathlib import Path
from datetime import datetime


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
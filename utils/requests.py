import utils


VERSIONS = {'requests': '==2.26.0'}

print('requests')


def request(method, url, *args, **kwargs):
    requests_ = utils.imp.install_import('requests', VERSIONS['requests'])
    r = requests_.request(method, url, *args, **kwargs)
    if r.status_code != 200:
        print(r.__dict__)
    return r

def get(url, *args, **kwargs):
    return request('GET', url, *args, **kwargs)

def post(url, *args, **kwargs):
    return request('GET', url, *args, **kwargs)

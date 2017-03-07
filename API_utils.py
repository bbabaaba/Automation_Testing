import requests


def get(uri=None, host=None):
    # Get Method:
    if uri is None or host is None:
        print "please set value of uri/host, which you want to test."
        return None
    else:
        url = host + uri
        res = requests.get(url=url)
        return res

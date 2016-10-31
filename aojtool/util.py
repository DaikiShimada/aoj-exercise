# -*- coding: utf-8 -*-

import sys
import six

def post(url, query):
    params = six.moves.urllib.parse.urlencode(query)
    params = params.encode('utf-8')

    headers ={
            "pragma":"no-cache",
            "User-Agent":"Opera/9.80 (Windows NT 6.1; U; ja) Presto/2.10.229 Version/11.60",
            }
    res_body = None
    try:
        req = six.moves.urllib.request.Request(url, params ,headers)
        res = six.moves.urllib.request.urlopen(req)
        res_body = str(res.read())
    except six.moves.urllib.error.URLError as e:
        sys.stderr.write(e.reason)
        raise
    return res_body


def get(url, query):
    params = six.moves.urllib.parse.urlencode(query)
    url = url + '?' + params
    res_body = None
    try:
        res = six.moves.urllib.request.urlopen(url)
        res_body = res.read().decode('utf-8')
    except six.moves.urllib.error.URLError as e:
        sys.stderr.write(e.reason)
        raise
    return res_body


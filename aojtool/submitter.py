# -*- coding: utf-8 -*-

import six
import account

def submit(problem, path, lang):
    userid, password = account.get_user_properties()
    with open(path, 'r') as f:
        code = f.read()

    url = 'http://judge.u-aizu.ac.jp/onlinejudge/servlet/Submit'
    data = {
            'userID': userid,
            'sourceCode': code,
            'problemNO': problem,
            'language': lang,
            'password': password,
        }
    params = six.moves.urllib.parse.urlencode(data)
    params = params.encode('utf-8')

    headers ={
            "pragma":"no-cache",
            "User-Agent":"Opera/9.80 (Windows NT 6.1; U; ja) Presto/2.10.229 Version/11.60",
            }
    try:
        req = six.moves.urllib.request.Request(url, params ,headers)
        res = six.moves.urllib.request.urlopen(req)
        res_body = str(res.read())
    except six.moves.urllib.error.URLError as e:
        print(e)
        raise

    print(res_body)
    return res


# -*- coding: utf-8 -*-

import six
import aojtool.account
import aojtool.util

def submit(problem, path, lang):
    userid, password = aojtool.account.get_user_properties()
    with open(path, 'r') as f:
        code = f.read()

    url = 'http://judge.u-aizu.ac.jp/onlinejudge/servlet/Submit'
    query = {
            'userID': userid,
            'sourceCode': code,
            'problemNO': problem,
            'language': lang,
            'password': password,
        }
    return aojtool.util.post(url, query)


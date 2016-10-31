# -*- coding: utf-8 -*-

import json
import aojtool.account
import aojtool.util
from xml.etree import ElementTree

status_code = {
        '0':'Compile Error',
        '1':'Wrong Answer',
        '2':'Time Limit Exceeded',
        '3':'Memory Limit Exceeded',
        '4':'Accepted',
        '6':'Output Limit Exceeded',
        '7':'Runtime Error',
        '8':'Presentation Error',
        }

def dump_node(node):
    ret = {}
    if 'list' in node.tag:
        ret[node.tag] = []
        for child in node:
            ret[node.tag].append(dump_node(child))
        return ret
    elif node.text is not None:
        ret[node.tag] = node.text
    else:
        ret[node.tag] = {}
    for child in node:
        ret.update(dump_node(child))
    return ret


def status_log(user_id=None, problem_id=None, start=None, limit=None):
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/status_log'
    query = {}
    if user_id is not None:
        query['user_id'] = user_id
    if problem_id is not None:
        query['problem_id'] = problem_id
    if start is not None:
        query['start'] = start
    if limit is not None:
        query['limit'] = limit
    res = aojtool.util.get(url, query).replace('\n','')
    elem = ElementTree.fromstring(res)
    return dump_node(elem)


def my_status_log(problem_id=None, start=None, limit=None):
    user_id, _  = aojtool.account.get_user_properties()
    return status_log(user_id=user_id, problem_id=problem_id, start=start, limit=limit)


def judge(run_id):
    url = 'http://judge.u-aizu.ac.jp/onlinejudge/webservice/judge'
    query = {'id': run_id}
    res = aojtool.util.get(url, query).replace('\n','')
    elem = ElementTree.fromstring(res)
    return dump_node(elem)


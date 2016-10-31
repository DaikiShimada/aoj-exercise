#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
import time
import aojtool.submitter
import aojtool.api

def main():
    problem = six.moves.input('Problem ID: ')
    path = six.moves.input('Code path: ')
    lang = six.moves.input('Code lang: ')
    #aojtool.submitter.submit(problem, path, lang)
    #time.sleep(30)
    status = aojtool.api.my_status_log(limit=1)
    judge = aojtool.api.judge(status['status_list'][0]['run_id'])
    print(judge)


if __name__ == '__main__':
    main()

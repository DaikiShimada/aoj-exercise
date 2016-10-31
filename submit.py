#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
import time
import argparse
import aojtool.submitter
import aojtool.api


def print_judge(judge):
    print('********JUDGE RESULT********')
    print('Run ID: {}'.format(judge['judge_id']))
    print('Title: {} ({})'.format(judge['problem_title'],judge['problem_id']))
    print('Submission Date: {}'.format(judge['submissiondate_locale']))
    print('Status: {}'.format(aojtool.api.status_code[judge['status']]))
    print('Accuracy: {}'.format(judge['accuracy']))
    if 'cuptime' in judge:
        print('Cpu Time: {}'.format(judge['cuptime']))
    if 'memory' in judge:
        print('Memory: {}'.format(judge['memory']))
    print('****************************')


def wait_judge(previous, interval=5, trial=10):
    cnt = 0
    latest = previous
    while latest==previous and cnt < trial:
        latest = get_latest_id()
        if latest != previous:
            break
        time.sleep(interval)
    judge = aojtool.api.judge(latest)
    return judge


def get_latest_id():
    status = aojtool.api.my_status_log(limit=1)
    latest_id = status['status_list'][0]['run_id']
    return latest_id


def main():
    # get arguments by argparse
    parser = argparse.ArgumentParser(description='AOJ Submission Tool')
    parser.add_argument('--problem', '-p', type=str, default=None, help='Problem ID')
    parser.add_argument('--src', '-s', type=str, default=None, help='Source Code Path')
    parser.add_argument('--lang', '-l', type=str, default=None, help='Language')
    args = parser.parse_args()

    # get arguments by interactive mode
    problem = six.moves.input('Problem ID: ') if args.problem is None else args.problem
    path = six.moves.input('Code path: ') if args.src is None else args.src
    lang = six.moves.input('Code lang: ') if args.lang is None else args.lang

    # check Submission log before new submission
    latest_id = get_latest_id()

    # submit to AOJ
    aojtool.submitter.submit(problem, path, lang)

    # wait judge
    judge = wait_judge(latest_id)
    print_judge(judge)


if __name__ == '__main__':
    main()

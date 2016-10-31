#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
import aojtool.submitter

def main():
    problem = six.moves.input('Problem ID: ')
    path = six.moves.input('Code path: ')
    lang = six.moves.input('Code lang: ')
    aojtool.submitter.submit(problem, path, lang)


if __name__ == '__main__':
    main()

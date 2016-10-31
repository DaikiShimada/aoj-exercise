# -*- coding: utf-8 -*-

import os
import pit

pit_name = 'aojtools3.account'
opts = {
        'require': {
            'userid': 'your username',
            'password': 'your password',
            }
        }


def config(editor='vi'):
    if not os.environ.get('EDITOR'):
        os.environ['EDITOR'] = editor
    pit.Pit.get(pit_name, opts)


def get_user_properties():
    account = pit.Pit.get(pit_name, opts)
    userid = account['userid']
    password = account['password']

    # strip back-slash
    userid = userid.replace('\\', '')
    password = password.replace('\\', '')

    return userid, password

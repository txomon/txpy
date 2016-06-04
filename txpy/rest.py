from __future__ import unicode_literals


def gen_ok(obj=None, code=200):
    res = {
        '_status': 'OK',
    }
    res.update(obj or {})
    return res, code, {'Content-Type': 'application/json'}


def gen_err(obj=None, code=400, message=''):
    res = {
        '_status': 'ERR',
        '_error': {
            'code': code,
            'message': message
        }
    }
    res.update(obj or {})
    return res, code, {'Content-Type': 'application/json'}

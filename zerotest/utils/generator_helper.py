#!/usr/bin/env python
# encoding: utf-8
import re

INVALID_METHOD_R = re.compile(r'[^a-zA-Z0-9_]')


def get_name_from_request(request):
    return '{}_{}'.format(
        request.method.lower(),
        _path_to_func_name(request.path)
    )


def _path_to_func_name(path):
    """
    Generate a valid python function name for a given request path.

    The valid characters for a Python 2 function name are defined as follows:

    identifier ::=  (letter|"_") (letter | digit | "_")*
    letter     ::=  lowercase | uppercase
    lowercase  ::=  "a"..."z"
    uppercase  ::=  "A"..."Z"
    digit      ::=  "0"..."9"

    :param path: The HTTP request path string.
    :type path: unicode
    :rtype: unicode
    """
    return 'root' if path == '/' else INVALID_METHOD_R.sub('_', path)


def dict_to_param_style_code(d):
    return ', '.join('{0}={1}'.format(k, repr(v)) for k, v in d.items())

# coding: utf-8

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlencode, parse_qsl


def concat_url_and_params(url, params):
    return '?'.join([url, urlencode(params)])


def body_str_to_dict(body):
    return dict(parse_qsl(body))

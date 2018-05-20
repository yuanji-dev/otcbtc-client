# coding: utf-8

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlencode


def concat_url_and_params(url, params):
    return '?'.join([url, urlencode(params)])

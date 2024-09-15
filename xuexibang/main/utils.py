#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='front.home', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


class Page(object):

    def __init__(self, cur_page, per, last_one=False):
        self.cur_page = cur_page
        self.per = per
        self.is_last = last_one
        self.has_prev = (cur_page == 1)

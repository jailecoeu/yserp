#!/usr/bin/env python
# coding: utf-8
'''
Created on 2011-4-20

@author: butter
'''

def paginate(view_func):
    """添加分页支持的修饰函数
    """
    def _add_page(request, *args, **kwargs):
        try:
            request.page = int(request.REQUEST['page'])
        except (KeyError, ValueError, TypeError):
            request.page = 1

        return view_func(request, *args, **kwargs)
    return _add_page

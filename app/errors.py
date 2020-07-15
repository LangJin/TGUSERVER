# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from .utils.retools import responsedata


errorbp = Blueprint("errorbp",__name__)


@errorbp.app_errorhandler(404)
def page_not_found(e):
    return responsedata(msg="%s" % e),404


@errorbp.app_errorhandler(Exception)
def internal_server_error(e):
    status,error = 500, '%s(%s)' % (e.__class__.__name__, str(e))
    return responsedata(msg=error),status
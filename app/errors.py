# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from .utils.retools import responsedata
from werkzeug.exceptions import HTTPException


errorbp = Blueprint("errorbp",__name__)


class EigenException(HTTPException):
    code = 500
    description = '服务器异常，请联系管理员！'



@errorbp.app_errorhandler(Exception)
def internal_server_error(e):
    if isinstance(e, HTTPException):
        status, error = e.code,  e.description
    else:
        status,error = 500, '%s(%s)' % (e.__class__.__name__, str(e))
    return responsedata(msg=error),status
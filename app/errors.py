# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint


errorbp = Blueprint("errorbp",__name__)


@errorbp.app_errorhandler(404)
def page_not_found(e):
    return "404", 404

@errorbp.app_errorhandler(500)
def internal_server_error(e):
    return "500", 500
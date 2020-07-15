# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import jsonify



def responsedata(data=None,msg="操作成功！",status=401):
    """
    构建统一的返回格式
    """
    response = {
        "data":data,
        "msg":msg,
        "status":status
    }
    return jsonify(response)

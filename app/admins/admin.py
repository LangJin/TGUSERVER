# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,make_response
from . import adminbp
from ..utils.dbtools import Db
from ..utils.retools import responsedata
from config import dbinfo


db = Db(dbinfo)


@adminbp.route("/manage/login",methods=["post"])
def login():
    requestdata = request.get_json()
    username = requestdata.get("username")
    password = requestdata.get("password")
    userinfo = db.query("select id,username,password,nickname from t_admins where username = '{}';".format(username))[0]
    if password == userinfo.pop("password"):
        token = "2423t5ertgdygtdfhfghh"
        userinfo.update(token=token)
        return responsedata(data=userinfo,status=200)
    else:
        return responsedata(msg="密码错误！")
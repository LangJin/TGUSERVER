# -*- coding:utf-8 -*-
__author__ = 'LangJin'

# 开发环境
class DevelopConfig:
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB


# 线上发布环境
class ProductionConfig:
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB



flask_config = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
    }


dbinfo = {
    "host":"192.144.148.91",
    "port":3306,
    "user":"ljtest",
    "password":"123456",
    "db":"tgudb"
}
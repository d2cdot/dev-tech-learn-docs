

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""アプリケーションコンフィグ

このモジュールは環境変数を読み込んでモジュール変数に設定を行います。

Attributes:
    TOKEN_SECRETS : トークン生成用のSECRETS
    CORS_DOMAIN : CORSで許可するドメイン
    MAIL_SERVER : サーバ名
    MAIL_PORT : ポート番号
    MAIL_USER : ユーザ名
    MAIL_PASS : パスワード
    MAIL_TO_ADDR : 送信先メールアドレス
"""
import os

CORS_DOMAIN= os.getenv('CORS_DOMAIN',default="*")

TOKEN_SECRETS= os.getenv('TOKEN_SECRETS')
SERVER=os.getenv('MAIL_SERVER')
PORT = os.getenv('MAIL_PORT')
USER = os.getenv('MAIL_USER')
PASS = os.getenv('MAIL_PASS')
MAIL_TO_ADDR = os.getenv('MAIL_TO_ADDR')


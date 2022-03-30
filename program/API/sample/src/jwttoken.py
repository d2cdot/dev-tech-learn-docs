#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import base64
import datetime
import jwt
import APIError
import config
"""AESデコーダ

tokenの生成・認証を行うモジュールです

"""

# 環境変数からConfig取得
time_format= '%Y-%m-%d %H:%M:%S'
def create():
    """トークン生成

    jwtトークンを生成します。expiredは2時間後です。

    Returns:
        bytes: エンコード済みのjwtトークン
    """
    expired = datetime.datetime.now() + datetime.timedelta(hours=2)
    return jwt.encode({"scope": "send","expired":expired.strftime(time_format)}, config.TOKEN_SECRETS, algorithm="HS256")

def verify(headers):
    """トークン検証

    jwtトークンを検証します。
    下記条件が満たされているときのみ正常終了します。
    - jwtトークンがデコード可能である
    - scopeがsendである
    - 現在時刻をexpiredが過ぎていない

    Args:
        headers (dict): Requestのheaderです。Authorizationが設定されていることを前提としています

    Raises:
        APIError.StatusUnauthorizedError: トークン検証に失敗した場合、401を返却します
    """
    try:
        m = re.search(r'Bearer (.*)', headers.get("Authorization"))
        craim = jwt.decode(m.group(1), config.TOKEN_SECRETS, algorithms=["HS256"])
    except Exception as e:
        raise APIError.StatusUnauthorizedError("トークン検証エラー", headers={"WWW-Authenticate":'Bearer realm="jwtssoprotectedrealm"'})
    if craim.get("scope","") !=  "send":
        raise APIError.StatusUnauthorizedError("トークンスコープエラー",headers={"WWW-Authenticate":'Bearer realm="jwtssoprotectedrealm"'})
    if  datetime.datetime.strptime(craim.get("expired",""), time_format) <  datetime.datetime.now():
        raise APIError.StatusUnauthorizedError("トークンタイムアウト",headers={"WWW-Authenticate":'Bearer realm="jwtssoprotectedrealm"'})

def main():
    """
    モジュールを実行した際のエントリポイントです。
    """
    print("本モジュールはパラメータのデコードを担当します。ライブラリとして呼び出してください。")

if __name__ == '__main__':
    main()

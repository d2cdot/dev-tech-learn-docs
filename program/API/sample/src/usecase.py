#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ユースケース

APIシーケンス処理を担当し。APIレスポンスの返却を行います

"""

import json
import mail
import validate
import APIError
import jwttoken
import config
from flask import jsonify

def cors_header():
    return {"Access-Control-Allow-Origin": config.CORS_DOMAIN}

def api_error(e):
    """APIエラー

    APIエラー処理関数です。
    例外発生時に呼び出され、APIレスポンスの生成を行います。

    Args:
        e (exeption): 例外。APIError以外の例外を受け取った場合、500/unknown errorに置き換えを行います

    Returns:
        APIResponse [tuple]: APIレスポンス(tupple)。tuppleの内容は "resuponse body","StatusCode(Default=200)","ResponseHeader(optional)"です
    """
    body = {
            "status": "failed",
            "error": getattr(e, 'message', 'unknown error')
        }
    if hasattr(e, 'detail'):
        body["detail"] = e.detail

    headers = cors_header()
    headers.update(getattr(e, 'headers', {}))

    return jsonify(body), getattr(e, 'statusCode', 500), headers

def token():
    """トークンAPI

    トークンAPIのシーケンス処理です。

    Returns:
        APIResponse [tuple]: APIレスポンス(tupple)。tuppleの内容は "resuponse body","StatusCode(Default=200)","ResponseHeader(optional)"です
    """
    try:
        token_data = jwttoken.create()
    except APIError.APIError as e:
        return api_error(e)
    except Exception as e:
        print(e)
        return api_error(e)
    return jsonify({"status": "success", "token":token_data}), cors_header()

def send(request):
    """メール送信API

    メール送信APIのシーケンス処理です。

    Args:
        request (object): flask requestオブジェクト

    Returns:
        APIResponse [tuple]: APIレスポンス(tupple)。tuppleの内容は "resuponse body","StatusCode(Default=200)","ResponseHeader(optional)"です
    """
    try:
        jwttoken.verify(request.headers)
        payload = request.json
        validate.validate(payload)
        mail.send_mail(payload)
    except APIError.APIError as e:
        return api_error(e)
    except Exception as e:
        print(e)
        return api_error(e)
    return jsonify({"status": "success"}), cors_header()


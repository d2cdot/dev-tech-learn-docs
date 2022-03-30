#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""エントリポイント

APIのエントリーポイントです。app.handlerを起動することでlambda-APIとして振る舞います。

Example:
    DockerのCMDに下記設定を投入することでCallできます
        $ CMD ["app.handler"]

"""
import awsgi
import usecase
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/inquiry/token', methods=['GET'])
def token():
    """tokenAPI
    
    jwtトークンを発行するAPIです。
    sendをCallする前に呼び出す必要があります。
    本APIで取得したTokenをAuthorizationに設定してsendをCallしてください


    Returns:
        APIResponse [tuple]: APIレスポンス(tupple)。tuppleの内容は "resuponse body","StatusCode(Default=200)","ResponseHeader(optional)"です
    """
    return usecase.token()

@app.route('/inquiry/send', methods=['POST'])
def send():
    """sendAPI
    
    お問い合わせを受け付けるAPIです。
    vaidate,メールの送信を行います。

    Returns:
        APIResponse [tuple]: APIレスポンス(tupple)。tuppleの内容は "resuponse body","StatusCode(Default=200)","ResponseHeader(optional)"です
    """
    return usecase.send(request)

def handler(event, context):
    """handler
    
    APIのエントリーポイントです。
    handlerを返却します。

    Args:
        event ([event]): lambda eventオブジェクト
        context ([context]): lambda contextオブジェクト
    """    
    return awsgi.response(app, event, context)

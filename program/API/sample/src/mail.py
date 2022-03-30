#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""メール送信

このモジュールはメール送信用のMIMEを作成し、メール送信を実行します

"""
import smtplib
import os
import APIError
import string
from jinja2 import Environment, FileSystemLoader

from email.mime.text import MIMEText
from email.utils import formatdate
import config

# subjects
category_to_subject={
    1:"アカウント登録・ログイン",
    2:"対応設定",
    3:"電話とか",
    4:"クーポン設定",
    5:"利用履歴",
    6:"店舗について",
    7:"ポイントカードについて",
    8:"店舗を探したい",
    9:"アカウント設定・変更",
    10:"退会",
    11:"一時停止・一時停止解除",
    12:"盗難紛失手続き",
    13:"利用回数のリセット",
    14:"モバイルの更新",
    15:"モバイルの変更手続き",
    16:"モバイル決済の確認",
    17:"エラー・不具合",
    18: "その他（ご意見・ご要望）",
}
# template読み込み
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__), encoding='utf8'))
template = env.get_template('mail.tmpl')

def create_mail_text(payload):
    """メール本文生成

    mail.tmplにpayloadを適用してレンダリングし、メール本文を作成します。

    Args:
        payload (dict): validate済みのpayload

    Returns:
        str: メール本文
    """    
    return template.render(payload) 

def send_mail(payload):
    """メール送信

    MIMEテキストの生成、SMTPサーバへのメール送信要求を実行します。

    Args:
        payload (dict): validate済みのpayload

    Raises:
        APIError.StatusInternalServerError: メールサーバ接続エラー
    """    

    msg = MIMEText(create_mail_text(payload))
    msg['Subject'] = "【お問い合わせ】"  + category_to_subject.get(payload["category"],"") + "について_メール問い合わせ"
    msg['From'] = payload["email"]
    msg['To'] = config.MAIL_TO_ADDR
    msg['Date'] = formatdate()
    err = {}
    try:
        with smtplib.SMTP_SSL(host=config.SERVER, port=config.PORT) as smtp:
            smtp.login(config.USER, config.PASS)
            smtp.send_message(msg)
            smtp.quit()
    except smtplib.SMTPSenderRefused as e:
        raise APIError.StatusBadRequestError("バリデーションエラー",{"email":"※正しいメールアドレスを入力してください"})
    except Exception as e:
        print (e)
        raise APIError.StatusInternalServerError("メール送信エラー")
    return

def main():
    """
    モジュールを実行した際のエントリポイントです。
    """
    print("本モジュールはメール送信を担当します。ライブラリとして呼び出してください。")

if __name__ == '__main__':
    main()

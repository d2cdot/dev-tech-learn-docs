#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""バリデータ設定

このモジュールはvalidateの設定を担当します。
設定項目はcerberusに従います。
また、metaの設定を行うことで対象パラメータ・ルールのvalidate error時のdetail設定を行うことができます。

"""

schema = {
    "name": {
        'type': 'string',
        'required': True,
        'empty': False,
        'maxlength': 100,
        # エラーメッセージを定義
        'meta': {
            'default': '※お名前（漢字）を入力してください',
            'maxlength': '※正しいお名前（漢字）を入力してください',
        }
    },
     "furigana": {
        'type': 'string',
        'required': True,
        'empty': False,
        'maxlength': 100,
        'regex': r'^[ァ-ヶー　]+$',
        'meta': {
            'default': '※お名前（フリガナ）を入力してください',
            'maxlength': '※正しいお名前（フリガナ）を入力してください',
            'regex': '※全角カタカナで入力してください',
        }

    },
    "email":{
        'type': 'string',
        'required': True,
        'empty': False,
        'nullable': False,
        'maxlength': 80,
        'regex': r'^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
        'meta': {
            'default': '※正しいメールアドレスを入力してください',
        }
    },
    "tel": {
        'type': 'string',
        'required': True,
        'empty': False,
        'minlength': 10,
        'maxlength': 11,
        'regex': r'^[0-9]+$',
        'meta': {
            'default': '※電話番号を入力してください',
            'minlength': '※10桁もしくは11桁の電話番号を入力してください',
            'maxlength': '※10桁もしくは11桁の電話番号を入力してください',
            'regex': '※半角数字のみで入力してください',
        }
    },
    "category": {
        'type': 'integer',
        'required': True,
        'empty': False,
        'min': 1,
        'max': 18,
        'meta': {
            'default': '※お問い合わせ種別を選択してください',
        }
    },
    "contents": {
        'type': 'string',
        'required': True,
        'empty': False,
        'maxlength': 4000,
        'meta': {
            'default': '※お問い合わせ内容を入力してください',
            'maxlength': '※4000文字以内で入力してください',
        }
    },
    "device": {
        'type': 'string',
        'required': False,
        'empty': True,
        'nullable': True,
        'meta': {
        }
    },
    "device_version": {
        'type': 'string',
        'required': False,
        'empty': True,
        'nullable': True,
        'meta': {
        }
    },
    "app_version": {
        'type': 'string',
        'required': False,
        'empty': True,
        'nullable': True,
        'meta': {
        }
    }
}

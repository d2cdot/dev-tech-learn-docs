#!/usr/bin/env python
# -*- coding: utf-8 -*-
import APIError
import cerberus
import validate_conf
from cerberus import Validator
from cerberus.errors import BasicErrorHandler

"""バリデータ

バリデータモジュールです。バリデーション設定はvalidate_conf.pyから読み込みます

"""

class CustomErrorHandler(BasicErrorHandler):
    """カスタムエラーハンドラ
    cerberusのエラーハンドラの置き換えを行います。
    バリデーション実施時のerrorsにパラメータとエラー内容に紐付いたメッセージをmetaから読み込んで設定できるようにします。
    """
    def __init__(self, schema):
        self.custom_defined_schema = schema

    def _format_message(self, field, error):
        return self.custom_defined_schema[field].get('meta', {}).get(error.schema_path[1],  self.custom_defined_schema[field].get('meta', {}).get("default", "エラーメッセージが定義されていません"))

def format(errors):
    """フォーマット

    エラーをレスポンス用にフォーマットする。

    Args:
        errors (list): validateから取得されたエラー

    Returns:
        list: フォーマット済みのエラー
    """
    format_errors = {}
    for error in errors:
        format_errors[error] = errors[error].pop()
    return format_errors

def validate(value):
    """バリデート実行

    バリデートを実行します。
    valueに"device"が含まれている場合、mobileapp用のスキーマを読み込みます。
    valueに"device"が含まれていない場合、website用のスキーマを読み込みます。

    Args:
        value (dict): バリデート対象になるパラメータオブジェクト

    Raises:
        APIError.StatusBadRequestError: バリデーションエラーになった場合、401を返却します
    """

    schema = validate_conf.schema

    v = Validator(schema, error_handler=CustomErrorHandler(schema))
    v.allow_unknown = True
    if not v.validate(value):
        raise APIError.StatusBadRequestError("バリデーションエラー",format(v.errors))
    return

def main():
    """
    モジュールを実行した際のエントリポイントです。
    """
    print("本モジュールはメール送信を担当します。ライブラリとして呼び出してください。")

if __name__ == '__main__':
    main()

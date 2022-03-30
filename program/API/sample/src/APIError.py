#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""API例外モジュール.

このモジュールはレスポンスを作成しやすいAPI例外を定義します。

HTTPStatusCodeをメンバーに持っているので、APIエラーになる問題が発生した時点で指定したいステータスコードの例外をraiseしてください。

Example:
    例外を発生させる:
    literal blocks::
        raise APIError.StatusUnauthorizedError("トークン検証エラー", headers={"WWW-Authenticate":'Bearer realm="jwtssoprotectedrealm"'})
    例外を処理する:
    literal blocks::
        except APIError.APIError as e:
            body = {
                    "error": getattr(e, 'message', 'unknown error')
                }
            if hasattr(e, 'detail'):
                body["detail"] = e.detail
            return jsonify(body), getattr(e, 'statusCode', 500), getattr(e, 'headers', [])
"""

class APIError(Exception):
    """API例外基底クラス

    APIエラーを受け取る基底クラスです。

    Args:
        message (str): エラーメッセージです。発生したエラーの説明を設定してください.
        detail (:obj:): 詳細エラーです。validate等詳細なエラー情報をResponseしたい場合に利用してください。json化可能なオブジェクトなら何を設定しても問題ありません。
        headers (dict[str, str]): ヘッダー情報です。エラーに関連してレスポンスヘッダーに設定したい情報を設定してください。

    Attributes:
        message (str): エラーメッセージです。初期設定は"Error"です
        detail (:obj:): 詳細エラーです。初期設定はNoneです。
        headers (dict[str, str]): ヘッダー情報です。初期設定はNoneです。

    """
    def __init__(self,  message= "Error", detail=None,headers=None):
        self.message = message
        if detail is not None:
            self.detail = detail
        if headers is not None:
            self.headers = headers

class StatusBadRequestError(APIError):
    """400 Bad Request
    
    リクエストが不正である。定義されていないメソッドを使うなど、クライアントのリクエストがおかしい場合に返される。

    Attributes:
        statusCode : 400
    """
    statusCode = 400

class StatusUnauthorizedError(APIError):
    """401 Unauthorized
    
    認証が必要である。Basic認証やDigest認証などを行うときに使用される。

    Attributes:
        statusCode : 401
    """
    statusCode = 401

class StatusForbiddenError(APIError):
    """403 Forbidden
    
    リクエストが不正である。定義されていないメソッドを使うなど、クライアントのリクエストがおかしい場合に返される。

    Attributes:
        statusCode : 403
    """
    statusCode = 403

class StatusNotFoundError(APIError):
    """404 Not Found
    
    未検出。リソース・ページが見つからなかった。

    Attributes:
        statusCode : 404
    """
    statusCode = 404

class StatusConflictError(APIError):
    """409 Conflict
    
    競合。要求は現在のリソースと競合するので完了出来ない。

    Attributes:
        statusCode : 409
    """
    statusCode = 409

class StatusInternalServerError(APIError):
    """500 Internal Server Error
    
    サーバ内部エラー。サーバ内部にエラーが発生した場合に返される。

    Attributes:
        statusCode : 500
    """
    statusCode = 500

class StatusBadGatewayError(APIError):
    """502 Bad Gateway
    
    不正なゲートウェイ。ゲートウェイ・プロキシサーバは不正な要求を受け取り、これを拒否した。

    Attributes:
        statusCode : 502
    """
    statusCode = 502

class StatusServiceUnavailable(APIError):
    """503 Service Unavailable
    
    サービス利用不可。サービスが一時的に過負荷やメンテナンスで使用不可能である。
    
    Attributes:
        statusCode : 503
    """
    statusCode = 503

class StatusGatewayTimeout(APIError):
    """504 Gateway Timeout
    
    ゲートウェイタイムアウト。ゲートウェイ・プロキシサーバはURIから推測されるサーバからの適切なレスポンスがなくタイムアウトした。

    Attributes:
        statusCode : 504
    """
    statusCode = 504
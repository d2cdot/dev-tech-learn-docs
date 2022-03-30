#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py,mail.py テスト用コード
## mail.pyはapp.pyに包含してテストを行う。
import sys
import os
import json
import unittest
from unittest.mock import patch
from email.mime.text import MIMEText
from email.header import decode_header
import base64
import datetime
import jwt
import smtplib 

path = os.path.join(os.path.dirname(__file__), '../src')
sys.path.append(path)

class Test_app(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        self.env = patch.dict('os.environ',
            {
                'MAIL_SERVER':'test',
                'MAIL_PORT':'8025',
                'MAIL_USER':'mail_user',
                'MAIL_PASS':'password',
                'MAIL_TO_ADDR':'recive@example.com',
                'ENCRYPT_KEY':'80GsD4k2lUy7TDBvoqitf1lCBylFaAmm',
                'TOKEN_SECRETS':'test',
                'ENCRYPT_VECTOR':'A123456789B123==',
            }
        )
    def test_app_1_1_1(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                }

                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                headers = {'Authorization': 'Bearer ' + data.get("token","")}
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers=headers
                )
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})

                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】アカウント登録・ログインについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_2(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    
                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                self.assertEqual(response.status_code, 200)

                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】対応設定について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_3(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":3,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】電話とかについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_4(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":4,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】クーポン設定について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)

    def test_app_1_1_5(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":5,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】利用履歴について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_6(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":6,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】店舗についてについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_7(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":7,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】ポイントカードについてについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_8(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":8,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】店舗を探したいについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_9(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":9,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】アカウント設定・変更について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)

    def test_app_1_1_10(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":10,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】退会について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)

    def test_app_1_1_11(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":11,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】一時停止・一時停止解除について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_12(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":12,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    

                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】盗難紛失手続きについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)

    def test_app_1_1_13(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":13,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】利用回数のリセットについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_14(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":14,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】モバイルの更新について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_15(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":15,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】モバイルの変更手続きについて_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_16(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":16,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】モバイル決済の確認について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_17(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # テスト対象

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":17,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                # mockの呼び出し記録を確認
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】エラー・不具合について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_min.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_1_18(self):

        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":18,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "success"})
                # mockの呼び出し記録を確認
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                context = mock.return_value.__enter__.return_value
                context.login.assert_called_with("mail_user","password")
                context.quit.assert_called()

                msg = context.send_message.call_args.args[0]
                self.assertEqual(decode_header(msg["Subject"])[0][0],"【お問い合わせ】その他（ご意見・ご要望）について_メール問い合わせ")
                self.assertEqual(decode_header(msg["From"])[0][0],"send@example.com")
                self.assertEqual(decode_header(msg["To"])[0][0],"recive@example.com")
                test_pattern = "test_mail_max.txt"
                with open(os.path.dirname(__file__)+"/mail_test_pattern/"+test_pattern,encoding="utf-8") as f:
                    s = f.read()
                self.assertEqual(msg.get_payload(decode=True).decode(),s)


    def test_app_1_2_1(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":19,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )
                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json,  {"status": "failed", "error": "バリデーションエラー", "detail": {"category": "※お問い合わせ種別を選択してください"}})
                # mail mockが呼ばれていないことを確認
                mock.assert_not_called()

    def test_app_1_2_2(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    

                }
                # 検証実施
                mock.side_effect = Exception("Mock Exception")
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 500)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json, {"status": "failed", "error": "メール送信エラー"})
                # mockの呼び出し記録を確認
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                context = mock.return_value.__enter__.return_value
                context.login.assert_not_called()
                context.quit.assert_not_called()
                context.send_message.assert_not_called()

    def test_app_1_2_3(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com"
                }

                # 検証実施
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                headers = {'Authorization': 'Bearer ' + "ERROR"}
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers=headers
                )

                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.headers["WWW-Authenticate"], 'Bearer realm="jwtssoprotectedrealm"')
                self.assertEqual(response.json, {"status": "failed", "error": "トークン検証エラー"})
                # mockの呼び出し記録を確認
                mock.assert_not_called()


    def test_app_1_2_4(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com"
                }


                # 検証実施
                expired = datetime.datetime.now() + datetime.timedelta(hours=2)
                data = jwt.encode({"scope": "recieve","expired":expired.strftime('%Y-%m-%d %H:%M:%S')}, os.getenv('TOKEN_SECRETS'), algorithm="HS256")
                headers = {'Authorization': 'Bearer ' + data}
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers=headers
                )

                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.headers["WWW-Authenticate"], 'Bearer realm="jwtssoprotectedrealm"')
                self.assertEqual(response.json, {"status": "failed", "error": "トークンスコープエラー"})
                # mockの呼び出し記録を確認
                mock.assert_not_called()


    def test_app_1_2_5(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()
                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789",
                    "email":"send@example.com"
                }

                # 検証実施
                token = self.client.get('/inquiry/token')
                expired = datetime.datetime.now() + datetime.timedelta()
                data = jwt.encode({"scope": "send","expired":expired.strftime('%Y-%m-%d %H:%M:%S')}, os.getenv('TOKEN_SECRETS'), algorithm="HS256")
                headers = {'Authorization': 'Bearer ' + data}
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers=headers
                )

                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.headers["WWW-Authenticate"], 'Bearer realm="jwtssoprotectedrealm"')
                self.assertEqual(response.json, {"status": "failed", "error": "トークンタイムアウト"})
                # mockの呼び出し記録を確認
                mock.assert_not_called()


    def test_app_1_2_6(self):
        with self.env:
            with unittest.mock.patch('smtplib.SMTP_SSL', autospec=True) as mock:
                import app
                app.app.config['TESTING'] = True
                self.client = app.app.test_client()

                # 引数設定
                body = {
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":1,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    

                }
                # 検証実施
                mock.side_effect = smtplib.SMTPSenderRefused("","","")
                token = self.client.get('/inquiry/token')
                data = json.loads(token.data)
                response = self.client.post('/inquiry/send',
                    json = body,
                    headers={'Authorization': 'Bearer ' + data.get("token","")}
                )

                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.headers["Content-Type"], "application/json")
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
                self.assertEqual(response.json, {"status": "failed", "error": "バリデーションエラー",'detail': {'email': '※正しいメールアドレスを入力してください'}})
                # mockの呼び出し記録を確認
                mock.assert_called_with(
                    host = "test",
                    port = "8025"
                )
                context = mock.return_value.__enter__.return_value
                context.login.assert_not_called()
                context.quit.assert_not_called()
                context.send_message.assert_not_called()

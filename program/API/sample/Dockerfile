# AWS lambda用のベースイメージを利用
FROM public.ecr.aws/lambda/python:3.8

# 実装を実行ディレクトリに転送
COPY src ${LAMBDA_TASK_ROOT}

# pythonパッケージをインストール
RUN pip install -r requirements.txt

# lambdaで実行する関数を指定
CMD ["app.handler"]
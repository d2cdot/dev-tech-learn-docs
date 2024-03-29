# お問い合わせAPIのsample解説
https://github.com/d2cdot/dev-tech-learn-docs/tree/main/program/API/sample

お問い合わせAPIの実装例とその解説です。
# アーキテクチャの話
- 本実装のアーキテクチャのベースはクリーンアーキテクチャですが、規模が小さいので役割をまとめて再整理しています。
    - 結果MVCみたいな事になりました。
- 規模が非常に小さかったのでコンポーネントごとのディレクトリ分けは行っていません。

## コンポーネント(カッコ内はクリーンアーキテクチャ上の立ち位置、MVC上の立ち位置)
### エントリーポイント(フレームワークとインターフェースアダプター,View)
- 含まれる実装
    - app.py
- アプリケーションのエントリーポイントとフレームワークの読み込み、APIRequestとメソッドの紐付けを行います。
- 基本的に１ファイルです。

### コンフィグ(インターフェースアダプターの一部,C/M)
- 含まれる実装
    - config.py
- アプリケーションの設定として、環境変数の取得を行います。
  - 外部接続先の設定や暗号化キーなどを設定しています。
- 他のすべての実装から参照されることを前提としています。
- 長くなりすぎる場合、機能部ごとに分割しても良いですが、Configを分割するような規模の場合は別のアプリケーションに切り出したほうが良いです

### シーケンス(ユースケース,C)
- 含まれる実装
    - usecase.py
    - APIError.py
- シーケンスの記述とAPIResponseの作成を行っています。
    - シーケンスの記述だけを行うことによって設計と実装を強く一致させる事を目的としています
- APIの場合、Response生成周りやRequestの取得周りはここにまとめたほうが都合が良いことが多いです。
    - 入出力の管理はシーケンスと併せて管理したほうが楽です。
    - 例外が発生しない限りは正常のResponse,例外発生時は例外に指定されたステータスコードで準正常・異常のResponseを返却するようにしています
- 一つのアプリケーションにいろいろなAPIを実装する場合、パスなどの単位で分割してあげると良いと思います。
- 分割する必要がある場合、別のアプリケーションに切り出したほうが良いことが多いです

### ロジック(エンティティとドライバ, Model)
- 含まれる実装
    - jwttoken.py
    - validate.pyとvalidate_conf.py
    - mail.pyとmail.tmpl
- シーケンス中から実行される各処理を記述しています。
    - JWT認証、バリデーション、メール送信等、色々。
- 機能が増えればふえるほど、ここが大きくなります。
    - 無尽蔵に増える部分なので必要に応じてディレクトリで整理しても良いと思います

# テストの話
- テストの作り方の基本は[テストの資料](../test/) を読んでください
- testディレクトリにtestケースを記述しています。
- 本リポジトリをCloneして、sample配下で[テスト環境のREADME.md](https://github.com/d2cdot/dev-tech-learn-docs/tree/main/program/API/sample/tests)に従うとテスト実行できます。
    - python3.8.0/pipで関連パッケージをインストールする必要があります

## testcase_app
- アプリケーション自体の単体テストです。
    - flask側の機能でAPIの疑似実行を行って検証をしています。
    - 接続先のメールサーバについてはmockを利用して疑似実行しています。
- 単体テストはすべての動作パターンを検証できれば良いので、アプリケーション全体のテストで全ルートが網羅できる場合はアプリケーション全体のテストで記述して問題ありません。

## testcase_validate
- バリデーションに関しては、パラメータパターン数が非常に多く、単独でテスト可能なことから個別にすべてのパターンを書いています。
- testcase_appではバリデーションの結果によって動作が変わる部分については全パターンテストを行い、各パラメータの正常・異常動作に関してはtestcase_validateで確認しています。

# コンテナとlambdaの話
- sampleではlambda用のコンテナを作成することができます。
- 何をやってるかは[Dockerfile](https://github.com/d2cdot/dev-tech-learn-docs/blob/main/program/API/sample/Dockerfile) もご確認お願いします

## コンテナのビルド
sample直下で docker build .を行うとコンテナをビルドできます。

- lambda用のベースパッケージを利用し、ソースファイルをlambda用のルートに転送しています。
- src配下のrequirements.txtを利用して依存パッケージのインストールを行っています。
- CMDに設定したプログラムファイル(今回はapp.py)の中から指定した関数(handler)を読み込んで起動します。
    - 今回はフレームワークを使っているのでhandlerをReturnしていますが、フレームワークを使わなくても文字列をReturnするとAPIでその文字列を返却することができます。

## コンテナをECRにpush
- lambdaでコンテナを使うにはECRにpushしてlambda環境から参照できるようにする必要があります。
- AWSコンソール上なりCLIなりでECRのリポジトリを作成して、コンテナをpushしてください。

## コンテナからlambdaを作成
- 基本的には下記のような手順で実行可能です。version up時は新しくpushされたイメージを選択するだけです。
- 自動デプロイなどを仕込まない限り、ecrが更新されてもlambdaが更新されることはありません。
    - （タグ指定でコンテナを取得した場合でも特定のイメージバージョンに固定されます）

1. lambdaの新しい関数の作成でコンテナイメージを選択
2. イメージを参照 で push したイメージを選択
3. 名前などを設定
4. 環境変数を設定

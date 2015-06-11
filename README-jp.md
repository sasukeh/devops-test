# Quipper DevOps テスト

## 課題 1: プログラミング

### 制約

- 課題を達成するために、最低1つ以上のコードを書いてください。
  - プログラミング言語は何を使っても構いません。
- 課題の中で、最低1つ以上の SQL または SQL-like なクエリを利用できるデータベースを利用してください。
  - 例: PostgreSQL, MySQL, sqlite3, Google BigQuery, InfluxDB など

### 課題内容

- `logs` フォルダに含まれる5個のログファイルをパースし、データベースにデータを格納してください。
  - 各ファイルは日時のデータを持ち、gzip で圧縮されています
  - ログファイルのフォーマットは LTSV です
- 使用したデータベースに対して、以下の結果を返す SQL を書いてください。
  - 各`uri`ごとのの日毎のアクセス数
  - 各日の Top 10 のリクエストタイムをもつログデータ抽出

## 課題 2: システム設計

面接の場で、下記いずれかについてあなたが考えたシステム設計案をプレゼンしてください。
ホワイトボードに描くこともできますし、事前に補足資料を準備して持ち込んでも構いません。
システムの設計にあたって、制約はありません。

1. 非同期ジョブシステム
2. ユニバーサルプッシュ通知システム

### 非同期ジョブシステム

- 複数の Web アプリケーションから共通で使える非同期ジョブの基盤を提供する
  - 対称となるのは時間がかかる処理。例えば、動画のエンコーディングや大量のサムネイルの作成など。
- 非同期ジョブが失敗した場合は、自動的に5回リトライする
- 5回失敗した非同期ジョブはシステム管理者にエラー通知する
- 非同期ジョブが終了したら、成否に関わらず結果をユーザに通知したい。
  - これは可能か？どのような制約をつければ実現できるか？

### ユニバーサルプッシュ通知システム

- Android, iOS, デスクトップの Web ブラウザに同時にプッシュ通知を送る共通インターフェースを提供する
- 通知を開いたかどうか、もしくは通知経由でユーザがアクションを取ったかどうかを検知したい。
  - これは可能か？どのような制約をつければ実現できるか？
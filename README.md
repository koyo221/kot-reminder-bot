# KOTリマインダーBot
## QR
## 概要
出勤/退勤時刻になったらリマインドしてくれるひよこのLineBotです。<br>
こんな人におすすめ→毎月タイムカードを切るのを忘れまくっている
## 使い方
1. 上のQRからLINEで友達登録をしてください。
2. HH/HHで出勤時刻/退勤時刻を入力して下さい。例) 10/19
## 機能
- 出勤/退勤時刻にプッシュ通知を行う
- 「出勤」/「退勤」とメッセージを送ると打刻ページのURLを返す
- 1/10の確率で出勤/退勤時に普段と異なる特殊メッセージを送る
- 「記事」とメッセージを送るとランダムな記事のURLを返す
## 構成
API: Flask(Python)<br>
DB(?): Spread Sheet<br>
Server: Heroku
## 注意事項
無料サーバーを使っているため、レスポンスが遅い、またはタイムアウトする場合があります。<br>
また、もし利用人数が想像以上に増えてきてLine Messaging APIやHerokuの無料枠を超えるとサーバーが止まりますが、その時はすみません。<br>
🐥←免責のひよこ
## さいごに
バグなどを発見した場合製作者までご連絡いただけると幸いです。
また、質問や要望等についても、いつでもどうぞ。

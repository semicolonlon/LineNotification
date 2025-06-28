# LineNotification
Library of LINE API
とりあえずはLINE APIを使用してテキストメッセージのみ送信することができます。
# 使い方
とりあえず LINE でビジネスアカウントを作成し、ボットを作成するところまではお願いします。
https://developers.line.biz/ja/docs/messaging-api/getting-started/

完了したら、このファイルをプロジェクトと同じ階層に配置しインポートしてください。
```.py
from LineNotification import sendMessage
sendMessage("こんにちは", "ボットのアクセストークン", "ボットのユーザーID")
```
終わり。お疲れ様でした

-semicolonlon 2025-


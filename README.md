# 校正ツール

## ツールの動かし方

1. サーバを起動

```
$ git clone https://github.com/fumihiko-takahashi/proofreading_tool.git

$ cd proofreading_tool

$ pip install -r requirements.txt （最初だけ）

$ python server.py
```

2. ブラウザでツールを開く

ブラウザ(Google Chromeとか)で、`http://localhost:5000/` にアクセスする。

3. 語句置換時に起こり得る問題

- 送り仮名のつく単語・動詞などの活用形がある場合  
  - ex.「走る」「走った」どちらも「はしる」「はしった」としたい  
    - →「走」を指定して置換すると「走者」なども置換されてしまう  
     - →正規表現を使ってみたが他によい方法ある？

## 開発

デバッグ用に `sample.py` を用意した。

```bash
# 先にsample.pyの中のinput_textを任意の文字に書き換える
$ python sample.py
いっせいにはしる
```

## TODO

- [ ] 固有名詞中に置換対象の語句がある場合の対処
  - ex.「薔薇」を「バラ」にしたいが、「釘崎野薔薇」という名前のキャラもいる  
   - →janomeで使えるNEologd辞書の公開されているパッケージだとwindowsでは動かない？
  - ex.「京大」をすべて「京都大学」にしたいが、「東京大学」が固有名詞なので変になる  
- [ ] 外部ファイルからルールを取り込む

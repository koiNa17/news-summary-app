# 金融ニュース要約ダッシュボード

RSSフィードから金融ニュースをリアルタイムで取得し、AIが市場動向を要約・センチメント分析するWebアプリです。

## 機能

- Bloomberg・Yahooニュース経済・日経クロステックからニュースを自動取得
- OpenAI GPT-4o-miniによる市場動向の日本語要約
- ニュース見出しごとのセンチメント分析（ポジティブ／ネガティブ／ニュートラル）
- カテゴリ別の絞り込み表示

## 使用技術

- Python 3.11
- Streamlit
- OpenAI API（GPT-4o-mini）
- feedparser
- Docker（Dev Container）

## 起動方法

```bash
streamlit run app.py
```

## 開発背景

金融機関・公的機関でのリサーチ業務の経験から、市場情報を素早くキャッチアップするツールの必要性を感じ制作しました。
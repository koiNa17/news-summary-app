# AIに要約・分析させるファイル。
# fetcher.pyで取得したニュースの見出しと概要を、OpenAI APIに送って以下の2つをやらせる。
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 記事リストを受け取って市場全体の要約を返す関数。
def summarize_news(articles):
    headlines = "\n".join([
        f"・{a['source']}: {a['title']}"
        for a in articles
    ])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "あなたは金融市場のアナリストです。日本語で簡潔に回答してください。"
            },
            {
                "role": "user",
                "content": f"以下のニュース見出しをもとに、今日の市場動向を3文で要約してください。\n\n{headlines}"
            }
        ]
    )

    return response.choices[0].message.content

# 記事の見出し1件を受け取って、センチメントを返す関数。
def analyze_sentiment(title):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "あなたは金融市場のアナリストです。"
            },
            {
                "role": "user",
                "content": f"以下のニュース見出しのセンチメントを「ポジティブ」「ネガティブ」「ニュートラル」の1語のみで答えてください。\n\n{title}"
            }
        ]
    )

    return response.choices[0].message.content.strip()

# テスト用コード
if __name__ == "__main__":
    from fetcher import fetch_news

    articles = fetch_news()
    print("市場まとめを生成中．．．")
    summary = summarize_news(articles)
    print(f"\n【市場まとめ】\n{summary}")

    print("\n【センチメント分析】")
    for a in articles[:3]:
        sentiment = analyze_sentiment(a["title"])
        print(f"{sentiment} | {a['title']}")

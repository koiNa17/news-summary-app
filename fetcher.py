# ニュースを取得するpyファイル

import feedparser     # RSSフィードを取得・解析するライブラリ


RSS_FEEDS = {
    "Bloomberg": "https://feeds.bloomberg.com/markets/news.rss",
    "Yahooニュース経済": "https://news.yahoo.co.jp/rss/topics/business.xml",
    "日経クロステック": "https://xtech.nikkei.com/rss/index.rdf",
}

def fetch_news():
    articles = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            articles.append({
                "source": source,
                "title": entry.title,
                "summary": entry.get("summary", ""),
                "link": entry.link,
                "published": entry.get("published", ""),
            })
    
    return articles

# テスト用コード
if __name__ == "__main__":
    articles = fetch_news()
    print(f"取得件数: {len(articles)}件")
    for a in articles[:3]:
        print(f"[{a['source']}] {a['title']}")
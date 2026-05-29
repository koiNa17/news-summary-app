import streamlit as st
from fetcher import fetch_news
from summarizer import summarize_news, analyze_sentiment

st.set_page_config(
    page_title="金融ニュース要約ダッシュボード",
    page_icon="📰",
    layout="wide"
)

st.title("📰 金融ニュース要約ダッシュボード")
st.caption("RSSフィードからニュースを取得し、AIが要約・センチメント分析します")

CATEGORIES = {
    "すべて": None,
    "Bloomberg": "Bloomberg",
    "Yahooニュース経済": "Yahooニュース経済",
    "日経クロステック": "日経クロステック",
}

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("最新を取得"):
        st.cache_data.clear()

@st.cache_data(ttl=300)
def load_news():
    return fetch_news()

articles = load_news()

with st.spinner("AIが市場を分析中..."):
    summary = summarize_news(articles)

st.subheader("今日の市場まとめ")
st.info(summary)

st.subheader("ニュース一覧")

selected = st.radio(
    "カテゴリで絞り込む",
    options=list(CATEGORIES.keys()),
    horizontal=True
)

filter_source = CATEGORIES[selected]
if filter_source:
    filtered = [a for a in articles if a["source"] == filter_source]
else:
    filtered = articles

for article in filtered:
    sentiment = analyze_sentiment(article["title"])

    if sentiment == "ポジティブ":
        sentiment_color = "🟢"
    elif sentiment == "ネガティブ":
        sentiment_color = "🔴"
    else:
        sentiment_color = "🟡"
    
    with st.container(border=True):
        st.markdown(f"**[{article['source']}]** {article['title']}")
        st.caption(f"{sentiment_color} センチメント: {sentiment} | {article['published']}")
        if article["summary"]:
            with st.expander("概要を見る"):
                st.write(article["summary"])
        st.markdown(f"[元記事を読む →]({article['link']})")

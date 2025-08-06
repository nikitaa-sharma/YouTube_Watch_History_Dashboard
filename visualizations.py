import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# ✅ Top 10 Watched Channels
def top_channels_chart(df):
    top = df['channel'].value_counts().head(10).reset_index()
    top.columns = ['channel', 'count']
    fig = px.bar(
        top,
        x='channel',
        y='count',
        labels={'channel': 'Channel', 'count': 'Watch Count'},
        title='Top 10 Watched YouTube Channels'
    )
    return fig


# ✅ Watch Activity by Hour
def activity_by_hour(df):
    fig = px.histogram(
        df,
        x='hour',
        nbins=24,
        labels={'hour': 'Hour of Day'},
        title='Watch Activity by Hour'
    )
    return fig


# ✅ Watch Activity by Day of the Week
def day_of_week_chart(df):
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fig = px.histogram(
        df,
        x='weekday',
        category_orders={'weekday': order},
        labels={'weekday': 'Day of Week'},
        title='Watch Activity by Day of Week'
    )
    return fig


# ✅ Word Cloud of Watched Titles (matplotlib-based)
def generate_wordcloud(df):
    text = ' '.join(df['video_title'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Render with matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.title("Word Cloud of Watched Titles", fontsize=16)
    
    return fig

from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

from wordcloud import WordCloud
import pandas as pd

import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def remove_stop_words(message):
    words = []
    for word in message.lower().split():
        if word not in stop_words and word not in string.punctuation:
            words.append(word)
    return " ".join(words)


def create_wordcloud(selected_user, df):
    # filter by user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # remove system & non-text messages
    temp = df.copy()
    temp = temp[temp['user'] != 'group_notification']
    temp = temp[~temp['message'].isin(['<Media omitted>', 'This message was deleted'])]
    temp = temp[temp['message'].notna()]  # drop NaN just in case

    # if no text messages left, return None
    if temp.empty:
        return None

    # ensure message column is string before processing
    temp['message'] = temp['message'].astype(str).apply(remove_stop_words)

    # join all text safely as string
    text = temp['message'].astype(str).str.cat(sep=" ")

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(text)
    return df_wc


from collections import Counter
import pandas as pd

def most_common_words(selected_user, df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    temp = df.copy()
    temp = temp[temp["user"] != "group_notification"]
    temp = temp[~temp["message"].isin(["<Media omitted>", "This message was deleted"])]
    temp = temp[temp["message"].notna()]

    words = []
    for message in temp["message"].astype(str):
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    if not words:
        # return truly empty df
        return pd.DataFrame()

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    # columns will be: 0 = word, 1 = count (matches your current plotting code)
    return most_common_df


from collections import Counter
import pandas as pd
import emoji

def emoji_helper(selected_user, df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    temp = df.copy()
    temp = temp[temp["message"].notna()]  # drop NaN

    emojis = []
    for message in temp["message"].astype(str):
        for char in message:
            if emoji.is_emoji(char):
                emojis.append(char)

    if not emojis:
        # return empty DataFrame with the expected columns
        return pd.DataFrame(columns=[0, 1])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    # Columns: 0 = emoji, 1 = count (matches your plotting code)
    return emoji_df


def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    # If no rows after filtering, return empty DataFrame
    if df.empty:
        return pd.DataFrame()

    user_heatmap = df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0)

    return user_heatmap

















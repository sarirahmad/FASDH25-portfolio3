import pandas as pd
import plotly.express as px

# Load topic model data
df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio3/data/dataframes/topic-model/topic-model.csv")

# Convert to datetime
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' +
                            df['month'].astype(str).str.zfill(2) + '-' +
                            df['day'].astype(str).str.zfill(2))

# Filter: June–Nov 2023
df_filtered = df[(df['date'] >= '2023-06-01') & (df['date'] <= '2023-11-30')].copy()

# Combine keywords
df_filtered['Topic_Label'] = df_filtered['topic_1'] + ' | ' + \
                             df_filtered['topic_2'] + ' | ' + \
                             df_filtered['topic_3'] + ' | ' + \
                             df_filtered['topic_4']

# Define stopwords and generic words
useless_words = set([
    'the', 'to', 'of', 'and', 'in', 'on', 'at', 'for', 'with', 'is', 'are', 'was',
    'he', 'she', 'they', 'we', 'you', 'i', 'his', 'her', 'their',
    'call', 'say', 'said', 'get', 'go', 'come', 'be', 'has', 'have', 'had', 'do'
])

# Define a function to filter meaningful themes
def is_useful_theme(row):
    keywords = [row['topic_1'], row['topic_2'], row['topic_3'], row['topic_4']]
    for word in keywords:
        if word.lower() not in useless_words and len(word) > 3:
            return True
    return False

# Apply the filter
df_filtered = df_filtered[df_filtered.apply(is_useful_theme, axis=1)]

# Group by month and topic
df_filtered['month'] = df_filtered['date'].dt.strftime('%Y-%m')
topic_counts = df_filtered.groupby(['month', 'Topic_Label']).size().reset_index(name='Number of Articles')

# Plot with visible/thicker bars
fig = px.bar(topic_counts,
             x='month',
             y='Number of Articles',
             color='Topic_Label',
             title='Cleaned Themes of Articles (June–Nov 2023)',
             labels={'month': 'Month', 'Topic_Label': 'Theme (Top Keywords)'},
             barmode='group',
             height=600)

fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Number of Articles',
    legend_title='Article Theme',
    plot_bgcolor='rgba(250,250,250,1)',
    paper_bgcolor='rgba(255,255,255,1)',
    font=dict(size=12),
    xaxis_tickangle=-45,
    bargap=0.1,            # smaller gap = thicker bars
    bargroupgap=0.05       # reduce space between groups
)

fig.show()

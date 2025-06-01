import pandas as pd
import plotly.express as px

# Load TF-IDF pairwise similarity data
df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio3/data/dataframes/tfidf/tfidf-over-0.3-len100.csv")

# Create proper datetime columns
df['date_1'] = pd.to_datetime(df['year-1'].astype(str) + '-' +
                              df['month-1'].astype(str).str.zfill(2) + '-' +
                              df['day-1'].astype(str).str.zfill(2))
df['date_2'] = pd.to_datetime(df['year-2'].astype(str) + '-' +
                              df['month-2'].astype(str).str.zfill(2) + '-' +
                              df['day-2'].astype(str).str.zfill(2))

# NEW: average the two article dates and use that for grouping
df['avg_date'] = df[['date_1', 'date_2']].mean(axis=1)
df['month'] = df['avg_date'].dt.to_period('M').astype(str)  # formatted like "2023-10"

# Box plot: similarity score spread per month
fig1 = px.box(df, x='month', y='similarity',
              title='Distribution of Similarity Scores by Month',
              labels={'month': 'Month-Year', 'similarity': 'TF-IDF Similarity'})
fig1.update_layout(xaxis_title='Month', yaxis_title='TF-IDF Similarity')
fig1.show()

# Count how many comparisons happen per month
monthly_count = df.groupby('month').size().reset_index(name='article_pairs')

fig2 = px.bar(monthly_count, x='month', y='article_pairs',
              title='Number of Article Pairs per Month',
              labels={'month': 'Month-Year', 'article_pairs': 'Number of Article Pairs'})
fig2.show()

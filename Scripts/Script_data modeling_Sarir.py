#importing libraries
import pandas as pd
import plotly.express as px

# Loading topic model data from the path
df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio3/data/dataframes/topic-model/topic-model.csv")

#Converting into datetime: Help taken from _____________________
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' +
                            df['month'].astype(str).str.zfill(2) + '-' +
                            df['day'].astype(str).str.zfill(2))

#Filtering the data for June 2023 to January 2024, becasue i want to explore this part
df_filtered = df[(df['date'] >= '2023-06-01') & (df['date'] <= '2024-01-31')].copy()

#Saving the filtered data to see if I got it right or not
df_filtered.to_csv("Outputs/filtered_topic_data_Jun2023-Jan2024.csv", index=False)

#After manually examining the topic themes I saw some were useless therefore, listing topic numbers to remove
topics_to_remove = [-1, 2, 9, 26, 27, 40, 43, 52, 55, 62, 67, 79]

#filtering out rows with those topics and remove the entire row: Help taken from Chat GPT - Solution 1
df_filtered_cleaned = df_filtered[~df_filtered['Topic'].isin(topics_to_remove)].copy()

#I have to combine keywords with a pipe in between so that they will apear in the side of the graph
df_filtered_cleaned['Topic_Label'] = df_filtered['topic_1'] + ' | ' + \
                             df_filtered['topic_2'] + ' | ' + \
                             df_filtered['topic_3'] + ' | ' + \
                             df_filtered['topic_4']

#Converting separate year, month, and day columns into a single datetime column
df_filtered_cleaned['date'] = pd.to_datetime(df_filtered_cleaned[['year', 'month', 'day']])

#Now creating a new column that represents the year and month together (e.g., "2023-6")
#this is useful for grouping articles by month in visualisations
df_filtered_cleaned['month'] = df_filtered_cleaned['date'].dt.year.astype(str) + '-' + df['date'].dt.month.astype(str)

#Grouping it by month and topic, and count number of articles in each group: Help taken from Mam Amna
topic_counts = df_filtered_cleaned.groupby(['month', 'Topic_Label']).size().reset_index(name='Number of Articles')

#Plotting a bar graph with full colors to make it more easy to study.
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
    bargap=0.1,            # I set this because the bars were very thin
    bargroupgap=0.05       #I also reduced the space between the bars to make look them thicker, using Chat GPT
)

fig.write_html("Outputs/Bar graph_Topic modeling_Sarir.html")

import pandas as pd
import plotly.express as px
import nltk #I asked Chatgpt to help me understand how can I remove the extra words from my topics and he referred to this library.
from nltk.corpus import stopwords

# Downloading NLTK stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

df = pd.read_csv("../data/dataframes/topic-model/topic-model.csv") # I Loaded the CSV file
print(df["Topic"].value_counts().sort_index())

# Removing unclassified rows for making my data clean and coherent. 
df = df[df["Topic"] != -1]

#After manually examining the topic themes I saw some were irrelevant, therefore, listing topic numbers to remove
topics_to_remove = [2, 9, 26, 38, 40, 43, 45, 49, 52, 55, 63, 67, 79]
#filtering out rows with those topics and remove the entire row: Help taken from Chat GPT - Solution 1
df = df[~df['Topic'].isin(topics_to_remove)].copy()

# Creating a datetime column for feasibilty with the data handeling
df['date'] = pd.to_datetime({
    'year':df['year'],
    'month':df['month'],
    'day':1}
                            )
# Filtering for Oct–Dec 2023 because it is the only part I am currently interested in
df_filtered = df[(df['date'] >= '2023-10') & (df['date'] <= '2023-12')].copy()
# Creating 'Month' column directly as a datetime with the first day of each month (in this way, it becomes clean for plotting)
df_filtered["Month"] = df_filtered["date"].dt.to_period("M").dt.to_timestamp()


# Cleaning the topic keywords
def clean_keywords(row):
    words = []
    for col in ["topic_1", "topic_2", "topic_3", "topic_4"]:
        for word in str(row[col]).split():
            word_clean = word.lower().strip(",.")
            if word_clean not in stop_words:
                words.append(word_clean)
    return ", ".join(words)

df_filtered["Topic_Label"] = df_filtered.apply(clean_keywords, axis=1)

# Grouping by topic and month for order (specially cronological order).
grouped = df_filtered.groupby(["Topic_Label", "Month"]).size().reset_index(name="Article_Count")
# Sorting by date for visual order so that I get a cronologially well orderd output
grouped = grouped.sort_values("Month")

# Saving the filtered data as CSV for further analysis
df_filtered.to_csv("../Scripts/Outputs/Filtered_Topics_Oct-Dec2023.csv", index=False)

# Ploting all topics across months to know the main topics being discussed
fig = px.bar(
    grouped,
    x="Month",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    labels={"Month": "Month", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
    title="Topic trends (Oct–Dec 2023)"
)
month_ticks = pd.date_range(start="2023-10-01", end="2023-12-01", freq="MS")

fig.update_layout(
    xaxis=dict(
        tickmode="array",
        tickvals=month_ticks,
        tickformat="%b %Y",  # for instance if I want the year 2023
        tickangle=-45
    )
)

fig.show()
# Saving output in the output folder  
fig.write_html("../Scripts/Outputs/BarGraph-Topic modeling-Naveera.html")

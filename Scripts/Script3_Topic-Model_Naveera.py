import pandas as pd
import plotly.express as px

import nltk #I asked Chatgpt to help me understand how can I remove the extra words from my topics and he referred to this library, so I Used it to remove some basic english words.
from nltk.corpus import stopwords

# Downloading stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

df = pd.read_csv("../data/dataframes/topic-model/topic-model.csv") # I Loaded the CSV file
print(df["Topic"].value_counts().sort_index())

# Removing unclassified rows for cleaner data
df = df[df["Topic"] != -1]

# Creating a datetime column for my own feasibilty 
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

# Filter for Oct–Dec 2023, since this time period has remained of interest to me
df = df[(df["date"].dt.year == 2023) & (df["date"].dt.month >= 10) & (df["date"].dt.month <= 12)]

# Save the filtered data as CSV (for further analysing the data and using it for removing the unwanted or not so important articles)
df.to_csv("../Scripts/Outputs/Filtered_Topics_Oct-Dec2023.csv", index=False)

#After manually examining the CSV file I saw some were useless therefore, listing topic numbers to remove
topics_to_remove = [2, 9, 26, 38, 40, 43, 45, 49, 52, 55, 63, 67, 79]

#filtering out rows with those topics and remove the entire row: Help taken from Chat GPT -
df = df[~df['Topic'].isin(topics_to_remove)].copy()
# Clean topic keywords
def clean_keywords(row):
    words = []
    for col in ["topic_1", "topic_2", "topic_3", "topic_4"]:
        for word in str(row[col]).split():
            word_clean = word.lower().strip(",.")
            if word_clean not in stop_words:
                words.append(word_clean)
    return ", ".join(words)

df["Topic_Label"] = df.apply(clean_keywords, axis=1)

# Creating 'Month' column directly as a datetime with the first day of each month (clean for plotting)
df["Month"] = df["date"].dt.to_period("M").dt.to_timestamp()

# Grouping by topic and month for easy visualization through graph
grouped = df.groupby(["Topic_Label", "Month"]).size().reset_index(name="Article_Count")

# Sorting by date for visual order
grouped = grouped.sort_values("Month")


# Ploting all topics across months
fig = px.bar(
    grouped,
    x="Month",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    labels={"Month": "Month", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
    title="Topics (Oct–Dec 2023) - Stopwords Removed"
)

fig.update_layout(xaxis_tickformat="%b %Y")  # e.g., Oct 2023

fig.show()

# Saving output to our output folder. 
fig.write_html("../Scripts/Outputs/Bar Graph-topic modeling- Naveera.html")

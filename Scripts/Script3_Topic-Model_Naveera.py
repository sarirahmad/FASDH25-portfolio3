import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load the CSV
df = pd.read_csv("../data/dataframes/topic-model/topic-model.csv")

# Remove unclassified rows
df = df[df["Topic"] != -1]

# Create a datetime column
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

# Filter for Oct–Dec 2023
df = df[(df["date"].dt.year == 2023) & (df["date"].dt.month >= 10) & (df["date"].dt.month <= 12)]

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

# Create 'Month' column (e.g., '2023-10')
df["Month"] = df["date"].dt.to_period("M").astype(str)

# Group by topic and month
grouped = df.groupby(["Topic_Label", "Month"]).size().reset_index(name="Article_Count")

# Sort by date for visual order
grouped["Month"] = pd.to_datetime(grouped["Month"])
grouped = grouped.sort_values("Month")

# Plot all topics across months
fig = px.bar(
    grouped,
    x="Month",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    labels={"Month": "Month", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
    title= "Topics (Oct–Dec 2023) - Stopwords Removed"
)

fig.update_layout(xaxis_tickformat="%b %Y")  # e.g., Oct 2023

fig.show()

# Save output
fig.write_html("../Scripts/Outputs/BarGraph-topic modeling- Naveera.html")

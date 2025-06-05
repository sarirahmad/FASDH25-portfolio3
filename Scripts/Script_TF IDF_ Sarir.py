#Importing libraries
import pandas as pd
import plotly.express as px

#Loading your TF-IDF file with len100 from the path
df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio3/data/dataframes/tfidf/tfidf-over-0.3-len100.csv")
print(df.head()) #to see the column names / headings of the datasheet. 

#Creating a full date from 'year-1', 'month-1', and 'day-1' for article 1. Meanwhile renaming the column names to make it easier for pandas to undrerstand: Help taken from Chat GPT - Solution 1
df['date_1'] = pd.to_datetime(
    df[['year-1', 'month-1', 'day-1']].rename(columns={'year-1': 'year', 'month-1': 'month', 'day-1': 'day'})
)

#creating a full date from 'year-2', 'month-2', and 'day-2' for article 2: from the above step
df['date_2'] = pd.to_datetime(
    df[['year-2', 'month-2', 'day-2']].rename(columns={'year-2': 'year', 'month-2': 'month', 'day-2': 'day'})
)
#extracting 'YYYY-MM' format for use in grouping and visualization:
df['month_1'] = df['date_1'].dt.strftime('%Y-%m')
df['month_2'] = df['date_2'].dt.strftime('%Y-%m')


#to see the months
print("Unique values in month_1:", df['month_1'].unique())
print("Unique values in month_2:", df['month_2'].unique())

#making a  histogram to explore the number of articles and similarity.
fig1 = px.histogram(
    df,
    x='similarity',
    nbins=40,
    title='Figure 2: Distribution of Article Pair Similarities',
    labels={'similarity': 'TF-IDF Similarity Score', 'count': 'Number of Article Pairs'},
    color_discrete_sequence=['darkblue']  #optional color
)

#Grouping by both months and calculate average similarity: Help taken from Chat GPT - Solution 2
heatmap_data = df.groupby(['month_1', 'month_2'])['similarity'].mean().reset_index()

#converting it in a matrix kind of form that will help me use both the articles using Pivot function and then analyze the similarity: Help Taken from Chat GPT - Solution 3
heatmap_matrix = heatmap_data.pivot(index='month_1', columns='month_2', values='similarity')

#Creating the heatmap
fig2 = px.imshow(
    heatmap_matrix,
    labels={"x": "Month of Article 2", "y": "Month of Article 1", "color": "Avg Similarity"},
    title="Heatmap of Average TF-IDF Similarity Between Article Months"
)

#after plotting it i saw that the size was too small and not vissible therefore, i am applying some extra layout.
fig2.update_layout(width=800, height=700)
fig1.write_html("Outputs/Histogram_TFIDF_Sarir.html")
fig2.write_html("Outputs/Heatmap_TFIDF_Sarir.html")
print("The Outputs are saved in the folder successfully")


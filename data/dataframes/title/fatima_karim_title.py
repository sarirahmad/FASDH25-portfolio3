#import necessary libraries 
import pandas as pd
import plotly.express as px
from collections import Counter
import re

#loading the csv file
df = pd.read_csv("C:/Users/DELL/Downloads/FASDH25-portfolio3/data/dataframes/title/title.csv")

#Creating a 'month' column to simplify grouping (from chatgpt) 
df['month'] = df['year'].astype(str) + "-" + df['month'].astype(str).str.zfill(2)

#Counting the number of words in each title
df['title_word_count'] = df['title'].str.split().apply(len)

#Number of articles per month
monthly_counts = df['month'].value_counts().sort_index()

fig1 = px.bar(x=monthly_counts.index, y=monthly_counts.values,
              labels={'x': 'Month', 'y': 'Article Count'},
              title='Number of Articles per Month')
fig1.update_traces(marker_color='lightgreen')
fig1.show()
fig1.write_html("C:/Users/DELL/Downloads/FASDH25-portfolio3/Scripts/Outputs/Bar_Title_Fatima.html")

#Exploring the Average title word count per month
avg_title_length = df.groupby('month')['title_word_count'].mean().reset_index()

fig2 = px.line(avg_title_length, x='month', y='title_word_count',
               title='Average Title Word Count Per Month',
               labels={'title_word_count': 'Average Title Word Count'})
fig2.show()
fig2.write_html("C:/Users/DELL/Downloads/FASDH25-portfolio3/Scripts/Outputs/Line_Title_Fatima.html")

#Top 15 most common words in titles (took help from chatgpt to write the following code) 
#Combining all titles into one string (drop missing titles, make lowercase) 
all_text = " ".join(df['title'].dropna()).lower()
#Use regex to extract words with 4+ letters only
words = re.findall(r'\b[a-z]{4,}\b', all_text)
#Count the top 15 most common words
word_counts = Counter(words).most_common(15)
#Creating a DataFrame for plotting
word_df = pd.DataFrame(word_counts, columns=['word', 'count'])
fig3 = px.bar(word_df, x='word', y='count',
              title='Top 15 Most Common Words in Titles',
              labels={'word': 'Word', 'count': 'Frequency'})
fig3.show()
fig3.write_html("C:/Users/DELL/Downloads/FASDH25-portfolio3/Scripts/Outputs/Bar_Title_Fatima.html")                      

#Relationship between title and article length
fig4 = px.scatter(df, x='title_word_count', y='length',
                  title='Title Length vs. Article Length',
                  labels={'title_word_count': 'Title Word Count', 'length': 'Article Length'})
fig4.show()
fig4.write_html("C:/Users/DELL/Downloads/FASDH25-portfolio3/Scripts/Outputs/Scatter_Title_Fatima.html")



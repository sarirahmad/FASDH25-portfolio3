# importing necessary Libraries
import os
import plotly.express as px

# Setting the folder path for using articles folder to know about the frequency of articles publsihed in 2023.
folder_path = r'C:\Users\HP\Downloads\FASDH25-portfolio3\data\articles'

# making a dictionary to count files per month, so that the comparison can be seen.
article_counts = {
    '01': 0, '02': 0, '03': 0, '04': 0,
    '05': 0, '06': 0, '07': 0, '08': 0,
    '09': 0, '10': 0, '11': 0, '12': 0
}

# Looping through all files to count the number of articles published each individual month. 
for filename in os.listdir(folder_path):
    if '2023' in filename:
        for month in article_counts:
            if f'2023-{month}' in filename or f'2023_{month}' in filename:
                article_counts[month] += 1

# Converting the data recieved to list form for plotting
months = list(article_counts.keys())
counts = list(article_counts.values())

# Create=ing a bar chart for easy visualization
fig = px.bar(x=months, y=counts,
             labels={'x': 'Month (2023)', 'y': 'Number of Articles'},
             title='Article Count Per Month in 2023')

fig.update_layout(template='plotly_white') # again took help from the perviously learned method from AI. 

# Save the chart for further analysis. 
output_path = r'C:\Users\HP\Downloads\FASDH25-portfolio3\Scripts\Outputs\Bargraph-ArticleFrequency-Naveera.html'
fig.write_html(output_path)
print(f"Plot saved to: {output_path}")

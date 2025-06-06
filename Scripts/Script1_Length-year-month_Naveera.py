import os
import pandas as pd
import plotly.express as px

# Set working directory
new_dir = r'C:\Users\HP\Downloads\FASDH25-portfolio3\data\dataframes\length'
os.chdir(new_dir)
print("New working directory:", os.getcwd())

# Load and clean data
df = pd.read_csv('length-year-month.csv')
df['year'] = df['year'].astype(int)
df['month'] = df['month'].astype(int)
df = df.sort_values(by=['year', 'month']).reset_index(drop=True)

# Filter data from 2021 to 2023
filtered_df = df[(df['year'] >= 2021) & (df['year'] <= 2023)]
filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month']].assign(day=1))

# Create plot
fig = px.line(filtered_df, x='date', y='length-mean', title='Average Article Length (2021–2023)',
              markers=True, labels={'length-mean': 'Length Mean', 'date': 'Date'})
fig.update_traces(line=dict(color='teal'))
fig.update_layout(xaxis_title='Date', yaxis_title='Average Article Length', template='plotly_white') # from chatgpt to understand how the polotting is shown.

# Save the figure
output_path = r'C:\Users\HP\Downloads\FASDH25-portfolio3\Scripts\Outputs\Bar graph-length-year-month_Naveera.html'
fig.write_html(output_path)
print(f"Plot saved to: {output_path}")

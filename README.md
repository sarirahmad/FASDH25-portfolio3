# Mini Project 3

This project analyzes thematic similarity and content patterns in a collection of news articles using TF-IDF, article frequency, and text length data. By calculating TF-IDF similarity scores between article pairs, we track how closely articles align in content over time. Visualizations such as histograms and heatmaps highlight trends in similarity across months. We also examine the number and length of articles published each month to explore how content volume may influence thematic overlap. Finally, topic modeling is applied to identify dominant themes during periods of high similarity, offering deeper insight into recurring narratives and shifts in focus within the corpus.

## Folder Structure

FASDH25-portfolio3/
│
├── data/
│   └── dataframes/
│       └── tfidf/
│           ├── tfidf-over-0.3.csv
│           ├── tfidf-over-0.3-len100.csv
│           └── tfidf-over-0.3-len200.csv
│
├── Outputs/
│   ├── Histogram_TFIDF_Sarir.html
│   ├── Heatmap_TFIDF_Sarir.html
│   ├── Filtered_Topics_BarGraph.html
│   └── [Any additional saved figures or exports]
│
├── Scripts/
│   ├── Script_TFIDF_Sarir.py
│   ├── Script_TopicModeling_Sarir.py
│   └── [Other scripts by team members]
│
├── AI Documentation/
│   └── README.md (or AI summary/instructions)
│
├── Report/
│   └── Project_Report.docx (Final Turnitin Submission)
│
└── README.md (Project overview, setup instructions, and folder structure)


---------------------------------------------

## Analyzing Similarity and Themes in Articles using TF-IDF and Topic Modeling (Sarir)

### Overview:

This part focuses on the  similarity of articles using TF-IDF, tracking article counts and high similarity over specific time period, and analyzing thematic trends through topic modeling. The goal is to understand when and why articles become more aligned in content.

### Objectives

* Exploring TF-IDF similarity scores between article pairs.

* Tracking highest similarity of articles and counts of articles.

* Finding the similarity of articles from 0.7 - 0.85 and finding dates and time accordingly.

* Apply topic modeling to uncover dominant themes during peaks in similarity.

### Tools and Libraries

* Python
* pandas, plotly, datetime

### Output:
1. A histogram of similarity and counts of articles.
2. heatmap of similarity and specific time (month and year)
3. Bar graph to see the themes of articles in the specific time framw. 


------------------------------------------------------------------------

## Using Length and Topic Modeling (Naveera)

### Overview:
This part of the project is concerened with finding the trends in Length (Mean Length specifically), Frequency (though analysing titles) and Topic Modleing to contextualize the change in all these dataset with time and intensity of war situation in Gaza. The aim was to find a trend that would justify our argument that Global Conflict etc significantly effects the lenght, frequency and topics of news to be disseminated. I observed a unique declining trend in the mean-length, while a uprising trend in the frequency of articles. This, in context of Gaza can be analysed as: since the war condition got worse by the end of 2023, there became a need of more fragmented information flow, rather than packed articles. Through the Topic modeling, this this was confimed that topics like patient, hospital, attacks and aids like topics were more in those short articles. 


### Environment Setup
 
* Python
* pandas, plotly, datetime, 
* NLTK stopwords


### Corpus and Filtering

* Aljazera Articles 
* Mean length of articles in 2023, Titles (for frequency during Oct-Dec2023), Topic Models (Oct-Dec2023). 

### Output (example):
* I made visualizations through Bar graphs for:
1. Mean length
2. Frequency
3. Topic Models
That supported my argument.

-----------------------------------------------------

## 3: (Fatima)

### Overview:
This section analyzed article titles to explore patterns in media coverage over time. I tracked changes in publishing frequency, headline length, and common words, revealing how titles reflect media focus. While the analysis showed useful trends, it didn’t capture tone or deeper context.

### Input Data
CSV file: "title.csv"
Contains the following relevant columns:
    - 'title': the title of each article
    - 'year': year of publication
    - 'month': month of publication
    - 'day' : day of publication 
    - 'length': full article length (word count)

### Tools and Functions
* Python 
* Pandas (for data loading and manipulation) 
* Plotly.express (for interactive visualizations) 
* Re (for regular expression-based word extraction)
* Collections.Counter (for word frequency counting) 

### Process Summary
1. Load the data:using `pandas` from the specified CSV file.
2. Create a 'month' column: for easier grouping by combining year and month.
3. Calculate article count per month: and visualize it as a bar chart.
4. Compute average title word count: by month and plot it as a line chart.
5. Extract common title words: using regular expressions and plot top 15 as a bar chart.
6. Visualize relationship: between title length and full article length using a scatter plot.
7. Save all plots: as interactive HTML files inside the `Scripts/Outputs/` folder.

### Output (structure):
1. A fluctuating but generally high volume of articles over time, with notable peaks in certain years(2023).
2. Variations in title length, possibly reflecting shifts in reporting style.
3. The dominance of conflict-related terminology in titles, suggesting a focus on specific geopolitical events.
4. A weak correlation between title length and article length, indicating that longer titles do not necessarily correspond to longer articles.
--------------------------------

The End...


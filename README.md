# Individual_Project_1
[![Install](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Data_Engineering_Individual_Project1/actions/workflows/lint.yml)

This is the README for my Individual Project 1 for the IDS706 - Data Engineering Systems class at Duke University.

## Dataset
The dataset comes from Kaggle, a public machine learning and data science community. It contains a CSV file of detailed information regarding the most-streamed Spotify songs in 2023. Link: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data

## Data Visualization
For the visualization, I analyzed and visualized the 10 hottest artists by their stream counts using [Pandas](pandas.pydata.org)

![alt text](top_10_artist_by_stream_count.png)

## Summary Statistics
Here is a glimpse into the summary statistics for certain columns from the dataset by running `dataframe.describe()`:

![alt text](summary_statistics.png)

## Extra Credit
If you examine the [one of the latest commits by myself](https://github.com/nogibjj/Peter_Min_Data_Engineering_Project3/actions/runs/10977799956/job/30480175871) in GitHub, you will see that both the HTML descriptive data analytics file from the `ProfileReport` and the markdown descriptive statistics file are built automatically at each push from the CI/CD pipeline. PDF file format is not supported by this package so HTML has to be used here.

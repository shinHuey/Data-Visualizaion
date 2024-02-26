# COVID-19 Impact on Students Dashboard
This dashboard visualizes the impact of COVID-19 on students using data from the COVID-19 Survey Student Responses dataset, which can be found https://www.kaggle.com/datasets/kunal28chaturvedi/covid19-and-its-impact-on-students.

## Code
The code for this dashboard is written in Python and uses the following libraries:

- pandas: for data manipulation and analysis
- matplotlib: for creating static plots
- plotly: for creating interactive plots
- dash: for creating the web-based dashboard

The code begins by loading the dataset into a pandas dataframe and performing some data pre-processing, such as handling missing values, converting data types, and cleaning up categorical variables.

The layout of the dashboard is defined using HTML and Dash components. The dashboard includes the following visualizations:

1. Distribution of Students by Region of Residence: Pie chart showing the proportion of students in each region of residence.
2. Age-wise Distribution of Students: Bar chart showing the count of students in each age group.
3. Medium Used for Online Classes: Pie chart showing the proportion of students using different mediums for online classes.
4. Time Spent on Various Activities: Box plots showing the distribution of time spent by students on various activities such as online classes, self-study, fitness, sleep, social media, and TV.
5. Preferred Social Media Platform: Bar chart showing the count of students using different social media platforms.
6. Favourite Stress Buster: This visualization uses a pie chart to display the distribution of different stress busters chosen by survey respondents.
7. What did they miss the most?: This visualization uses a bar chart to show the items missed the most during the lockdown. 
8. Health Impacted by Various Factors (YES): This visualization uses a box plot to display the impact of various activities on health during the lockdown, for respondents who reported health issues (Health issue during lockdown = YES). Multiple box plots are used to show the distribution of time spent on online classes, TV, social media, fitness, self-study, and sleep. 
9. Health Impacted by Various Factors (NO): This visualization is similar to the previous one, but it shows the impact of various activities on health for respondents who did not report any health issues during the lockdown (Health issue during lockdown = NO). 

The visualizations are created using plotly and matplotlib, and the interactive plots are displayed in the Dash app.

## How to Run the Dashboard
1. Make sure you have Python and the required libraries installed (pandas, matplotlib, plotly, dash).
2. Download the dataset from here and save it as "COVID-19 Survey Student Responses.csv" in the same directory as the code.
3. Run the code in a Python environment or IDE.
4. Open a web browser and go to the URL "http://127.0.0.1:8050/" to access the dashboard.

## Known Issues
1. Word overlap on x-axis labels: Due to the length of some x-axis labels, there may be issues with the overlapping of words on the x-axis labels of some visualizations. This can be resolved by increasing the size of the plot or by rotating the x-axis labels to make them more readable.
2. Data filtering: The code filters out low correlation data based on a threshold of 0.3, which may not be suitable for all datasets. It is recommended to review and adjust this threshold based on the specific dataset being used.



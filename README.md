# Beers Across the Atlantic: Decoding Beer Preferences in North America and Europe

## Abstract
The North American and European markets are of great significance to the global beer industry. They influence the trends that are followed by the industry. Thus, we are curious to discover the differences between their customers’ preferences and the reason behind them.

We are primarily interested in establishing whether there is a significant disparity in preference for beers with high alcohol by volume (ABV) between North Americans and Europeans, and if this preference is linked to certain types of beers. Indeed we suspect that some of the cultural dissimilarities of these two groups might lead to different inclinations when it comes to alcohol concentration in beers.

To verify this, different methods will be used such as regression analysis to investigate correlations between beer ratings and their features, and notably ABV. In order to develop an interesting narrative that demonstrates the evolution of alcohol content preference, we will have to use some time-series analysis. Moreover, we will also try to map American states to European countries based on similar beers’ ABV likings that we will have uncovered.

This research could provide insightful information for product development and marketing strategies in the beer sector, especially for brands wanting to conquer both continents.

## Research Questions
### Main question:
**Do Americans prefer beers with a higher alcohol content (ABV) than Europeans?**<\br>
This investigation explores  into whether N. Americans favor higher alcohol content beers compared to Europeans. In order to investigate this question, we will analyse ratings from both datasets, grouping users based on their location.
### Subquestions:
1. Is there a correlation between this preference and specific beer styles known for higher ABV?
We will use grouping techniques and micro/macro averages to analyse this preference. <\br>
2. How have beer preferences, especially in terms of ABV, evolved in America and Europe between 2000 and 2017?
To analyse this question, we will use time series analysis and visualisation techniques. <\br>
3. Is it possible to map American states to European countries based on similarities in beer preferences?
How can graph and network algorithms be utilized to explore these geographical correlations? <\br>

## Datasets
**BeerAdvocate** and **RateBeers**

## Methods
The analysis focuses on comparing the preferences for beer ABV (Alcohol By Volume) between North American and European users. It particularly investigates whether Americans have a preference for higher ABV beers compared to Europeans.
The study examines how these preferences have changed from 2000 to 2017.
Beer ratings are analysed in relation to ABV. The investigation includes looking at how different beer styles are rated in North America versus Europe.
The analysis includes examining average ratings and ABV trends over time, comparing review frequencies, and analysing the impact of seasonality and regional variations on beer ABV and ratings.

**Our methodology includes:**
- **Data preprocessing**</br>
**Data Filtering:** Not all features will be useful, therefore, we will filter the data to remove irrelevant or redundant information</br>
First, the data is divided into two main geographical regions: North America and Europe. In detail, European countries are named and users are placed depending on their localities.
The dataset becomes properly conditioned for analysis purposes. This requires links between individual user information and his or her respective beer ratings.
Beer styles are grouped into broader categories to make them more manageable. 
We also discretized the ABV to have a discrete and manageable number of categories of ABV from which we can extract meaningful information.


- **Time Series Analysis**</br>
We will employ time series analysis to explore how beer preferences, particularly in terms of ABV, have evolved from 2000 to 2017. This method will help us identify the trends, seasonal patterns, and the changes over time.

- **Correlation Analysis**</br>
We will estimate the extent by which beer ratings correlate with ABV through correlation analysis by calculating the correlation coefficients which will show whether the relationship between these variables is strong/weak and positive/negative.

- **Regression Analysis**</br>
We will apply regression models that will provide insight on how various factors affect the rating of a given type. We may use Multiple regression analysis in this case whereby such predictors as alcohol percentage volume (ABV), other types mixed with other participants’ characteristics can be included.

- **Data Visualization**</br>
We will create charts and graphs to help users and breweries visualize beer prefrences, and trends among parameters.
Various data visualisations are planned, likely using seaborn, a Python visualization library. These visualisations are intended to provide clear insights into ABV values, ratings, and other relevant factors across the two regions.
Leverage seaborn and other visualisation tools to create more complex and informative visualisations. This could include interactive plots or dashboards that allow for dynamic exploration of the data.
Consider visualising the data geographically to highlight regional differences in beer preferences across North America and Europe.
Make a geomap plot: Interconnect NA states with EU contries based on their the most desired beer style.

## Proposed timeline
- 17.11.23 **Milestone 2** deadline.
- 24.11.23 A break from the Project Work. Wrok on **Homework 2**.
- 01.12.23 Deadline for **Homework 2**. Complete and submit homework 2.
- 08.12.23 Begin Drafting Data Story. Start developing a rough draft of the data story, incorporating insights and visualizations from the analysis.
- 09.12.23 Completion of Statistical Tests. Finalise all statistical tests required for the analysis.
- 11.12.23 Finalize Code Implementations and Visualizations. Complete all coding and data visualizations pertinent to the analysis.
- 15.12.23 Finalize Data Story. Complete the data story, ensuring it effectively communicates the findings of the analysis.
- 21.12.23 Finalise the project Development.
- 22.12.23 Deadline for **Milestone 3**.

## Organisation within the team
**Data Analysis Team:** Members 1 & 2</br>
Lead the data slicing, preprocessing, and exploratory analysis
Conduct statistical tests and interpret results.

**Data Story and Visualization Team:** Members 3, 4 & 5</br>
Develop the narrative for the data story, integrating analytical insights.
Design and create data visualizations and infographics.

**Code Implementation:** Collaborative Effort</br>
Coding aspects of the project such as: data analysis, visualization scripts, etc. are contributed by all team members.

**Analysis:** Group Discussion</br>
Discussing analyses at group meetings regularly; interpreting results; planning for next actions. Such discussions help establish a common understanding and approach to analysis.

**Regular Check-ins and Updates:**</br>
Plan weekly or bi-weekly meetings where everyone reports on what they have done so far, challenges faced during task completion, and whether they are still on track to complete their tasks.





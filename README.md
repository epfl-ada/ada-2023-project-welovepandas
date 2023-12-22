# Beers Across the Atlantic: Decoding Beer Preferences in North America and Europe

## Abstract
The North American and European markets are of great significance to the global beer industry. They influence the trends that are followed by the industry. Thus, we are curious to discover the differences between their customers’ preferences and the reason behind them.

We are primarily interested in establishing whether there is a significant disparity in preference for beers with high alcohol by volume (ABV) between North Americans and Europeans, and if this preference is linked to certain types of beers. Indeed we suspect that some of the cultural dissimilarities of these two groups might lead to different inclinations when it comes to alcohol concentration in beers.

To verify this, different methods will be used such as regression analysis to investigate correlations between beer ratings and their features, and notably ABV. In order to develop an interesting narrative that demonstrates the evolution of alcohol content preference, we will have to use some time-series analysis. Moreover, we will also try to map American states to European countries based on similar beers’ ABV likings that we will have uncovered.

This research could provide insightful information for product development and marketing strategies in the beer sector, especially for brands wanting to conquer both continents.

## Research Questions
### Main question:
**Do Americans prefer beers with a higher alcohol content (ABV) than Europeans?**</br>
This investigation explores  into whether N. Americans favor higher alcohol content beers compared to Europeans. In order to investigate this question, we will analyse ratings from both datasets, grouping users based on their location.
### Subquestions:
1. Is there a correlation between this preference and specific beer styles known for higher ABV?</br>
We will use grouping techniques and micro/macro averages to analyse this preference.
2. How have beer preferences, especially in terms of ABV, evolved in America and Europe between 2000 and 2017?</br>
To analyse this question, we will use time series analysis and visualisation techniques.

## Datasets
**BeerAdvocate** and **RateBeers**

## Methods
The analysis focuses on comparing the preferences for beer ABV (Alcohol By Volume) between North American and European users. It particularly investigates whether Americans have a preference for higher ABV beers compared to Europeans.
The study examines how these preferences have changed from 2000 to 2017.
Beer ratings are analysed in relation to ABV. The investigation includes looking at how different beer styles are rated in North America versus Europe.
The analysis includes examining average ratings and ABV trends over time, comparing review frequencies, and analysing the impact of seasonality and regional variations on beer ABV and ratings.

**Our methodology includes:**

**Part 1: Data Foundation and Preliminary Analysis**

- **Data preprocessing**</br>
Not all features will be useful, therefore, we will filter the data to remove irrelevant or redundant information</br>
First, the data is divided into two main geographical regions: North America and Europe. In detail, European countries are named and users are placed depending on their localities.
The dataset becomes properly conditioned for analysis purposes. This requires links between individual user information and his or her respective beer ratings.
Beer styles are grouped into broader categories to make them more manageable. 
We also discretized the ABV to have a discrete and manageable number of categories of ABV from which we can extract meaningful information.

- **Data Categorization and Grouping**</br>
This step involves organizing beers into categories based on their styles in order to facilitate a comparative analysis structure. 
While at the same time the data will be divided geographically, so as to analyze how each group (North America versus Europe) prefers their beers distinctly. 
Such categorization is necessary for comparing beer preferences across continents.  
We also discretized the ABV to have a discrete and manageable number of categories of ABV from which we can extract meaningful information.

**Part 2: In-Depth Data Analysis**
- **Analysis of Beer Style Preferences**</br>
Using the categorized data, we will examine the types of beer favored by people in North America as well as Europe more closely.
We seek not only to identify popular styles but also to understand what average ABV range characterizes these preferences in both cases.
Thus, this analysis intends to bring out main patterns of behaviors regarding the selection of brands.

- **Time Series Analysis of ABV Preferences**</br>
we will keep track of ABV preferences from 2000 – 2017. Through time series analysis we can identify trends as well as notable changes that have happened over some time thus understanding more about what happens when it comes to alcohol consumption among various individuals, the trends, seasonal patterns, and the changes over time.

**Part 3: Synthesis and Interpretation**

- **Statistical Analysis**</br>
In addition, we will carry out correlation analysis which looks into whether highly alcoholic beer styles have particular popularity within regions.
 We will examine the correlation between various features, such as ABV and ratings to see the dependancy between those parameters and validate our predictions.
This is done to give an insight on whether a preference for higher alcohol content by beer consumers could be associated with specific types of beers, thus on regional preferences for beer.


- **Data Visualization and Conclusion**</br>
We will create charts and graphs to help users and breweries visualize beer prefrences, and trends among parameters.</br>
Lastly, we will conduct a comprehensive analysis comparing the findings from North America and Europe.
By doing this we seek to highlight any significant differences in their preferences that would be useful.


## Proposed timeline
- 17.11.23 **Milestone 2** deadline.
- 24.11.23 A break from the Project Work. Work on HW2.
- 01.12.23 Deadline for HW2. Complete and submit HW2.
- 08.12.23 Begin Drafting Data Story. Start developing a rough draft of the data story, incorporating insights and visualizations from the analysis. 
- 15.12.23 Finalise all statistical tests required for the analysis. Finalize Code Implementations and Visualizations. Complete all coding and data visualizations pertinent to the analysis.
- 22.12.23 Finalise Data Story. Complete the data story, ensuring it effectively communicates the findings of the analysis. Finalise the project Development.

## Organisation within the team
**Data Preparation Team:** Members 1 & 2</br>
Lead the data filtering, preprocessing, and exploratory analysis.</br>
Conduct statistical tests and interpret results.

**Data Story and Visualization Team:** Members 3, 4 & 5</br>
Develop the narrative for the data story, integrating analytical insights.</br>
Design and create data visualizations and infographics.

**Code Implementation:** Collaborative Effort</br>
Coding aspects of the project such as: data analysis, visualization scripts, etc. are contributed by all team members.

**Analysis:** Group Discussion</br>
Discussing analyses at group meetings regularly; interpreting results; planning for next actions. Such discussions help establish a common understanding and approach to analysis.

**Regular Check-ins and Updates:**</br>
Plan meetings once/twice a week, when everyone reports on what they have done so far, challenges faced during task completion, and whether they are still on track to complete their tasks.

## Questions for TAs
As shown in the preliminary results in `p2_notebook.ipynb`, we notice that the BeerAdvocate dataset contains very few ratings by European users.
Moreover, we are always plotting the plots for BeerAdvocate and RateBeer side-by-side, which is not convenient. One solution to this would be to 
merge the two datasets, but the ratings are not always on the same scale and the American users from RateBeer would be mixed with a high number of BeerAdvocate users, and this would not be the case for European users.
For all these reasons, it seems to us that RateBeer is much more adapted to answer our reseach question.
The question is then: are we allowed to only use the RateBeer dataset in our case?



# 2020Fall_projects
# Final Project - IS 597PR
# Analyzing New York City Arrests, Complaints, and Stop, Question, Frisk Data

## Overview

NYC, commonly referred to as the 'Big Apple', is one of the most populous city in the United States of America. A high population indicates a larger economic unit comprising of multiple industries. However, it also indicates more number of crimes, and more number of complaints from civilians who are victims of these crimes. One of the key factors that determines a city's quality of life is the safety of the individuals. Keeping this in mind, we decided to perform some analysis on the data available about the same. We decided to come up with hypotheses centered around racial backgrounds, age and gender to determine if individuals with a certain background are subjected to prejudice. All of the data that we have worked on is public data and is made available by NYC Open Data (https://opendata.cityofnewyork.us/). Our analysis will be beneficial for those who wish to know more about the city of New York, individuals who wish to settle in the Big Apple, as well as relevant authorities who might see this analysis as a way to bring about positive change by identifying areas of improvement.

## Team Members
Shraddha Sutar - sutar2@illinois.edu</br>
Devwrat Tanwar - dtanwar2@illinois.edu

## Datasets used for Analysis
Stop, Question and Frisk Data - https://data.cityofnewyork.us/Public-Safety/The-Stop-Question-and-Frisk-Data/ftxv-d5ix </br>
NYPD Complaint Data Historic - https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i </br>
NYPD Arrest Data Historic - https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc </br>

Although these data sources comprise of records from over a decade, we have focused our analysis on records from the year 2019 i.e. incidents that occured in the 2019 (01/01/2019 - 12/31/2019). Instead of filtering the data after loading it in python, which would be computationally exhaustive, we filtered the data from NYC Open Data's website and downloaded appropriate versions of the files.

# Hypotheses

## Hypothesis 1 : A larger proportion of individuals who are arrested for the crime they commit are in the age group of 25 - 44

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp1_VC.PNG">
</p>

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp1_NormValues.png">
</p>

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp1_PropValues.png">
</p>

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp1_PropPie.png">
</p>


### Conclusion : The graphs generated indicate that a larger proportion of individuals who are arrested belong in the age group of 18 - 23. Hence our hypothesis does not stand true.

## Hypothesis 2 (A) : Males are more likely to be frisked than females (when stopped)

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp2_VC.PNG">
</p>

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp2_A_ProbFrisk.png">
</p>

### Conclusion : The graph indicates that a male stands a higher chance of being frisked than a female, when stopped. In this case, our hypothesis does stand true. 

## Hypothesis 2 (B) : Males are more likely to be arrested than females (when stopped)

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp2_A_ProbArrest.png">
</p>

### Conclusion : The graph indicates that a female stands a higher chance of being arrested than a male, when stopped. In this case, our hypothesis does not stand true.

## Hypothesis 3 (A) : Individuals of a particular race are more likely to be frisked than any other race

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp3_A_VC_Race.PNG">
</p>

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp3_B_Prob_Frisk.png">
</p>

### Conclusion : From the graph, it is tough to either confirm or deny our hypothesis since the probability of being frisked for the Black Hispanic race and (null)/UNKNOWN is the same. However, if the UNKNOWN race is neglected, we notice that the chances of you being frisked are higher if you are an individual who is Black Hispanic. 

## Hypothesis 3 (B) : Individuals of a particular race are more likely to be arrested than any other race

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp3_A_Prob_Arrest.png">
</p>

### Conclusion : From the graph, we can see that the probability of you being arrested is higher if you are an individual whose race is White. Had both, 3(A) and 3(B) revealed that a particular race has a higher probability of being arrested/frisked, we could have said that prejudice against a particular race is witnessed. However, when looking at both graphs holistically, we can say that individuals from one race are not targeted in particular. 

## Hypothesis 4 : Complaints for crimes are usually reported in the same week/month that they are committed in. 

<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp4_Week.png">
</p>


<p align="center">
  <img src="https://github.com/devwrattanwar24/2020Fall_projects/blob/main/Graphs/Hyp4_Month.png">
</p>

### Conclusion : From the graphs, we see that a majority of the crimes are reported within the first week / within the first month of the crime occuring. Hence, our hypothesis stands true.

## References :
https://worldpopulationreview.com/us-cities/new-york-city-ny-population </br>
https://github.com/rahulrohri/final_project_2020Sp </br>
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html </br>
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html </br>
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html </br>
https://www.statista.com/statistics/911456/new-york-population-share-age-group/ </br>
https://www-statista-com.proxy2.library.illinois.edu/statistics/911456/new-york-population-share-age-group/ </br>
https://github.com/python-visualization/folium/tree/master/examples </br>
https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_and_donut_labels.html </br>
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html </br>
https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/ </br>
https://gist.github.com/DavidWells/7d2e0e1bc78f4ac59a123ddf8b74932d


## Work Distribution :

Shraddha Sutar -> Hypothesis 2, 4; Functions + Doctests + Docstrings; Future Scope

Devwrat Tanwar -> Hypothesis 1, 3; Functions +  Doctests; README.md + Future Scope

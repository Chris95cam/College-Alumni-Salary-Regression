# College Alumni Salary Regression

## Summary
This repository contains the files for my college alumni salary regression project. In this project,
I examine Forbes Magazine's 2019 United States college rankings, and use machine learning to predict 
the median alumni salary for each school.

## Contents
 - [College Alumni Salary Regression.ipynb](https://github.com/Chris95cam/College-Alumni-Salary-Regression-Project/blob/master/College%20Alumni%20Salary%20Regression.ipynb): Python notebook containg the data processing, data exploration, and model building for this project.

- [ForbesAmericasTopColleges2019Original.csv](https://github.com/Chris95cam/College-Alumni-Salary-Regression-Project/blob/master/ForbesAmericasTopColleges2019Original.csv): Raw data set used for this project, collected using my custom webscraper. The data contains information for 650 top ranked United States colleges, according to Forbes Magazine.

- [locutility.py](https://github.com/Chris95cam/College-Alumni-Salary-Regression-Project/blob/master/locutility.py): A custom function I wrote that returns the latitudes and longitudes of the college locations in the data set. The function uses Geopy to fetch the information, which is then used for data exploration purposes. 

- [visutility.py](https://github.com/Chris95cam/College-Alumni-Salary-Regression-Project/blob/master/visutility.py): A custom function I wrote that creates a predicted vs. actual graph that is used to visualize the amount of error in the machine learning models. 

- [webscrapper.py](https://github.com/Chris95cam/College-Alumni-Salary-Regression-Project/blob/master/webscrapper.py): Webscraper I built using BeautifulSoup to extract the extract the needed information from forbes.com.

## Acknowledgements 
- [America's Top Colleges 2019](https://www.forbes.com/top-colleges/#6010771e1987) - Data source for the project
- [CoderzColumn: Cartopy - Basic Maps [Scatter Map, Bubble Map & Connection Map](https://coderzcolumn.com/tutorials/data-science/cartopy-basic-maps-scatter-map-bubble-map-and-connection-map) - Helped to create Cartopy map
- [Visualising Top Features in Linear SVM with Scikit Learn and Matplotlib](https://medium.com/@aneesha/visualising-top-features-in-linear-svm-with-scikit-learn-and-matplotlib-3454ab18a14d) - Used to create SVR feature importance chart
- [Filling the missing data using regression in python](http://www.statisticsandprobability.com/Statistics/filling_missing_data) - Helped with method I used to impute missing test scores

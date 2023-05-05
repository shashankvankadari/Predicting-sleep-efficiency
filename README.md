# DSCI441_Repository
# Created this repository for DSCI441 Final project submission:
This project aims to predict the efficiency of sleep which is defined as the ratio of time spent asleep to the total time spent in bed. We predict this by considering various factors in the dataset such asthe sleep timings, duration, and various habits of a person such as Caffeine intake, Smoking, and alcohol consumption etc. Also, each test subject’s age and gender are taken into consideration. We perform both classification and regression and compare them using various metrics to decide on the best performing model. The aim is to achieve fairness in the model without any bias. 

The project compares various classification and regression models and chooses the best performing model. In addition to that, we perform fairness evaluation on each model to make sure the model is not biased across various groups. After we decide on the best model, we develop an application to predict sleep efficiency using streamlit.

# Below I have provided an explanation about the code. Overall the code is divided into 8 sections. 
1) Importing the necessary libraries and data.
2) Exploratory Data Analysis
3) Data distribution for categorical attributes.
4) Linear Regression
5) Ridge Regression
6) Classification Model - Random Forest
7) XG-Boost classifier
8) Streamlit app

####  SECTION-1: Importing necessary libraries and data. ######
In this section, we import necessary libraries required for entire project. After that we import the csv data file and load it into pandas dataframe. 

#### SECTION-2: Exploratory Data Analysis. ######


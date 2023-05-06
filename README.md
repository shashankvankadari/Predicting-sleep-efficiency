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
In the first part, we format the variables in the proper manner. We convert the categorical variables such as "Gender", "Smoking Status" into numerical by replacing them with 0's and 1's. Also the attributes "Bedtime" and "Wakeup time" are converted to timestamp format. We then check for null values and the missing values are fileld with mean of that particular column. We didnot remove the rows with missing values just to avoid the information loss. 
We then check the correlations between the variables and do feature selection based on that. We have done this by plotting correlation heat map which describes the correlation values between all the variables. We then remove the features which has high correlation because both the variables contribute the same to the target variable and so it will be redundant. The variables "Wakeup time" and "Deep sleep percentage" are removed in this regard and now finally we have 12 features left in the dataset. 

####  SECTION-3: Checking data distribution for categorical attributes ######
In this section, we plan to check the data distribution for categorical attributes in order to consider a feature do to fairness evaluation. We did distribution graphs for Gender, Smoking status, Awakenings, Exercise frequency. We observe that distribution is good only for Gender column. All the other variables have uneven distributions. So we use this feature to calculate fairness as the bias is minimum for this column. (There is equal number of datapoints for both Male and Female).

#### SECTION-4: Linear Regression #####
We created a copy of the final dataframe which is cleaned. The intension is to use one for classification and regression model respectively.

In the next step, we perform linear regression with 5-fold cross validation and find the R2 score and Mean square error for each fold. We finally compute the average of MSE and R2 scores obtained in each fold. We got 79.7% of R2 score and 0.00036 for MSE. 

#### SECTION-5: Ridge Regression ####
We tried Ridge regression to improve the R2 Score by adding the penalty.  We added penalty values (alpha) of 0.1, 1, 10. We again did 5-fold cross validation and calculated R2 score and MSE. We observe that MSE and R2 score remain similar across all the values of penalty and is almost same like linear regression. 
We have choosen alpha = 10 as the optimul penalty value for linear regression and performed fairness evaluation. We calculated R2 score and MSE individually for male and female separately. The fairness results are almost similar which indicated that data is not biased and model is fair. 

##### SECTION-6: Classification model - Random Forest #######
For classification model, we converted the numerical target variable into categorical by dividing into 3 sections. (Best > Average > Worst). We then performed Random forest model with 80:20 train test split. We got accuracy of 96% and log loss of 0.1 for RF model. 
After that we performed fairness evaluation on Gender and calculated accuracy, precision and recall individually for each gender. The results were similar almost for each gender and this model is properly balanced. 

#### SECTION-7: XG-Boost model ######
We perform XG Boost model on the same dataset where the target variable is categorical. We found the accuracy to be 95% with log loss of 0.14. We then perform evaluation on both Male and Female and the results were similar both the groups. 

We considered RF model as the best one among all, since its accuracy is higher and fairness is good. 

#### SECTION-8: Streamlit app ######
Before creating an app, we install a local tunnel for our app to run outside of colab environment.
After that we save the Random Forest model in a pickle file for use in our app development.
We also save our finalized clean data in a csv file. 

We now create a file called "streamlit_app.py" by creating a code line %%writefile streamlit_app.py
In this section of code we create our code for our app and finally run below code in another cell to generate the url to oprn our app on our local. 

!streamlit run /content/streamlit_app.py & npx localtunnel --port 8501

On running the above line, it generates the local url to open our app online. 
Keep the colab running and open the url in the browser. Enter the required values and click on predict button to predict the sleep efficiency.

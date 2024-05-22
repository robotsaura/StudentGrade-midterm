# Predicting Race/Ethnicity Based on Test Scores - Midterm

## App for predicting race/ethnicity based on test scores Predictor
https://student-grade-race-midterm-0c0bf8b1b3f6.herokuapp.com/

## Author
Saura Naderi

## Class
NU ANA 680

## Problem Statement
In modern educational systems, standardized test scores are often used to assess student performance and potential. However, these scores can sometimes reflect underlying biases that affect students from different racial and ethnic backgrounds. Understanding these biases is crucial for promoting fairness and equality in education.
In this midterm, we are asked to predict race/ethnicity based on test scores alone.
## Description
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
This is a fake data set

## Methodology
### Data Cleaning
- I removed irrelevant columns and kept the race/ethnicity column as the target variable and the math,read,write test scores as the input variables. 
- Split the dataset into a training set (75%) and a test set (25%).

### Model
- I used the SVM classifier using the 'fit' method to train the model
- Race was encoded to numerical values
- The trained model was exported as a pickle file.

### App Development
- Developed a web application using Flask to create a user-friendly interface for inputting data and viewing predictions.
- Deployed the application on Heroku for easy access and scalability.

## Support
I utilized ChatGPT to assist with writing and debugging the code, ensuring the application runs smoothly and meets the project requirements.

## Interesting to Note
It wasn't working for the longest time and then I realized I wrote "App.py" and not "app.py" !!!! 
Accuracy is 34%

## References
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

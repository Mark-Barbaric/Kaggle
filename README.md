# Kaggle Competition Repository

This repository contains workbooks related to various Kaggle Competitions. Full list is below.

## Disaster Tweets

https://www.kaggle.com/competitions/nlp-getting-started

Contains various workbooks related to the NLP With Disaster Tweets Kaggle Course. List of workbooks are below:

- NLP_With_Disaster_Tweets.ipynb: creates embeddings using TFIDVectorizers and trains a Logistic Regression model. Achieved f1 score of 77%.
- NLP_With_Disaster_Tweets_Pretrained_BERT.ipynb: uses the Keras example to fine tune the BERT Pretrained model. Achieve f1 score of 83%.

## Learning

Various workbooks related to Kaggle Courses

- Intermediate Machine Learning: contains all of the courses which are currently covered within this course on Kaggle. https://www.kaggle.com/learn/intermediate-machine-learning

## Tech Layoffs

https://www.kaggle.com/datasets/ulrikeherold/tech-layoffs-2020-2024

- tech_layoffs_eda: this is a workbook containing preliminary EDA of the Tech Layoffs dataset (was completed with data up to Q1_2024).

## Titanic

https://www.kaggle.com/competitions/titanic/overview

These notebooks use a number of custom methods which I moved to the kaggle_lib to allow them to be easily used across all of the workbooks.

- titanic_v1.ipynb: this was the first attempt which trained a LogisticRegression model and achieved an accuracy of 77%.
- titanic_multi_model.ipynb: this workbook uses GridSearch to perform hyperparameter tuning, and trains and evaluates multiple models.
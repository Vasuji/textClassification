
[//]: # (Image References)

[image1]: ./pic/1.png
[image2]: ./pic/2.png 
[image3]: ./pic/3.png 
[image4]: ./pic/4.png 


# Text Classification

This repository includes text classification works which involves following steps:


## Step I: Getting and Cleaning Data
In this step data has been downloaded and cleaned. A new data frame has been created and saved as new data file. Final data file has 3117 rows. There are 5 different classes in the data file. 

[Python notebook: Getting and Cleaning Data](https://github.com/Vasuji/text_classification/blob/master/1.Getting_and_cleaning.ipynb)


## Step II: Exploratory Data Analysis
In this step some exploratory data analysis has been done. Few examples are
1. Plot of class frequencies
2. Net word frequencies plot
3. Plot of  frequencies of words in each class
4. Plot of Word cloud



| Class frequencies         | Net word freq     | Word freq per class     | Word cloud |
| ------------- |:-------------:|:-------------:| ------|
|![Left][image1] | ![Center][image2] | ![Right][image3]| ![Right][image4]

[Python notebook:Exploratory Data Analysis](https://github.com/Vasuji/text_classification/blob/master/2.Exploratory_data_analysis.ipynb)


## Step III: Model Selection and Tuning
This is the main body of the project. It includes three different model building files:

### 1. Model built with Bag of Words. 
This python notebook walks through the model evaluation using bag of words representation of text data and picks a best model for further parameter tuining.
[Python notebook: Bag of Words models](https://github.com/Vasuji/text_classification/blob/master/3.1.model-BagOfWords.ipynb)

### 2. Model built with TFIDF
This python notebook walks through the model evaluation using TF-IDF representation of text data and picks a best model for further parameter tuining.
[Python notebook: TF-IDF Models](https://github.com/Vasuji/text_classification/blob/master/3.2.model-TF-IDF.ipynb)

### 3. Model built with Word to vec
This python notebook walks through the model evaluation using 'word to vec' representation of text data and and specially train a RNN model.
[Python notebook: Word to Vec Models](https://github.com/Vasuji/text_classification/blob/master/3.3.model-Word2Vec.ipynb)


## Discussion:
So far 85-87 % accuracy has been obtained. Typically ```XGBoostClassifier```, ```LogisticRegression``` and ```RNN``` with word to vec embedding are performing better then other classifiers.



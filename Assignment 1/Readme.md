# Sentiment Analysis of Yelp Reviews using Logistic Regression

Sentiment Analysis of Yelp Reviews In this project, we perform a coarse-grained sentiment analysis on Yelp review dataset by proposing a solution using Scikit Learn based Logistic Regression and finding the polarity of reviews at a content level. The project is divided into mainly two parts- preprocessing the data and training the built model using Logistic Regression. The preprocessed data is used to find the sentiment of the reviews with the help of a set of positive and negative keywords. This is considered as semi supervised learning where we first determine the labels for the unlabeled datatset, and then use it to train our model. The end product is a model which predicts the sentiment of the reviews to an accuracy of 70%.

## Getting Started

Place the "yelp_reviews.csv", "pos_words.txt" and "neg_words.txt" in your working directory to easily import the files into your code. Install the Anaconda packages specified in the Prerequisites section before getting started.

### Prerequisites

We need to install the Scikit-Learn package to build the model. 
Tabulate is used to display the results in a tabular form.

```
pip install scikit-learning
pip install tabulate
```

### Pre-Processing

The preprocessing includes the following steps:
(i)   Removal of punctuations from the reviews
(ii)  Lowering the case of the characters in the reviews
(iii) Breaking the sentences into word tokens 
(iv)  Removing the stop words such as "is, the, not, a" etc from the tokens
 
```
['Super', 'simple', 'place', 'amazing', 'nonetheless', 'around', 'since', '30s', 'still', 'serve', 'thing', 'started', 'bologna', 'salami', 'sandwich', 'mustard', 'Staff', 'helpful', 'friendly']
```

After the preprocessing, the tokens are then compared with a set of positive and negative words to assign scores. If token is present in Positive words a score of '1' is assigned, for negative a score of '-1' is assigned and if token is not present in both sets, then a score of '0' is assigned.
Based on these token scores, the mean score for each review is calculated. The value of mean score helps us to label each review as "Positive", "Negative" or "Neutral"

## Building the Model

Pipelining was used to build our Logistic Regression based model. The modules of the pipeline are:
1) Countvectorizer
2) Tfidftransformer
3) Logistic Regression Algorithm

```
Pipeline([('vect', CountVectorizer(analyzer = 'word',lowercase = True,stop_words='english')),
               ('tfidf', TfidfTransformer(smooth_idf=True)),
               ('clf', LogisticRegression(penalty='l2',solver='newton-cg',multi_class='multinomial')),
              ])
```

### Training and Testing

45,000 Reviews were taken from the dataset to train and test the model. These were randomly split in the ratio of 80-20 as training and test data respectively. The training data was then fed to the Pipeline to train the model.

```
x_train,x_test,y_train,y_test = train_test_split(dataset,labels,test_size=0.25,random_state=42)
```

A 5 fold Cross_validation and accuracy calculation were then performed on the training and test data respectively. 


### Results

From the cross_validation and accuracy scores we can see that our model is able to predict with an accuracy close to 70%

```
 precision    recall  f1-score   support

          -1       0.71      0.71      0.71      3615
           0       0.56      0.55      0.56      3835
           1       0.74      0.76      0.75      3800

   micro avg       0.67      0.67      0.67     11250
   macro avg       0.67      0.67      0.67     11250
weighted avg       0.67      0.67      0.67     11250
```

## Observations

After perfoming the tests using multiple models such as Naives Bayes, Decision Trees, Random Forests, SVM and Logistic Regression, we were able to conclude that LogisticRegression gave the best results in terms of cross_validation and accuracy scores.

From the precision, recall and f1 scores, we can see that the accuracy of predicting the positiveand negative reviews is around 75%, but for neutral the score is only 56%. The scores can be improved by only considering the balanced data, .i.e. classifying the reviews as positive and negative instead of using three classes of pos, neg and neutral.

## Authors

* **Jaya Prakash Reddy Dumpa** 

## Acknowledgments

* I would like to thank Prof. Sithu Aung for giving us this opportunity of working on such good assignment and increase our knowledge base on real time application of Machine Learning and Data Mining concepts.



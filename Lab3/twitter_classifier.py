#!/usr/bin/env python
# coding: utf-8

# In[25]:


import warnings
warnings.filterwarnings("ignore")
import random

def load_data():
    data = []
    data_labels = []
    with open("C:/Users/jayap/Desktop/Git Repos/cmpe255-spring19/lab3/pos_tweets.txt",encoding="utf8") as f:
        for i in f: 
            data.append(i) 
            data_labels.append('pos')

    with open("C:/Users/jayap/Desktop/Git Repos/cmpe255-spring19/lab3/neg_tweets.txt",encoding="utf8") as f:
        for i in f: 
            data.append(i)
            data_labels.append('neg')

    return data, data_labels

def transform_to_features(data):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(
        analyzer = 'word',
        lowercase = False,
    )
    features = vectorizer.fit_transform(
        data
    )
    features_nd = features.toarray()
    return features_nd

def train_then_build_model(data_labels, features_nd,data):
    from sklearn.model_selection import train_test_split
    # TODO : set training % to 80%.
    X_train, X_test, y_train, y_test  = train_test_split(features_nd, 
                                                         data_labels,
                                                         train_size=0.80, 
                                                         random_state=1234)

    from sklearn.linear_model import LogisticRegression
    log_model = LogisticRegression()

    log_model = log_model.fit(X=X_train, y=y_train)
    y_pred = log_model.predict(X_test)
    
    # print first 10th prediction in this format:
    # ::{prediction}::{tweet}
    # TODO
    for i in range(0,10):
        index = features_nd.tolist().index(X_test[i].tolist())
        print(":: " + y_pred[i] + ":: " + data[index])
    
    # print accuracy
    from sklearn.metrics import accuracy_score
    # TODO
    print("Accuracy: " + str(accuracy_score(y_test,y_pred)))

def process():
    data, data_labels = load_data()
    features_nd = transform_to_features(data)
    train_then_build_model(data_labels, features_nd,data)


process()


# In[ ]:





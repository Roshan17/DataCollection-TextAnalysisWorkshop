# -*- coding: utf-8 -*-
"""
Created July 2017

@author: arw 
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# We improve our feature matrix builder with 3 additional optional parameters
# This allows us to extract not only word features, but also n-gram features
# We can also set the minimum and maximum frequencies to be considered as valid
# NB: All these are simply passed on to sklearn's Vectorizer classes
def build_feature_matrix(documents, feature_type='frequency',
                         ngram_range=(1, 1), min_df=0.0, max_df=1.0):

    feature_type = feature_type.lower().strip()  
    
    if feature_type == 'binary':
        vectorizer = CountVectorizer(binary=True, min_df=min_df,
                                     max_df=max_df, ngram_range=ngram_range)
    elif feature_type == 'frequency':
        vectorizer = CountVectorizer(binary=False, min_df=min_df,
                                     max_df=max_df, ngram_range=ngram_range)
    elif feature_type == 'tfidf':
        vectorizer = TfidfVectorizer(min_df=min_df, max_df=max_df, 
                                     ngram_range=ngram_range)
    else:
        raise Exception("Wrong feature type entered. Possible values: 'binary', 'frequency', 'tfidf'")

    feature_matrix = vectorizer.fit_transform(documents).astype(float)
    
    return vectorizer, feature_matrix


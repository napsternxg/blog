Title: Sklearn Paired Cosine Distance Issue
Date: 2023-09-07 10:20
Category: posts
Tags: machine-learning
Slug: sklearn-paired-cosine-dist-issue
Authors: Shubhanshu Mishra
Summary: Sklearn Paired Cosine Distance Issue


Here I explore an issue with how sklearn's [`paired_cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html) function returns erronous values when we have one vector with zero norm. 


```python
import numpy as np
from sklearn.metrics.pairwise import paired_cosine_distances, paired_euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer

paired_cosine_distances(
    np.array([[1, 1], [0, 1], [0, 0], [1, 0]]),
    np.array([[1, 1], [0, 1], [0, 1], [0, 1]])
)
# Outputs: array([0. , 0. , 0.5, 1. ])

# dot products
(np.array([[1, 1], [0, 1], [0, 0], [1, 0]]) * np.array([[1, 1], [0, 1], [0, 1], [0, 1]])).sum(axis=-1)
# Outputs: array([2, 1, 0, 0])
```

Dot product between [0, 0] and [0, 1] is zero and hence cosine sim should also be zero (or at best undefined).
However, sklearn paried cosine dist will give a value of 0.5 for this case which is not realistic. 
The reason for this dist value is because in sklearn the cosine dist is defined as:
1 - cos(theta) = 0.5*|A - B| for unit normed vectors A and B. 
This makes |A - B| term equal to 1 for the case where one of the vector has zero norm.

However, if we take the dot product defition of cosine dist = 1 - A.B / (|A|*|B|), 
this value should either be undefined as we have a 0/0 division or should be 1.0 assuming A.B = 0 takes precedence.

This can cause incorrect results when mining massive datasets using pairwise cosine dist which is an important metric in ML for NN search or as a feature to downstream models.


Make sure to keep this in mind or filter out values with zero norm when working with cosine distances in sklearn.







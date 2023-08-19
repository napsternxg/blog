Title: Precision and Recall are just filtered accuracies
Date: 2023-08-19 23:48
Category: posts
Slug: accuracy-precision-recall


In this post I will show how precision and recall are related to accuracy and how they can be thought of as filtered versions of accuracy.

# Accuracy

Accuracy is a fundamental concept in evaluating every day systems. In simple terms, accuracy is defined as proportion of times the predictions of our system matched the true outcome (assuming the true outcome exists). For this post lets follow the scikit-learn convention and define `y_true` as the true outcome and `y_pred` as the predictions. 

In mathematical terms accuracy can be simply written as the mean value of the indicator function which is 1 when the `y_true == y_pred` and 0 otherwise.

More consicely, this can be written as $accuracy(y_{true}, y_{pred}) = \frac{1}{N} * \sum_i \mathbb{1}[y_{true} = y_{pred}]$.

## Confusion Matrix

Another popular way of computing accuracy is by using the confusion matrix. If our outcome classes can be enumerated as 0, 1, 2, ... then the confusion matrix $CM$ will contain elements $CM[i, j] = \sum_i \mathbb{1}[y_{true} = i \land y_{pred} = j]$, i.e. count of the number of times $y_{true}$ was $i$ and $y_{pred}$ was $j$. 

A confusion matrix for binary classification (assuming $+$ as the positive class) may look as follows:

| true/pred | $-$ | $+$ | total |
| ---   | --- | --- | --- |
| $-$     | 10 [TN] | 05 [FP]  | 15 [$-_{true}$]|
| $+$     | 35 [FN] | 50 [TP] | 85 [$+_{true}$] |
| total | 45 [$-_{pred}$]     | 55 [$+_{pred}$]  | 100 |

Here the terms mean the following:

| Term | Defition | Comments |
| --- | --- | --- |
| TP | True Positives | Number of times the $+$ class is predicted as $+$; correctly predicted as positive |
| FP | False Positives | Number of times the $-$ class is predicted as $+$; i.e. incorrectly predicted as positive |
| FN | False Negatives | Number of times the $+$ class is predicted as $-$; i.e. incorrectly predicted as negative |
| TN | True Positives | Number of times the $-$ class is predicted as $-$; i.e. correctly predicted as negative |

This confusion matrix approach easily extends to multi-class cases and is quite helpful when defining Precision, Recall metrics as we will see below.

Finally, Accuracy can be defined in terms of the confusion matrix as $accuracy = \frac{TP + TN}{TP + FP + FN + TN}$

# Precison and Recall

Precision and Recall are popular evaluation metrics used for evaluating classification systems and are very valuable when we have multiple classes and these classes are present with a skewed distribution in the data. 

Precision recall metrics are often defined using the confusion matrix approach as follows: 

* $precision = \frac{TP}{ TP + FP}$
* $recall = \frac{TP}{ TP + FN}$


However, I find this definition restrictive, i.e. this only works for binary classification use cases and for each new class we need to define a new confusion matrix. I also find this formulation difficult to remember. E.g. in my initial days of learning these definitions I often used to confuse False Positive and False Negatives. 

 Furthermore, this also relies on the confusion matrix approach to compute the values, which has its benefits in terms of computational complexity as we can compute the confusion matrix once on a large dataset and compute all sorts of metrics on top of this. 


 Here, I am going to share my convention of remembering what precision and recall means and this will help us later connect to the accuracy metric. 


 ## Precision Recall as filtered accuracies

 If you look at the confusion matrix above you will notice that precision is really defined as the ratio of $\frac{CM[+, +]}{\sum_{true~classes} CM[:, +]}$.
 
 This ratio can be stated $\frac{correct~prediction~of~+_{class}}{all~the~ predictions~of~+_{class}}$. 

 If you notice clearly, this is just the accuracy of the data limited to items predicted as $+_{class}$ or simply $precision(y_{true}, y_{pred}, class) = accuracy(y_{true}[y_{pred} = class], y_{pred}[y_{pred} = class])$, where $X[y=class]$ selects only those items from $X$ where $y=class$, we can $y = class$ as a filter or mask.

 Similarly, recall is $\frac{CM[+, +]}{\sum_{pred~classes} CM[+, :]}$ or $\frac{correct~prediction~of~+_{class}}{all~the~items~of~+_{class}}$ or $recall(y_{true}, y_{pred}, class) = accuracy(y_{true}[y_{true} = class], y_{pred}[y_{true} = class])$. 


 So if you look closely, you will notice that precision and recall only differ in the filter used to send data to accuracy. Precision uses the filter $[y_{pred} = +]$ while recall uses the filter $[y_{true} = +]$.

 Furthermore, we can see that if we swap the arguments to precision or recall we get the value for the other, i.e. $precision(y_{true}, \boldsymbol{y_{pred}}, class) = recall(\boldsymbol{y_{pred}}, y_{true}, class)$.


 Furthermore, this definition can easily be extended to multi class setting where you simply need to replace $+$ with the new class.


## Python Implementation

Next we are going to see how to implement these functions in python using the abstractions defined above.

```python
import numpy as np

def accuracy(y_true, y_pred):
  return (y_true == y_pred).mean()

def masked_accuracy(x, y, mask):
  return accuracy(x[mask], y[mask])

def class_specific_accuracy(x, y, true_class):
  mask = (x == true_class)
  return masked_accuracy(x, y, mask)

def recall(y_true, y_pred, true_class):
  return class_specific_accuracy(y_true, y_pred, true_class)

def precision(y_true, y_pred, true_class):
  return class_specific_accuracy(y_pred, y_true, true_class)

# Notice that recall(y_true, y_pred, true_class) == precision(y_pred, y_true, true_class)
```

We can now compare the implementation against the sklearn implementation. 

```python

N = 10000
true_class = 1
y_true = np.random.randint(true_class + 1, size=N)
y_pred = np.random.randint(true_class + 1, size=N)

report = classification_report(y_true, y_pred)
print(report)

print(f"{accuracy(y_true, y_pred)=:.2f}")
print(f"{precision(y_true, y_pred, true_class)=:.2f}")
print(f"{recall(y_true, y_pred, true_class)=:.2f}")
print(f"{recall(y_true, y_pred, true_class)=:.2f} == {precision(y_pred, y_true, true_class)=:.2f}")
```

Leading to the outputs:

```terminal
              precision    recall  f1-score   support

           0       0.50      0.50      0.50      4939
           1       0.51      0.50      0.51      5061

    accuracy                           0.50     10000
   macro avg       0.50      0.50      0.50     10000
weighted avg       0.50      0.50      0.50     10000

accuracy(y_true, y_pred)=0.50
precision(y_true, y_pred, true_class)=0.51
recall(y_true, y_pred, true_class)=0.50
recall(y_true, y_pred, true_class)=0.50 == precision(y_pred, y_true, true_class)=0.50
```

If you notice, this doesn't require us to construct the full confusion matrix thereby making the approach suitable where the number of classes is very large. 


## Example of application to Named Entity Recognition Evaluation

One example of where this is useful is when evaluating named entity recognition systems where we want to evaluate if the model prediction at the entity level. E.g. `[Shubhanshu Mishra](PER) visited [SFO](LOC)` was predicted by the model as `[Shubhanshu](PER) Mishra visited [SFO](LOC)` with entity types as `PER` and `LOC`. Here, if we define a class as `(docid, start, end, type)` i.e. `y_true = [(0, 0, 17, PER), (0, 26, 29, LOC)]` and `y_pred=[(0, 0, 10, PER), (0, 26, 29, LOC)]` we can easily compute the precision, and recall values of the data as simply `precision = len(set(y_true) & set(y_pred)) / len(set(y_pred))` and `recall = len(set(y_true) & set(y_pred)) / len(set(y_true))` and their type specific versions as follows:

```python
def precision_ner(y_true, y_pred, type):
    type_specific_true = set(((d, s, e, t) for (d, s, e, t) in y_true if t == type))
    type_specific_pred = set(((d, s, e, t) for (d, s, e, t) in y_pred if t == type))
    correct_predictions = type_specific_true & type_specific_pred
    return len(correct_predictions) / len(type_specific_pred)

def recall_ner(y_true, y_pred, type):
    return precision_ner(y_pred, y_true, type)
```

You can now extend it to Named Entity Recognition and Disambiguation (NERD) by defining the class as `(docid, start, end, type, entity_id)`. This is the approach we have taken in our paper [TweetNERD - End to End Entity Linking Benchmark for Tweets](https://proceedings.neurips.cc/paper_files/paper/2022/hash/09723c9f291f6056fd1885081859c186-Abstract-Datasets_and_Benchmarks.html).


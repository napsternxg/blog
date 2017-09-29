Title: Ask Me Anything - Dynamic Memory Networks for Natural Language Processing
Date: 2016-03-09 10:20
Modified: 2016-03-09 10:20
Category: posts
Tags: deeplearning, reviews
Slug: ama-socher
Authors: Shubhanshu Mishra
Summary: End to end module to learn NLP tasks as Q/A tasks. 


**Authors: Ankit Kumar, Ozan Irsoy, Peter Ondruska, Mohit Iyyer, James Bradbury, Ishaan Gulrajani, Victor Zhong, Romain Paulus, Richard Socher**

## Overview

This paper presents a general purpose neural network framework called Dynamic Memory Networks \(DMN\), for solving NLP tasks such as question answering \(QnA\), text classification for sentiment analysis, and Part-of-Speech \(POS\) tagging. The authors achieve this by converting each task into its equivalent QnA form e.g. "What is the sentiment?", "POS tags?" etc. They report state of the art accuracy on all the tasks.

## Thoughts

The paper proposes an end-to-end differentiable NN module called DMN. It consists of 4 parts, an input module, question module, episodic memory module and an answer module. Their works appear quite similar to the MemNN neural network with the main difference being the episodic memory module, which is an attention based recurrent module over the input hidden states and the question state. The authors argue that in many cases multiple passes over all the facts and question can help in better question answering. This is also demonstrated in their visualization of the attention matrix for the sentiment analysis case. This application is also demonstrated to work quite well for the question answering tasks.

Some highlights of the paper are:

* Recurrent processing of multiple sentences and outputting only one hidden state per sentence.
* Recurrent attention based episodic memory
* Supervised training of the episodic memory

Although the authors report a better average performance of DMN on Facebook bABI dataset compared to MemNN, there are many instances where their performance is worse then MemNN. On POS tagging, their method equals the performance of the previous state of the art SCNN, although their ensemble model outperforms SCNN outperforms by 0.06%. On sentiment analysis, their model is better by 0.5% compared to CNN-MC model of Kim 2014.

One important thing which comes out from the comparison is that the CNN models are quite close to RNN models in performance for sentiment and POS tagging tasks. I would be interested in knowing, if this is because of similar properties of CNN which can encode attention during convolution and pooling operations. Also, given the fact that RNNs are sometimes more expensive to train than CNN, should we try out more CNN applications in NLP, probably a CNN over the attention matrix.

For the multi-sentence input, I would be interested in knowing how the DMN performns if there is an output from the Input module per token for each sentence. I think this will give the module more fine-grained control over the details in each sentence, especially, when it involved path finding and positonal arguments.

Overall, I think this paper is another important step in the direction of end-to-end NLP, and supports the the prediction of Christopher Manning of "Deep Learning Tsunami in NLP". Given the previous seminal work in the MemNN paper as well as the NLP from Scratch paper, this work also will get more researchers involved in using end to end sequence to sequence learning approaches in NLP tasks.

### Reference

```
@article{DBLP:journals/corr/KumarISBEPOGS15,
author = {Ankit Kumar and
Ozan Irsoy and
Jonathan Su and
James Bradbury and
Robert English and
Brian Pierce and
Peter Ondruska and
Ishaan Gulrajani and
Richard Socher},
title = {Ask Me Anything: Dynamic Memory Networks for Natural Language Processing},
journal = {CoRR},
volume = {abs/1506.07285},
year = {2015},
url = {http://arxiv.org/abs/1506.07285},
timestamp = {Wed, 01 Jul 2015 15:10:24 +0200},
biburl = {http://dblp.uni-trier.de/rec/bib/journals/corr/KumarISBEPOGS15},
bibsource = {dblp computer science bibliography, http://dblp.org}
}
```

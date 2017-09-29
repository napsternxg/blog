Title: Revisiting Semi-Supervised Learning with Graph Embeddings
Date: 2016-04-04 10:20
Modified: 2016-04-04 10:20
Category: posts
Tags: deeplearning, reviews
Slug: semi-sup-graphemb-salakh
Authors: Shubhanshu Mishra
Summary: Semi-supervised way of learning graph embeddings

**Authors: Zhilin Yang, William Cohen, Ruslan Salakhutdinov**

## Overview

This is an interesting paper which describes a semi-supervised learning algorithm for Graph Embedding. The authors have build up on the DeepWalk \[1\] and LINE \[2\] algorithms which learn embeddings of nodes in a graph in a similar way Word2Vec Skipgram model \[3\] learns word embeddings based on context. They add a semi-supervised component using both Transductive and Inductive learning, which utilizes partially labeled data to jointly train the model to predict the class of the labeled nodes and the context of the all nodes. The authors report an increase in accuracy over other semi-supervised methods, on several text classification, entity extraction and entity classification tasks.

## Thoughts

I found the paper to be really interesting because of its ability to lay some foundation in joint training of embeddings on labeled and unlabled data. The authors differentiate their paper from other semi-supervised algorithms in its use of graph to identify context of the instances, while at the same time using features of each instance.

It is interesting to see, how many algorithms have build up on the word2vec skipgram approach to learn embeddings for the data instances. One of the major challenges with the approach is coming up with a proper way to generate the negative samples. Papers like DeepWalk and LINE use a random walk approach to generate the negative samples from the data. The authors have presented a really useful way to sample the positive and negative samples from the graph which, at the same time ensures that the labeled data is also present in each sample while training.

The authors' presentation of the transductive and inductive variants of the algorithms, presents a framework to apply this approach to cases where the predictions need to be done on in-sample unlabeled data \(transductive\) as well as out of sample unlabeled data \(inductive\).

One issue I found with the paper was the _Experiments_ sections and the data used for the analysis. The CiteSeer, CORA and PubMed data are relatively small in my understanding, to describe the efficiency of this model. However, on the larger DIEL data, the algorithms' significant performance improvement can be taken as a measure of its strength over other mentioned algorithms.

Overall, I think it is a very useful paper which will push the Machine Learning field forward by further utilizing the vector embedding approach and nicely incorporating it into a semi-supervised setting.

It would be interesting to use the same approach on Skip-Thought vectors \[4\] or paragraph vectors connected by topics, users etc.

## References

\[1\] Perozzi, Bryan, Rami Al-Rfou, and Steven Skiena. "Deepwalk: Online learning of social representations." Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2014.

\[2\] Tang, Jian, et al. "Line: Large-scale information network embedding." Proceedings of the 24th International Conference on World Wide Web. International World Wide Web Conferences Steering Committee, 2015.

\[3\] Mikolov, Tomas, et al. "Distributed representations of words and phrases and their compositionality." Advances in neural information processing systems. 2013.

\[4\] Kiros, Ryan, et al. "Skip-thought vectors." Advances in Neural Information Processing Systems. 2015.

```
@misc{1603.08861,
Author = {Zhilin Yang and William Cohen and Ruslan Salakhutdinov},
Title = {Revisiting Semi-Supervised Learning with Graph Embeddings},
Year = {2016},
Eprint = {arXiv:1603.08861},
}
```





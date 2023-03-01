Title: Why Conditional Probability?
Date: 2022-09-14 10:20
Category: posts
Tags: linear-algebra, sql
Slug: linear-algebra-in-sql
Authors: Shubhanshu Mishra
Summary: The computational reason for using conditional probability for sampling
Status: draft

## Key Idea

One way of sampling from a distribution is to construct the CDF and then draw a random uniform between [0, 1], use this to find the sampled item. 

However, multi-dimension CDF can't be constructed as there is no natural ordering of vectors. 
Conditional probability allows us to factor a joint distribution into a product of conditional distributions. 
Now we can sample each of these in any oder. Since, each sampling only requires genrating 1 variable, we can construct the CDF and then generate the output. 



Add examples. 

Compared with Gibbs Sampling and MH sampling and other methods. 

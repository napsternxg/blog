Title: Why Conditional Probability?
Date: 2022-09-14 10:20
Category: posts
Tags: probability
Slug: why-conditional-probability
Authors: Shubhanshu Mishra
Summary: The computational reason for using conditional probability for sampling
Status: draft

## Key Idea

One way of sampling from a distribution is to construct the CDF and then draw a random uniform between [0, 1], use this to find the sampled item. 

However, multi-dimension CDF can't be constructed as there is no natural ordering of vectors. 
Conditional probability allows us to factor a joint distribution into a product of conditional distributions. 
Now we can sample each of these in any oder. Since, each sampling only requires genrating 1 variable, we can construct the CDF and then generate the output. 


$$
X \sim P(x_0, x_1, ..., x_n) \\
X \sim P(x_0)P(x_1 | x_0)...P(x_n | x_0, x_1, ..., x_{n-1})
$$

Compared with Gibbs Sampling and MH sampling and other methods. 

Gibbs Sampling uses Conditional Probability. 

Take the example of the Cholskey decomposition used for multivariate normal sampling. It can be related to conditional probablities. 

$$
 \begin{array}{l}
x \sim  \mathcal{N}(\boldsymbol{\mu } , \boldsymbol{K})\\
K = LL^{T}\\
u_{ij}  \sim  \mathcal{N}( 0, 1)\\
x  = \mu  + Lu\\
x_{0}  = L_{00} u_{00}\\
x_{1}  = L_{10} u_{00}  + L_{11} u_{11}\\
x_{1}  = L_{10} /L_{00}  x_{0}  +L_{11} u_{11}  \\
x_{1}  \sim  \mathcal{N}( L_{10} /L_{00}  x_{0} , L_{11})\\
x_{1}  \sim  P( x_{1}  | x_{0})\\
x_{i}  \sim  P( x_{i}  | x_{\neg i})
\end{array}
$$


Often to make this sampling more efficient we should sample from the eigen vectors of the covariance matrix of the variables. 

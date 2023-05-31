Title: Understanding vectors
Date: 2022-09-02 10:20
Category: posts
Tags: linear-algebra, complex-numbers
Slug: understanding-vectors
Authors: Shubhanshu Mishra
Summary: Using Geometric Notion of Vectors to understand their properties and the inner product
Status: draft


## Raw notes

* The abstract way of thinking vectors is to have objects and we can use one object to measure other objects. 
* An object is represented by a vector. 
* NOTE: We haven't any representation to the vector or the object. This will become apparent later as we will have different types of objects, e.g. functions, images, text, etc. 
* The measurement can happen different ways. 
* We want a measurement which does not change if we measure object a using object b, or vice-versa. 
* One option is to take the area spanned by the two objects as a common measurement. However, this has a downside of sign flip if we go from a to b or from b to a. This area is commonly referred to as cross-product. 
* The more natural measurement is to project one object on the other, while moving the other object 90 degrees towards the first. This provides two new rectagles whose areas are same. This has the surprising property of maintianing sign and measure value. Area is always measured in anti-clockwise direction.
 - E.g. a's projection on b is $a*cos(\theta)$ and if b is rotated towards a by 90 degrees then it becomes b' now the area will be $b' x a cos(\theta) \hat{b}$. Notice that $\hat{b}$ and b' are going to be orthogonal by definition. 
 - if we rotate a towards b to get a' and project b on a to get $b*cos(\theta)$, then the area will be $b cos(\theta) \hat{a} x a'$. Again $\hat{a}$ and a' are going to be orthogonal by definition.
 - In both cases the area will then be $|b'|*|acos(\theta)| = |b||a|cos(\theta)$, and $|a'|*|bcos(\theta)| = |a||b|cos(\theta)$. 

 * A matrix then is just a way to perform measurement of an object using a collection of objects. 
 * Let us define a measured object (or simply referred to as the object from now) to always be a represented by a standing vector (or a column vector, but notice we haven't yet defined that a vector is a collection of numbers, hence I wanted to be abstract here).
 * Let us also define a measuring object (or we can call it a scale) to always be represented by a laying vector. 
 * Now a matrix will be a collection of laying vectors, represeting a list of measuring objects (or scales). 
 * If we would like to know the measurements of an object by a list of scales, we can expect as output a list of measurements. E.g. for 2 scales measuring a single object, the output will be 2 measurements. 
 * If we have a list of objects whose measurements we want to find given a list of scales we will represent the list of objects via a list of standing vectors, and list of scales as a list of laying vectors. 
 * We can observe that if we want to measure a list of vectors by themselves i.e. by the same list of vectors, the we can just convert a list of standing vectors to a list of lying vectors. This operation can be defined as the transpose (we will see its connection to matrics later).
 * Let the list of object vectors be a matrix A, then the eqivalent list of these objects as scales will be $A^T$. 
 * Extracting all the measurements of the objects by themselves as scales can be done via $A^T x A$, this will gives us a list of $n * n$ measurements, where the diagonal will be the self measurements. 
 * Notice that self-measurement using the rotated rectangle as defined above correctly captures the length as self-project is the same vector and its rotation by 90 gives the square whose area is equal to the square of the length of the vector. We can consider the rotation in any arbitrary plan spanned by a and its orthogonal vector. A way to think of this is to wiggle a in any plane by an infinitismal angle, and then doing the same calculation in the plane spanned using a and its wiggled counter-part as b and then later taking the limit of $\theta$ to 0. 
 * Also notice we have not defined any basis till now, the vectors exist in empty space right now with no coordinate systems. This means all measurements happen via projection and rotation. Furthermore, all vectors have one end at the same point, this makes the notion of angle well defined.




## Resources

* [J2. Unitary Groups](https://www.youtube.com/watch?v=yeK2N7FbkVI) - Helped me understand unitary matrices and their basis. One thing which pops out is invest of matrix is similar to if each vector was rotated 90 degrees clockwise and the order of the vectors was swapped. Need to explore this in details. 
* [Complex eigen values of a matrix](https://www.youtube.com/watch?v=9bPwL30PBwM) - Provides a good connection between the scaling and rotation matrix and how it is captured by eigen values which are complex. 
* [Motivation behind Definition of Inner Product Space](https://math.stackexchange.com/questions/2488135/motivation-behind-definition-of-inner-product-space) - Provides how Inner product is related to complex and geometric numbers

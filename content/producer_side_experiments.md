Title: Producer Side Experimentation
Date: 2025-05-09 23:48
Category: posts
Slug: producer-side-experimentation
Status: draft

## Design of Recommender systems

* Item:
* Producer: Produces Items
* User: Interacts with item
* Goal is user benefits from seeing the presented items in terms of key metrics


## Running Experiments in Recommender systems

* Split User into control and treatment
* Show one variant of content to control and another to treatment
* Compute viewer side metrics for each group, e.g. CTR, retention, UAM
* Test for significant change in the metrics using statistical methods
* This tests for impact on user population

## Challenge: How to check for impact on items and producer

* What if we are interested in knowing the impact on items/producer when shown to different viewers.


## Techniques from industry

LinkedIn:
* https://proceedings.neurips.cc/paper_files/paper/2021/file/32e19424b63cc63077a4031b87fb1010-Paper.pdf - https://arxiv.org/abs/2106.00762
* https://arxiv.org/abs/2310.16294

Tencent:
* https://arxiv.org/abs/2401.15811 - Uses interleaving strategy

Academia:
* https://arxiv.org/abs/2206.13102 - Modeling Content Creator Incentives on Algorithm-Curated Platforms

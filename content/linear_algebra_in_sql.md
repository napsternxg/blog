Title: Linear Algebra in SQL (BigQuery, DuckDB AND SQLite examples)
Date: 2022-09-14 10:20
Category: posts
Tags: linear-algebra, sql
Slug: linear-algebra-in-sql
Authors: Shubhanshu Mishra
Summary: Implementing common linear Algebra concepts in SQL with implementation in BigQuery and SQLite
Status: draft

## Introduction

Common operations are as follows:

### Cosine Similarity

```sql
WITH
X AS (
    SELECT 0 AS id, [1, 2, 3] AS emb
    UNION ALL
    SELECT 1 AS id, [1, 2, 3] AS emb
)
X_sparse AS (
    SELECT 0 AS id, [(0 AS idx, 1 AS v), (2 AS idx, 1 AS v), (3 AS idx, 1 AS v)] AS emb
    UNION ALL
    SELECT 1 AS id, [(1 AS idx, 1 AS v), (2 AS idx, 1 AS v), (3 AS idx, 1 AS v)] AS emb
),
X_norm AS (
    SELECT id, SUM(v*v) AS norm
    FROM X
    CROSS JOIN UNNEST(emb)
),
X_flat AS (
    SELECT id, idx, v
    FROM X CROSS JOIN UNNEST(emb) 
    AS v WITH OFFSET AS idx -- Only needed for dense
)
Dotprod_flat AS (
    SELECT x.id AS id_x, y.id AS id_y, idx, SUM(x.v*y.v) AS v
    FROM X_flat AS x
    FULL OUTER JOIN X_flat AS y USING (idx)
    GROUP BY x, y, idx
)

SELECT id1, id2, SUM(v/SQRT(x.norm*y.norm)) AS cosine_sim
FROM Dotprod_flat
JOIN X_norm AS x ON x.id = id1
JOIN X_norm AS y ON y.id = id2
GROUP BY idx

```


## DB Implementations

### DuckDB

- [Friendlier SQL with DuckDB](https://duckdb.org/2022/05/04/friendlier-sql.html)
- Can be made faster with Apache Arrow integration. 


## Related Works

* [Machine Learning, Linear Algebra, and More: Is SQL All You Need?](https://www.youtube.com/watch?v=D584L-oSXkI)
* [Scalable Linear Algebra on a Relational Database System](https://cacm.acm.org/magazines/2020/8/246372-scalable-linear-algebra-on-a-relational-database-system/fulltext)
* [HyperDB](https://hyper-db.de/)
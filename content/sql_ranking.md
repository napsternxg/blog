Title: Ranking Function in SQL
Date: 2024-11-21 10:20
Category: posts
Tags: sql
Slug: ranking-function-in-sql
Authors: Shubhanshu Mishra
Summary: Different between different SQL ranking functions

What are the different types of ranking function in SQL. I will take the example of SQL implemented in [Snowflake](https://docs.snowflake.com/en/sql-reference/functions/rank) but other sql engines have similar format.

```sql
WITH corn_production AS (
SELECT 
v.VALUE[0] AS farmer_ID,
v.VALUE[1] AS state,
v.VALUE[2] AS bushels,
FROM LATERAL FLATTEN([
[1, 'Iowa', 100],
[2, 'Iowa', 110],
[3, 'Kansas', 120],
[4, 'Kansas', 130],
[5, 'Kansas', 130],
[6, 'Kansas', 130]
]) AS v
)
SELECT 
farmer_ID, state, bushels,
ROW_NUMBER() OVER (ORDER BY bushels DESC) row_num,
RANK() OVER (ORDER BY bushels DESC) srank,
DENSE_RANK() OVER (ORDER BY bushels DESC) drank,
PERCENT_RANK() OVER (ORDER BY bushels DESC) prank,
CUME_DIST() OVER (ORDER BY bushels DESC) cdist,
FROM corn_production
ORDER BY row_num;
```

| FARMER_ID 	| STATE    	| BUSHELS 	| ROW_NUM 	| SRANK 	| DRANK 	| PRANK 	| CDIST  	|
|-----------	|----------	|---------	|---------	|-------	|-------	|-------	|--------	|
| 4         	| "Kansas" 	| 130     	| 1       	| 1     	| 1     	| 0     	| 0.5    	|
| 5         	| "Kansas" 	| 130     	| 2       	| 1     	| 1     	| 0     	| 0.5    	|
| 6         	| "Kansas" 	| 130     	| 3       	| 1     	| 1     	| 0     	| 0.5    	|
| 3         	| "Kansas" 	| 120     	| 4       	| 4     	| 2     	| 0.6   	| 0.6667 	|
| 2         	| "Iowa"   	| 110     	| 5       	| 5     	| 3     	| 0.8   	| 0.8333 	|
| 1         	| "Iowa"   	| 100     	| 6       	| 6     	| 4     	| 1     	| 1      	|


The ranking functions available are `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PERCENTILE_RANK`, and `CUME_DIST`.

`ROW_NUMBER`, `RANK`, `DENSE_RANK` provide numerical ranks.
`PERCENTILE_RANK`, and `CUME_DIST` provide percentile based ranks. 

The challenge is when you have column values which are duplicates leading to tie resolution in 

If you just want ranks for top K, use `ROW_NUMBER`, it will break ties arbitrarily. `RANK` will duplicate ranks but will also create gaps in ranks. `DENSE_RANK` will duplicate ranks but will not create rank gaps. 

`PERCENT_RANK` and `CUME_DIST` are good if you want to know where the element lies in the distribution. 





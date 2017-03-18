select a.country,a.month,((1/max(n))*(max(n)+1-(2*sum(revenue* (n+1- rownum)))/max(revenue_total))) gini_index FROM
(
SELECT country,month,revenue,row_number() OVER (PARTITION BY country,month) rownum
FROM monthly
) a JOIN
(SELECT country,month,count(*) AS n,sum(revenue) revenue_total from monthly group by 1,2
) b USING (country,month) GROUP BY 1,2

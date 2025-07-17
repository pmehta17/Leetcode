# Write your MySQL query statement below
SELECT P.product_name, S.year, S.price from Sales S inner join Product P on S.Product_ID = P.Product_ID
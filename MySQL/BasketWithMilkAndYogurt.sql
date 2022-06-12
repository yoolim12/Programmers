-- 프로그래머스 SQL 우유와 요거트가 담긴 장바구니
-- 나의 풀이
select cart_id
from cart_products
where cart_id in
(select cart_id from cart_products where name = 'Milk')
and
cart_id in
(select cart_id from cart_products where name = 'Yogurt')
group by cart_id
order by cart_id

-- 또 다른 나의 풀이
-- with t1 as (
--     select cart_id
--     from cart_products
--     where name = 'Milk'
-- ), t2 as (
--     select cart_id
--     from cart_products
--     where name = 'Yogurt'
-- )




-- select t1.cart_id
-- from t1
-- inner join t2
-- on t1.cart_id = t2.cart_id
-- order by cart_id;

-- 다른 좋은 풀이
-- SELECT DISTINCT A.CART_ID
-- FROM CART_PRODUCTS AS A, CART_PRODUCTS AS B
-- WHERE A.CART_ID = B.CART_ID
-- AND A.NAME = 'Milk' AND B.NAME = 'Yogurt'
-- ORDER BY A.CART_ID

-- SELECT 
--   CART_ID 
-- FROM 
--   CART_PRODUCTS
-- WHERE NAME IN ("Milk", "Yogurt") 
-- GROUP BY CART_ID HAVING COUNT(DISTINCT(NAME)) >= 2
-- ORDER BY CART_ID
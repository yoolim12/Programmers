-- 입양 시각 구하기(2)
-- 코드를 입력하세요
-- SELECT hour(datetime) as hour, count(hour(datetime)) as count
-- from animal_outs
-- group by hour
-- order by hour

with recursive hourlist as (
    select 0 as hour
    union all
    select hour + 1
    from hourlist
    where hour < 23
)

select hourlist.hour as hour, count(hour(o.datetime))
from hourlist
left join animal_outs as o
on hourlist.hour = hour(o.datetime)
group by hourlist.hour

-- 여기서 
-- select hourlist.hour as hour, count(hourlist.hour)
-- from hourlist
-- left join animal_outs as o
-- on hourlist.hour = hour(o.datetime)
-- group by hourlist.hour 
-- 로 하면 안되는 이유
-- --> 
-- select *
-- from hourlist
-- left join animal_outs as o
-- on hourlist.hour = hour(o.datetime)
-- 를 돌려보면 알 듯이 hour 컬럼은 0~23까지 쭉 나오고 datetime 컬럼은 null 상태로 있음
-- 따라서 group by hourlist.hour로 해서 count(hourlist.hour)로 하게 되면 hour가 0일 때
-- hour = 0인 컬럼 1개 해서 count가 원하는 값 0 이 아닌 1로 나오게 됨
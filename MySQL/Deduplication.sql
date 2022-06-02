-- 중복 제거하기
-- 코드를 입력하세요
select count(distinct(name))
from animal_ins

-- select count(distinct(name))
-- from animal_ins
-- where name is not null
-- 결과는 차이가 없습니다. 어차피 count 함수는 null의 개수는 세지 않기 때문이다.
-- [The COUNT() function returns the number of records returned by a select query. Note: NULL values are not counted.]
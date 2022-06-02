-- 중성화 여부 파악하기
-- 코드를 입력하세요
select animal_id, name, (case when sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%' then 'O' else 'X' end) as sex_upon_intake
from animal_ins
where sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%'
order by animal_id;

-- 주의!!
-- sex_upon_intake like '%Neutered%' or '%Spayed%'
-- 이렇게 작성하면 앞의 '%Neutered%'만 인식해서 sex_upon_intake like '%Neutered%'만 처리한다.

-- MySQL의 IF문을 통해서도 풀 수 있다
-- 참고 : https://redcow77.tistory.com/260
-- if(조건문, 참일 때의 값, 거짓일 때의 값)
select animal_id, name, if(sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%', 'O', 'X') as '중성화'
from animal_ins
order by animal_id;
-- 루시와 엘라 찾기
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id
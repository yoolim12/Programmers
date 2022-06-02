-- 헤비 유저가 소유한 장소
-- 코드를 입력하세요
SELECT id, name, host_id
from places
where host_id in (
    SELECT host_id
    from places
    group by host_id
    having count(id) >= 2
    order by id
)
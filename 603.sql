# Write your MySQL query statement below
select distinct a.seat_id from Cinema a, Cinema b where a.free = 1 and b.free =1 and abs(a.seat_id - b.seat_id) = 1 order by a.seat_id asc

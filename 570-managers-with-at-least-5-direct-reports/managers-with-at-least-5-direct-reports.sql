# Write your MySQL query statement below
select m.name
from 
(
select e.managerId, count(e.id)
from Employee e
group by  e.managerId
having count(e.id)  >= 5
) emp 
inner join 
Employee m
on emp.managerId = m.id

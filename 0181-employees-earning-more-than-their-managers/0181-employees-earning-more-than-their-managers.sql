# Write your MySQL query statement below

select 
    e.name as 'Employee'
from 
    Employee as e,
    Employee as m
where 
    e.ManagerId = m.id 
    and 
        e.salary > m.salary

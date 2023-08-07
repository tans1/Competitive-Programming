# Write your MySQL query statement below

select 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary

from 
    Employee as e
join 
    Department as d
    on e.departmentId = d.id
    
where (d.id, e.salary) in 
(
    select e.departmentId , max(e.salary)
    from Employee as e 
    group by e.departmentId
)
    


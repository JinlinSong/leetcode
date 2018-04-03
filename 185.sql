# Write your MySQL query statement below
set @sal = 0;
SELECT d.name as Department, x.Name as Employee, Salary
from (select e.Name, Salary, DepartmentId, @Rank := CASE WHEN @dept_id!=e.Departmentid THEN 1
WHEN @sal=Salary THEN @Rank ELSE @Rank+1 END as Rnk, @dept_id:=departmentid, @sal:=Salary
from Employee e
order by DepartmentId ASC,Salary DESC)x
join department d on d.id = x.Departmentid and Rnk < 4
order by d.name, Salary DESC;

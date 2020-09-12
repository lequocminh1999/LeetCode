--https://leetcode.com/problems/department-highest-salary/

# Write your MySQL query statement below
SELECT D.Name as Department, E.Name as Employee, E.Salary
FROM Employee E, Department D
WHERE E.DepartmentId= D.Id and E.Salary >= ALL (
            SELECT EE.Salary
            FROM Employee EE, Department DD
            WHERE EE.DepartmentId=DD.Id and EE.DepartmentId=D.Id
)
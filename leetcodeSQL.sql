create database Test;
use Test;
show tables;

Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255));
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255));
Truncate table Person;
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen');
Truncate table Address;
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York');

show tables;
select * from person;
select * from Address;

select firstname, lastname, city, state from person left join address on person.personid = address.personid;

Create table If Not Exists Employee (Id int, Salary int);
Truncate table Employee;
insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');

Create table If Not Exists Scores (Id int, Score DECIMAL(3,2));
Truncate table Scores;
insert into Scores (Id, Score) values ('1', '3.5');
insert into Scores (Id, Score) values ('2', '3.65');
insert into Scores (Id, Score) values ('3', '4.0');
insert into Scores (Id, Score) values ('4', '3.85');
insert into Scores (Id, Score) values ('5', '4.0');
insert into Scores (Id, Score) values ('6', '3.65');

select * from scores order by score DESC;

select * from scores group by score order by score DESC;

select score, (select count(distinct score) from scores where score >= s.score) ranks from scores s order by score desc;

select salary from employee order by salary desc limit 2, 1;

show tables;
use test;

Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');

select * from logs;

drop table employee;

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int);
Truncate table Employee;
insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3');
insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4');
insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', '0');
insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', '0');

select * from employee;

select e1.name as employee from employee as e1 left join employee as e2 on e1.managerId = e2.id
where e1.salary > e2.salary;

drop table person;

Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (Id, Email) values ('1', 'a@b.com');
insert into Person (Id, Email) values ('2', 'c@d.com');
insert into Person (Id, Email) values ('3', 'a@b.com');

select * from person;

select email from (select email, COUNT(*) as count from person group by email) as t where t.count > 1;

Create table If Not Exists Customers (Id int, Name varchar(255));
Create table If Not Exists Orders (Id int, CustomerId int);
Truncate table Customers;
insert into Customers (Id, Name) values ('1', 'Joe');
insert into Customers (Id, Name) values ('2', 'Henry');
insert into Customers (Id, Name) values ('3', 'Sam');
insert into Customers (Id, Name) values ('4', 'Max');
Truncate table Orders;
insert into Orders (Id, CustomerId) values ('1', '3');
insert into Orders (Id, CustomerId) values ('2', '1');

select * from customers;
select * from orders;

select name as Customers from (select c.name, o.customerid from customers as c left join orders as o on c.id = o.customerid) as t where customerid is null;

drop table employee;

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
Truncate table Department;
insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');


select * from employee;
select * from department;

select t.name as department, ee.name as employee, ee.salary as salary from employee as ee left join 
(select max(e.salary) as msalary, d.name from employee as e left join department as d on e.DepartmentId = d.id group by d.name) as t
on ee.salary = t.msalary where t.msalary is not Null;


select * from logs;

select distinct l1.num as ConsecutiveNums from logs l1, logs l2, logs l3
where l1.id = l2.id-1 and l2.id = l3.id-1 and l1.num = l2.num and l2.num = l3.num;

use test;
drop table employee;
drop table department;


Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'mxc', '80000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('6', 'miles', '50000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('7', 'house', '60000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('8', 'jj', '110000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('9', 'perter', '50000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('10', 'kko', '30000', '2');
Truncate table Department;
insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');

select * from employee;
select * from department;

SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;




























